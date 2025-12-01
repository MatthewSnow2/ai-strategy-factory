"""
Result processor for structuring Perplexity search results.

Transforms raw search results into structured data models
for use in the synthesis phase.
"""

import re
from typing import Dict, List, Optional, Any, Tuple
from datetime import datetime

from ..models import (
    QueryResult,
    SearchResult,
    CompanyProfile,
    IndustryContext,
    CompetitorProfile,
    TechLandscape,
    RegulatoryContext,
    ValidatedUserContext,
    ResearchOutput,
    CompanyInfoTier,
    CompanySize,
)
from ..config import ResearchMode
from .query_templates import QueryCategory


class ResultProcessor:
    """
    Processes raw Perplexity search results into structured models.
    
    Responsibilities:
    - Extract key information from search snippets
    - Structure data into Pydantic models
    - Detect company information availability tier
    - Validate and reconcile user-provided context
    """
    
    # Keywords for detecting company size
    SIZE_INDICATORS = {
        CompanySize.SMALL: ["startup", "small business", "boutique", "team of", "fewer than 100"],
        CompanySize.MEDIUM: ["mid-size", "midsize", "growing company", "100-500 employees"],
        CompanySize.LARGE: ["large company", "enterprise", "500+ employees", "global presence"],
        CompanySize.ENTERPRISE: ["fortune 500", "multinational", "thousands of employees", "10,000+"],
    }
    
    # Keywords for detecting information tier
    INFO_TIER_INDICATORS = {
        CompanyInfoTier.PUBLIC_LARGE: ["publicly traded", "nyse", "nasdaq", "fortune 500", "s&p 500"],
        CompanyInfoTier.PUBLIC_MEDIUM: ["founded", "headquarters", "ceo", "products"],
        CompanyInfoTier.PRIVATE_LIMITED: ["private company", "privately held"],
        CompanyInfoTier.STARTUP_STEALTH: ["stealth", "early-stage", "pre-launch"],
    }
    
    def __init__(self):
        """Initialize the result processor."""
        self.processed_count = 0
    
    def detect_info_tier(self, results: List[QueryResult]) -> CompanyInfoTier:
        """
        Detect the company's information availability tier.
        
        Args:
            results: Initial search results for the company.
        
        Returns:
            CompanyInfoTier indicating how much public info is available.
        """
        if not results:
            return CompanyInfoTier.PRIVATE_LIMITED
        
        # Combine all snippets for analysis
        all_text = " ".join(
            r.snippet.lower()
            for qr in results
            for r in qr.results
        )
        
        # Count results
        total_results = sum(qr.result_count for qr in results)
        
        # Check for tier indicators
        for tier, indicators in self.INFO_TIER_INDICATORS.items():
            for indicator in indicators:
                if indicator in all_text:
                    return tier
        
        # Fall back to result count heuristic
        if total_results >= 15:
            return CompanyInfoTier.PUBLIC_LARGE
        elif total_results >= 8:
            return CompanyInfoTier.PUBLIC_MEDIUM
        elif total_results >= 3:
            return CompanyInfoTier.PRIVATE_LIMITED
        else:
            return CompanyInfoTier.STARTUP_STEALTH
    
    def detect_company_size(self, results: List[QueryResult]) -> Tuple[CompanySize, Optional[int]]:
        """
        Detect company size from search results.
        
        Args:
            results: Search results about the company.
        
        Returns:
            Tuple of (CompanySize, estimated_employee_count).
        """
        all_text = " ".join(
            r.snippet.lower()
            for qr in results
            for r in qr.results
        )
        
        # Try to extract employee count
        employee_patterns = [
            r'(\d{1,3}(?:,\d{3})*)\s*(?:employees|staff|team members)',
            r'(?:employs|has)\s*(?:about|approximately|over|more than)?\s*(\d{1,3}(?:,\d{3})*)',
            r'workforce of\s*(\d{1,3}(?:,\d{3})*)',
        ]
        
        employee_count = None
        for pattern in employee_patterns:
            match = re.search(pattern, all_text)
            if match:
                count_str = match.group(1).replace(",", "")
                try:
                    employee_count = int(count_str)
                    break
                except ValueError:
                    continue
        
        # Determine size from count or indicators
        if employee_count:
            if employee_count < 100:
                return CompanySize.SMALL, employee_count
            elif employee_count < 500:
                return CompanySize.MEDIUM, employee_count
            elif employee_count < 2000:
                return CompanySize.LARGE, employee_count
            else:
                return CompanySize.ENTERPRISE, employee_count
        
        # Check size indicators
        for size, indicators in self.SIZE_INDICATORS.items():
            for indicator in indicators:
                if indicator in all_text:
                    return size, None
        
        return CompanySize.MEDIUM, None  # Default assumption
    
    def extract_company_profile(
        self,
        company_name: str,
        results: Dict[str, QueryResult],
    ) -> CompanyProfile:
        """
        Extract company profile from search results.
        
        Args:
            company_name: Company name.
            results: Dict of query name to QueryResult.
        
        Returns:
            CompanyProfile with extracted information.
        """
        profile = CompanyProfile()
        sources = set()
        
        # Extract from company overview results
        overview = results.get("company_overview")
        if overview and overview.results:
            profile.description = self._extract_first_paragraph(overview.results)
            sources.update(r.url for r in overview.results)
        
        # Extract from company details
        details = results.get("company_details")
        if details and details.results:
            all_results = [details]
            size, count = self.detect_company_size(all_results)
            profile.company_size = size
            profile.employee_estimate = count
            profile.headquarters = self._extract_location(details.results)
            profile.founded_year = self._extract_year(details.results, "founded")
            sources.update(r.url for r in details.results)
        
        # Extract leadership
        leadership = results.get("leadership")
        if leadership and leadership.results:
            profile.leadership = self._extract_leadership(leadership.results)
            sources.update(r.url for r in leadership.results)
        
        # Extract funding
        funding = results.get("funding_status")
        if funding and funding.results:
            profile.funding_status = self._extract_funding(funding.results)
            sources.update(r.url for r in funding.results)
        
        # Extract news
        news = results.get("recent_news")
        if news and news.results:
            profile.recent_news = self._extract_news(news.results)
            sources.update(r.url for r in news.results)
        
        # Extract products/services from description
        if profile.description:
            profile.products_services = self._extract_products(profile.description)
        
        profile.sources = list(sources)[:10]  # Limit sources
        return profile
    
    def extract_industry_context(
        self,
        results: Dict[str, QueryResult],
    ) -> IndustryContext:
        """
        Extract industry context from search results.
        
        Args:
            results: Dict of query name to QueryResult.
        
        Returns:
            IndustryContext with industry analysis.
        """
        context = IndustryContext()
        sources = set()
        
        # Extract from industry overview
        overview = results.get("industry_overview")
        if overview and overview.results:
            context.primary_industry = self._extract_industry_name(overview.results)
            context.market_size = self._extract_market_size(overview.results)
            context.growth_rate = self._extract_growth_rate(overview.results)
            context.key_trends = self._extract_trends(overview.results)
            sources.update(r.url for r in overview.results)
        
        # Extract challenges
        challenges = results.get("industry_challenges")
        if challenges and challenges.results:
            context.challenges = self._extract_list_items(challenges.results, "challenge")
            sources.update(r.url for r in challenges.results)
        
        # Extract opportunities
        opportunities = results.get("industry_opportunities")
        if opportunities and opportunities.results:
            context.opportunities = self._extract_list_items(opportunities.results, "opportunity")
            sources.update(r.url for r in opportunities.results)
        
        context.sources = list(sources)[:10]
        return context
    
    def extract_competitors(
        self,
        results: Dict[str, QueryResult],
    ) -> List[CompetitorProfile]:
        """
        Extract competitor profiles from search results.
        
        Args:
            results: Dict of query name to QueryResult.
        
        Returns:
            List of CompetitorProfile objects.
        """
        competitors = []
        
        comp_results = results.get("competitors_list")
        if not comp_results or not comp_results.results:
            return competitors
        
        # Extract competitor names from snippets
        competitor_names = self._extract_competitor_names(comp_results.results)
        
        for name in competitor_names[:5]:  # Limit to top 5
            competitors.append(CompetitorProfile(
                name=name,
                description="",  # Would need additional queries
                ai_initiatives=[],
                strengths=[],
                market_position="",
            ))
        
        # Enrich with AI info if available
        ai_results = results.get("competitor_ai")
        if ai_results and ai_results.results:
            ai_info = self._extract_competitor_ai(ai_results.results, competitor_names)
            for comp in competitors:
                if comp.name in ai_info:
                    comp.ai_initiatives = ai_info[comp.name]
        
        return competitors
    
    def extract_tech_landscape(
        self,
        results: Dict[str, QueryResult],
    ) -> TechLandscape:
        """
        Extract technology landscape from search results.
        
        Args:
            results: Dict of query name to QueryResult.
        
        Returns:
            TechLandscape with technology analysis.
        """
        landscape = TechLandscape()
        sources = set()
        
        # Extract tech stack
        tech = results.get("tech_stack")
        if tech and tech.results:
            landscape.company_tech_stack = self._extract_technologies(tech.results)
            sources.update(r.url for r in tech.results)
        
        # Extract AI initiatives
        ai = results.get("ai_initiatives")
        if ai and ai.results:
            landscape.company_ai_initiatives = self._extract_ai_initiatives(ai.results)
            sources.update(r.url for r in ai.results)
        
        # Extract industry AI adoption
        adoption = results.get("industry_ai_adoption")
        if adoption and adoption.results:
            landscape.industry_ai_adoption_rate = self._extract_adoption_rate(adoption.results)
            sources.update(r.url for r in adoption.results)
        
        # Extract use cases
        use_cases = results.get("ai_use_cases")
        if use_cases and use_cases.results:
            landscape.industry_ai_use_cases = self._extract_use_cases(use_cases.results)
            sources.update(r.url for r in use_cases.results)
        
        # Extract recommended tools
        tools = results.get("ai_tools")
        if tools and tools.results:
            landscape.recommended_ai_tools = self._extract_tools(tools.results)
            sources.update(r.url for r in tools.results)
        
        landscape.sources = list(sources)[:10]
        return landscape
    
    def extract_regulatory_context(
        self,
        results: Dict[str, QueryResult],
    ) -> RegulatoryContext:
        """
        Extract regulatory context from search results.
        
        Args:
            results: Dict of query name to QueryResult.
        
        Returns:
            RegulatoryContext with compliance information.
        """
        context = RegulatoryContext()
        sources = set()
        
        # Extract industry regulations
        regs = results.get("industry_regulations")
        if regs and regs.results:
            context.industry_regulations = self._extract_regulations(regs.results)
            sources.update(r.url for r in regs.results)
        
        # Extract AI regulations
        ai_regs = results.get("ai_regulations")
        if ai_regs and ai_regs.results:
            context.ai_regulations = self._extract_regulations(ai_regs.results)
            sources.update(r.url for r in ai_regs.results)
        
        # Extract data privacy
        privacy = results.get("data_privacy")
        if privacy and privacy.results:
            context.data_privacy_requirements = self._extract_privacy_requirements(privacy.results)
            sources.update(r.url for r in privacy.results)
        
        context.sources = list(sources)[:10]
        return context
    
    def validate_user_context(
        self,
        user_context: str,
        research_results: Dict[str, QueryResult],
    ) -> ValidatedUserContext:
        """
        Validate user-provided context against research results.
        
        Args:
            user_context: User-provided context string.
            research_results: Results from research queries.
        
        Returns:
            ValidatedUserContext with validation results.
        """
        validated = ValidatedUserContext(original_context=user_context)
        
        if not user_context:
            return validated
        
        # Extract claims from user context
        # This is a simplified implementation - could use NLP for better extraction
        validated.extracted_info = {
            "raw_context": user_context,
        }
        
        # Compare with research results
        all_text = " ".join(
            r.snippet.lower()
            for qr in research_results.values()
            for r in qr.results
        ).lower()
        
        user_lower = user_context.lower()
        
        # Check for potential conflicts (simplified)
        if "employees" in user_lower:
            validated.unverified_claims.append("Employee count claim - verify against research")
        
        return validated
    
    def build_research_output(
        self,
        company_name: str,
        mode: ResearchMode,
        results: Dict[str, QueryResult],
        user_context: str = "",
    ) -> ResearchOutput:
        """
        Build complete research output from all results.
        
        Args:
            company_name: Company name.
            mode: Research mode used.
            results: All query results.
            user_context: User-provided context.
        
        Returns:
            Complete ResearchOutput model.
        """
        # Detect info tier from initial results
        initial_results = [
            r for name, r in results.items()
            if name in ["company_overview", "company_details", "recent_news"]
        ]
        info_tier = self.detect_info_tier(initial_results)
        
        # Build all sections
        output = ResearchOutput(
            company_name=company_name,
            research_timestamp=datetime.now(),
            research_mode=mode,
            information_tier=info_tier,
            profile=self.extract_company_profile(company_name, results),
            industry=self.extract_industry_context(results),
            competitors=self.extract_competitors(results),
            tech_landscape=self.extract_tech_landscape(results),
            regulatory=self.extract_regulatory_context(results),
            user_context=self.validate_user_context(user_context, results),
            raw_queries=list(results.values()),
            total_cost=sum(r.cost_estimate for r in results.values()),
        )
        
        # Calculate confidence scores
        output.confidence_scores = self._calculate_confidence(results)
        
        self.processed_count += 1
        return output
    
    # Helper methods for extraction
    
    def _extract_first_paragraph(self, results: List[SearchResult]) -> str:
        """Extract first meaningful paragraph from results."""
        for r in results:
            if r.snippet and len(r.snippet) > 100:
                # Get first sentence or paragraph
                paragraphs = r.snippet.split("\n\n")
                if paragraphs:
                    return paragraphs[0][:500]
        return ""
    
    def _extract_location(self, results: List[SearchResult]) -> str:
        """Extract headquarters location."""
        patterns = [
            r'headquartered in ([^,.]+)',
            r'headquarters in ([^,.]+)',
            r'based in ([^,.]+)',
            r'located in ([^,.]+)',
        ]
        
        for r in results:
            text = r.snippet.lower()
            for pattern in patterns:
                match = re.search(pattern, text)
                if match:
                    return match.group(1).strip().title()
        return ""
    
    def _extract_year(self, results: List[SearchResult], keyword: str) -> Optional[int]:
        """Extract a year associated with a keyword."""
        pattern = rf'{keyword}\s*(?:in)?\s*(\d{{4}})'
        
        for r in results:
            match = re.search(pattern, r.snippet.lower())
            if match:
                try:
                    return int(match.group(1))
                except ValueError:
                    continue
        return None
    
    def _extract_leadership(self, results: List[SearchResult]) -> List[Dict[str, str]]:
        """Extract leadership information."""
        leaders = []
        titles = ["ceo", "cto", "cfo", "coo", "founder", "president"]
        
        for r in results:
            text = r.snippet
            for title in titles:
                pattern = rf'({title})[,:\s]+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)+)'
                matches = re.findall(pattern, text, re.IGNORECASE)
                for match in matches:
                    leaders.append({
                        "title": match[0].upper(),
                        "name": match[1],
                    })
        
        return leaders[:5]  # Limit
    
    def _extract_funding(self, results: List[SearchResult]) -> str:
        """Extract funding status."""
        for r in results:
            text = r.snippet.lower()
            if "raised" in text or "funding" in text or "series" in text:
                # Get the sentence containing funding info
                sentences = r.snippet.split(".")
                for s in sentences:
                    if any(word in s.lower() for word in ["raised", "funding", "series", "valuation"]):
                        return s.strip()[:200]
        return ""
    
    def _extract_news(self, results: List[SearchResult]) -> List[Dict[str, str]]:
        """Extract recent news items."""
        news = []
        for r in results[:5]:
            news.append({
                "title": r.title,
                "url": r.url,
                "date": r.date or "",
            })
        return news
    
    def _extract_products(self, description: str) -> List[str]:
        """Extract products/services from description."""
        # Simple extraction - look for common patterns
        products = []
        patterns = [
            r'offers? ([^,.]+)',
            r'provides? ([^,.]+)',
            r'specializ(?:es|ing) in ([^,.]+)',
        ]
        
        for pattern in patterns:
            matches = re.findall(pattern, description.lower())
            products.extend(matches)
        
        return list(set(products))[:5]
    
    def _extract_industry_name(self, results: List[SearchResult]) -> str:
        """Extract primary industry name."""
        for r in results:
            if r.title:
                # Often the industry is in the title
                return r.title.split("-")[0].strip()[:50]
        return ""
    
    def _extract_market_size(self, results: List[SearchResult]) -> str:
        """Extract market size information."""
        patterns = [
            r'\$[\d.]+\s*(?:billion|million|trillion)',
            r'market (?:size|value)[^.]*\$[\d.]+',
        ]
        
        for r in results:
            for pattern in patterns:
                match = re.search(pattern, r.snippet.lower())
                if match:
                    return match.group(0)
        return ""
    
    def _extract_growth_rate(self, results: List[SearchResult]) -> str:
        """Extract growth rate information."""
        patterns = [
            r'(\d+(?:\.\d+)?%)\s*(?:growth|cagr|increase)',
            r'growing at (\d+(?:\.\d+)?%)',
        ]
        
        for r in results:
            for pattern in patterns:
                match = re.search(pattern, r.snippet.lower())
                if match:
                    return match.group(1)
        return ""
    
    def _extract_trends(self, results: List[SearchResult]) -> List[str]:
        """Extract key trends."""
        trends = []
        trend_keywords = ["trend", "emerging", "growing", "rising", "shift toward"]
        
        for r in results:
            sentences = r.snippet.split(".")
            for s in sentences:
                if any(kw in s.lower() for kw in trend_keywords):
                    trends.append(s.strip()[:150])
        
        return list(set(trends))[:5]
    
    def _extract_list_items(self, results: List[SearchResult], context: str) -> List[str]:
        """Extract list items from results."""
        items = []
        for r in results:
            sentences = r.snippet.split(".")
            for s in sentences:
                if len(s) > 20 and len(s) < 200:
                    items.append(s.strip())
        return list(set(items))[:5]
    
    def _extract_competitor_names(self, results: List[SearchResult]) -> List[str]:
        """Extract competitor company names."""
        names = []
        # Look for capitalized words that might be company names
        for r in results:
            # Simple heuristic: find capitalized multi-word names
            pattern = r'(?:competitor|alternative|similar)[^.]*([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)'
            matches = re.findall(pattern, r.snippet)
            names.extend(matches)
        
        return list(set(names))[:5]
    
    def _extract_competitor_ai(
        self,
        results: List[SearchResult],
        competitor_names: List[str],
    ) -> Dict[str, List[str]]:
        """Extract AI initiatives by competitor."""
        ai_info = {}
        
        for name in competitor_names:
            initiatives = []
            for r in results:
                if name.lower() in r.snippet.lower():
                    # Extract AI-related sentences mentioning this competitor
                    sentences = r.snippet.split(".")
                    for s in sentences:
                        if name.lower() in s.lower() and "ai" in s.lower():
                            initiatives.append(s.strip()[:100])
            ai_info[name] = initiatives[:3]
        
        return ai_info
    
    def _extract_technologies(self, results: List[SearchResult]) -> List[str]:
        """Extract technology names."""
        tech_keywords = [
            "aws", "azure", "gcp", "kubernetes", "docker", "python", "java",
            "react", "angular", "vue", "node", "postgresql", "mongodb",
            "salesforce", "sap", "oracle", "microsoft", "google", "amazon"
        ]
        
        found = []
        for r in results:
            text = r.snippet.lower()
            for tech in tech_keywords:
                if tech in text and tech not in found:
                    found.append(tech.title())
        
        return found[:10]
    
    def _extract_ai_initiatives(self, results: List[SearchResult]) -> List[str]:
        """Extract AI initiative descriptions."""
        initiatives = []
        for r in results:
            sentences = r.snippet.split(".")
            for s in sentences:
                if any(kw in s.lower() for kw in ["ai", "machine learning", "automation"]):
                    initiatives.append(s.strip()[:150])
        return list(set(initiatives))[:5]
    
    def _extract_adoption_rate(self, results: List[SearchResult]) -> str:
        """Extract AI adoption rate."""
        patterns = [
            r'(\d+(?:\.\d+)?%)\s*(?:adoption|using ai|implemented)',
            r'adoption rate of (\d+(?:\.\d+)?%)',
        ]
        
        for r in results:
            for pattern in patterns:
                match = re.search(pattern, r.snippet.lower())
                if match:
                    return match.group(1)
        return ""
    
    def _extract_use_cases(self, results: List[SearchResult]) -> List[Dict[str, Any]]:
        """Extract AI use cases."""
        use_cases = []
        for r in results[:5]:
            use_cases.append({
                "description": r.snippet[:200],
                "source": r.url,
            })
        return use_cases
    
    def _extract_tools(self, results: List[SearchResult]) -> List[Dict[str, Any]]:
        """Extract recommended AI tools."""
        tools = []
        tool_patterns = [
            r'([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)\s+(?:is a|provides|offers)',
        ]
        
        for r in results:
            for pattern in tool_patterns:
                matches = re.findall(pattern, r.snippet)
                for match in matches:
                    tools.append({
                        "name": match,
                        "description": "",
                        "source": r.url,
                    })
        
        return tools[:5]
    
    def _extract_regulations(self, results: List[SearchResult]) -> List[str]:
        """Extract regulation names/descriptions."""
        regs = []
        for r in results:
            sentences = r.snippet.split(".")
            for s in sentences:
                if any(kw in s.lower() for kw in ["regulation", "compliance", "requirement", "law"]):
                    regs.append(s.strip()[:150])
        return list(set(regs))[:5]
    
    def _extract_privacy_requirements(self, results: List[SearchResult]) -> List[str]:
        """Extract privacy requirements."""
        privacy = []
        keywords = ["gdpr", "ccpa", "hipaa", "privacy", "data protection"]
        
        for r in results:
            sentences = r.snippet.split(".")
            for s in sentences:
                if any(kw in s.lower() for kw in keywords):
                    privacy.append(s.strip()[:150])
        
        return list(set(privacy))[:5]
    
    def _calculate_confidence(self, results: Dict[str, QueryResult]) -> Dict[str, float]:
        """Calculate confidence scores for each research section."""
        confidence = {}
        
        sections = {
            "profile": ["company_overview", "company_details", "leadership"],
            "industry": ["industry_overview", "industry_challenges"],
            "competitors": ["competitors_list"],
            "technology": ["tech_stack", "ai_initiatives"],
            "regulatory": ["industry_regulations", "ai_regulations"],
        }
        
        for section, queries in sections.items():
            total_results = 0
            for q in queries:
                if q in results:
                    total_results += results[q].result_count
            
            # Simple confidence based on result count
            if total_results >= 10:
                confidence[section] = 0.9
            elif total_results >= 5:
                confidence[section] = 0.7
            elif total_results >= 2:
                confidence[section] = 0.5
            else:
                confidence[section] = 0.3
        
        return confidence
