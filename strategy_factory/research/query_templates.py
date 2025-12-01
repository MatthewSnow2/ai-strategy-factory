"""
Query templates for Perplexity research.

Provides structured query templates for different research categories,
with temporal awareness and company context injection.
"""

from typing import Dict, List, Optional, Any
from enum import Enum
from dataclasses import dataclass

from ..temporal import TemporalContext, get_temporal_context


class QueryCategory(str, Enum):
    """Categories of research queries."""
    COMPANY_PROFILE = "company_profile"
    INDUSTRY = "industry"
    COMPETITORS = "competitors"
    TECHNOLOGY = "technology"
    AI_INITIATIVES = "ai_initiatives"
    REGULATORY = "regulatory"
    NEWS = "news"
    LEADERSHIP = "leadership"
    FUNDING = "funding"


@dataclass
class QueryTemplate:
    """Represents a query template with metadata."""
    name: str
    category: QueryCategory
    template: str
    recency_filter: str  # day, week, month, year
    priority: int  # 1 = highest priority
    required_for_quick_mode: bool
    description: str


class QueryTemplates:
    """
    Repository of query templates for company research.
    
    Templates use placeholders:
    - {company_name}: Company name
    - {industry}: Company's industry (if known)
    - {context}: User-provided context
    - Temporal placeholders from TemporalContext
    """
    
    # Company Profile Queries
    COMPANY_OVERVIEW = QueryTemplate(
        name="company_overview",
        category=QueryCategory.COMPANY_PROFILE,
        template='{company_name} company overview business model products services {current_year}',
        recency_filter="year",
        priority=1,
        required_for_quick_mode=True,
        description="Basic company overview and business model",
    )
    
    COMPANY_DETAILS = QueryTemplate(
        name="company_details",
        category=QueryCategory.COMPANY_PROFILE,
        template='{company_name} headquarters location employee count company size founded year',
        recency_filter="year",
        priority=2,
        required_for_quick_mode=True,
        description="Company details including size and location",
    )
    
    LEADERSHIP = QueryTemplate(
        name="leadership",
        category=QueryCategory.LEADERSHIP,
        template='{company_name} CEO leadership team executives management {current_year}',
        recency_filter="year",
        priority=3,
        required_for_quick_mode=False,
        description="Leadership team and key executives",
    )
    
    FUNDING_STATUS = QueryTemplate(
        name="funding_status",
        category=QueryCategory.FUNDING,
        template='{company_name} funding investment valuation investors {current_year}',
        recency_filter="year",
        priority=3,
        required_for_quick_mode=False,
        description="Funding and investment information",
    )
    
    RECENT_NEWS = QueryTemplate(
        name="recent_news",
        category=QueryCategory.NEWS,
        template='{company_name} latest news announcements developments {current_month_year}',
        recency_filter="month",
        priority=2,
        required_for_quick_mode=True,
        description="Recent company news and announcements",
    )
    
    # Industry Queries
    INDUSTRY_OVERVIEW = QueryTemplate(
        name="industry_overview",
        category=QueryCategory.INDUSTRY,
        template='{industry} industry market size growth trends {current_year}',
        recency_filter="year",
        priority=1,
        required_for_quick_mode=True,
        description="Industry overview and market analysis",
    )
    
    INDUSTRY_CHALLENGES = QueryTemplate(
        name="industry_challenges",
        category=QueryCategory.INDUSTRY,
        template='{industry} industry challenges pain points problems {current_year}',
        recency_filter="year",
        priority=2,
        required_for_quick_mode=True,
        description="Industry challenges and pain points",
    )
    
    INDUSTRY_OPPORTUNITIES = QueryTemplate(
        name="industry_opportunities",
        category=QueryCategory.INDUSTRY,
        template='{industry} industry opportunities growth areas emerging trends {current_year}',
        recency_filter="year",
        priority=2,
        required_for_quick_mode=False,
        description="Industry opportunities and growth areas",
    )
    
    # Competitor Queries
    COMPETITORS_LIST = QueryTemplate(
        name="competitors_list",
        category=QueryCategory.COMPETITORS,
        template='{company_name} competitors similar companies alternatives {industry}',
        recency_filter="year",
        priority=2,
        required_for_quick_mode=True,
        description="Main competitors and alternatives",
    )
    
    COMPETITOR_AI = QueryTemplate(
        name="competitor_ai",
        category=QueryCategory.COMPETITORS,
        template='{industry} companies AI adoption artificial intelligence initiatives {current_year}',
        recency_filter="month",
        priority=2,
        required_for_quick_mode=False,
        description="Competitor AI adoption and initiatives",
    )
    
    # Technology Queries
    TECH_STACK = QueryTemplate(
        name="tech_stack",
        category=QueryCategory.TECHNOLOGY,
        template='{company_name} technology stack software platforms tools infrastructure',
        recency_filter="year",
        priority=2,
        required_for_quick_mode=False,
        description="Company technology stack and platforms",
    )
    
    AI_INITIATIVES = QueryTemplate(
        name="ai_initiatives",
        category=QueryCategory.AI_INITIATIVES,
        template='{company_name} AI artificial intelligence machine learning initiatives projects {current_year}',
        recency_filter="month",
        priority=1,
        required_for_quick_mode=True,
        description="Company AI initiatives and projects",
    )
    
    INDUSTRY_AI_ADOPTION = QueryTemplate(
        name="industry_ai_adoption",
        category=QueryCategory.AI_INITIATIVES,
        template='{industry} AI adoption rate artificial intelligence use cases {current_year}',
        recency_filter="month",
        priority=1,
        required_for_quick_mode=True,
        description="Industry-wide AI adoption trends",
    )
    
    AI_USE_CASES = QueryTemplate(
        name="ai_use_cases",
        category=QueryCategory.AI_INITIATIVES,
        template='{industry} industry AI use cases applications generative AI {current_year}',
        recency_filter="month",
        priority=1,
        required_for_quick_mode=True,
        description="Industry-specific AI use cases",
    )
    
    AI_TOOLS = QueryTemplate(
        name="ai_tools",
        category=QueryCategory.AI_INITIATIVES,
        template='{industry} recommended AI tools platforms enterprise software {current_year}',
        recency_filter="month",
        priority=2,
        required_for_quick_mode=False,
        description="Recommended AI tools for the industry",
    )
    
    # Regulatory Queries
    INDUSTRY_REGULATIONS = QueryTemplate(
        name="industry_regulations",
        category=QueryCategory.REGULATORY,
        template='{industry} industry regulations compliance requirements {current_year}',
        recency_filter="year",
        priority=3,
        required_for_quick_mode=False,
        description="Industry-specific regulations",
    )
    
    AI_REGULATIONS = QueryTemplate(
        name="ai_regulations",
        category=QueryCategory.REGULATORY,
        template='AI artificial intelligence regulations compliance requirements {industry} {current_year}',
        recency_filter="month",
        priority=2,
        required_for_quick_mode=False,
        description="AI-specific regulations and compliance",
    )
    
    DATA_PRIVACY = QueryTemplate(
        name="data_privacy",
        category=QueryCategory.REGULATORY,
        template='{industry} data privacy requirements GDPR CCPA compliance {current_year}',
        recency_filter="year",
        priority=3,
        required_for_quick_mode=False,
        description="Data privacy requirements",
    )
    
    # All templates as a dictionary
    ALL_TEMPLATES: Dict[str, QueryTemplate] = {
        "company_overview": COMPANY_OVERVIEW,
        "company_details": COMPANY_DETAILS,
        "leadership": LEADERSHIP,
        "funding_status": FUNDING_STATUS,
        "recent_news": RECENT_NEWS,
        "industry_overview": INDUSTRY_OVERVIEW,
        "industry_challenges": INDUSTRY_CHALLENGES,
        "industry_opportunities": INDUSTRY_OPPORTUNITIES,
        "competitors_list": COMPETITORS_LIST,
        "competitor_ai": COMPETITOR_AI,
        "tech_stack": TECH_STACK,
        "ai_initiatives": AI_INITIATIVES,
        "industry_ai_adoption": INDUSTRY_AI_ADOPTION,
        "ai_use_cases": AI_USE_CASES,
        "ai_tools": AI_TOOLS,
        "industry_regulations": INDUSTRY_REGULATIONS,
        "ai_regulations": AI_REGULATIONS,
        "data_privacy": DATA_PRIVACY,
    }
    
    def __init__(self, temporal: Optional[TemporalContext] = None):
        """
        Initialize query templates with temporal context.
        
        Args:
            temporal: TemporalContext for date injection. Uses current date if not provided.
        """
        self.temporal = temporal or get_temporal_context()
    
    def get_template(self, name: str) -> Optional[QueryTemplate]:
        """Get a query template by name."""
        return self.ALL_TEMPLATES.get(name)
    
    def get_templates_by_category(self, category: QueryCategory) -> List[QueryTemplate]:
        """Get all templates for a category."""
        return [t for t in self.ALL_TEMPLATES.values() if t.category == category]
    
    def get_quick_mode_templates(self) -> List[QueryTemplate]:
        """Get templates required for quick mode."""
        return [t for t in self.ALL_TEMPLATES.values() if t.required_for_quick_mode]
    
    def get_comprehensive_templates(self) -> List[QueryTemplate]:
        """Get all templates (for comprehensive mode)."""
        return list(self.ALL_TEMPLATES.values())
    
    def render_query(
        self,
        template: QueryTemplate,
        company_name: str,
        industry: str = "",
        context: str = "",
        **extra_vars,
    ) -> str:
        """
        Render a query template with all variables.
        
        Args:
            template: QueryTemplate to render.
            company_name: Company name.
            industry: Industry (optional).
            context: User context (optional).
            **extra_vars: Additional variables.
        
        Returns:
            Rendered query string.
        """
        variables = {
            "company_name": company_name,
            "industry": industry or "technology",
            "context": context,
            **extra_vars,
        }
        
        return self.temporal.inject(template.template, **variables)
    
    def render_all_queries(
        self,
        company_name: str,
        industry: str = "",
        context: str = "",
        quick_mode: bool = True,
    ) -> Dict[str, Dict[str, Any]]:
        """
        Render all applicable queries for a company.
        
        Args:
            company_name: Company name.
            industry: Industry.
            context: User context.
            quick_mode: If True, only render quick mode queries.
        
        Returns:
            Dict mapping template name to rendered query and metadata.
        """
        templates = self.get_quick_mode_templates() if quick_mode else self.get_comprehensive_templates()
        
        rendered = {}
        for template in templates:
            query = self.render_query(template, company_name, industry, context)
            rendered[template.name] = {
                "query": query,
                "category": template.category.value,
                "recency_filter": template.recency_filter,
                "priority": template.priority,
            }
        
        return rendered
    
    def get_queries_by_priority(
        self,
        company_name: str,
        industry: str = "",
        quick_mode: bool = True,
    ) -> List[Dict[str, Any]]:
        """
        Get queries sorted by priority.
        
        Args:
            company_name: Company name.
            industry: Industry.
            quick_mode: If True, only include quick mode queries.
        
        Returns:
            List of query dicts sorted by priority.
        """
        rendered = self.render_all_queries(company_name, industry, quick_mode=quick_mode)
        
        queries = [
            {"name": name, **data}
            for name, data in rendered.items()
        ]
        
        return sorted(queries, key=lambda x: x["priority"])
