"""
Research orchestrator for coordinating all research phases.

Manages the execution of research queries in the correct order,
handles progress tracking, and produces the final research output.
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Callable, Any

from ..config import ResearchMode, PerplexityModel
from ..models import (
    CompanyInput,
    ResearchOutput,
    QueryResult,
    CompanyInfoTier,
)
from ..temporal import get_temporal_context, TemporalContext
from .perplexity_client import PerplexityClient
from .query_templates import QueryTemplates, QueryCategory, QueryTemplate
from .model_selector import ModelSelector
from .result_processor import ResultProcessor


class ResearchOrchestrator:
    """
    Orchestrates the complete research pipeline for a company.
    
    Research phases:
    1. Initial Discovery - Basic company info to determine info tier
    2. Company Deep Dive - Detailed company profile
    3. Industry Analysis - Industry context and trends
    4. Competitive Intelligence - Competitors and their AI adoption
    5. Technology Landscape - Tech stack and AI opportunities
    6. Regulatory Context - Compliance and regulatory requirements
    """
    
    # Query execution order by phase
    PHASE_QUERIES = {
        "initial_discovery": [
            "company_overview",
            "company_details",
            "recent_news",
        ],
        "company_deep_dive": [
            "leadership",
            "funding_status",
        ],
        "industry_analysis": [
            "industry_overview",
            "industry_challenges",
            "industry_opportunities",
        ],
        "competitive_intelligence": [
            "competitors_list",
            "competitor_ai",
        ],
        "technology_landscape": [
            "tech_stack",
            "ai_initiatives",
            "industry_ai_adoption",
            "ai_use_cases",
            "ai_tools",
        ],
        "regulatory_context": [
            "industry_regulations",
            "ai_regulations",
            "data_privacy",
        ],
    }
    
    def __init__(
        self,
        mode: ResearchMode = ResearchMode.QUICK,
        cache_dir: Optional[Path] = None,
        progress_callback: Optional[Callable[[str, float], None]] = None,
    ):
        """
        Initialize the research orchestrator.
        
        Args:
            mode: Research mode (quick or comprehensive).
            cache_dir: Directory for caching results.
            progress_callback: Callback for progress updates (phase, progress).
        """
        self.mode = mode
        self.cache_dir = cache_dir
        self.progress_callback = progress_callback
        
        # Initialize components
        self.client = PerplexityClient(cache_dir=cache_dir)
        self.templates = QueryTemplates()
        self.model_selector = ModelSelector(mode=mode)
        self.result_processor = ResultProcessor()
        self.temporal = get_temporal_context()
        
        # Track state
        self.current_phase = ""
        self.results: Dict[str, QueryResult] = {}
        self.info_tier = CompanyInfoTier.PUBLIC_MEDIUM
    
    def research(self, company_input: CompanyInput) -> ResearchOutput:
        """
        Execute the complete research pipeline.
        
        Args:
            company_input: Company input data.
        
        Returns:
            ResearchOutput with all research results.
        """
        company_name = company_input.name
        industry = company_input.industry or "technology"
        context = company_input.context
        
        self._report_progress("Starting research", 0)
        
        # Phase 1: Initial Discovery
        self._report_progress("initial_discovery", 0.05)
        self._execute_phase(
            "initial_discovery",
            company_name,
            industry,
        )
        
        # Detect info tier to adjust subsequent queries
        initial_results = [
            self.results[q]
            for q in self.PHASE_QUERIES["initial_discovery"]
            if q in self.results
        ]
        self.info_tier = self.result_processor.detect_info_tier(initial_results)
        self._report_progress(f"Detected info tier: {self.info_tier.value}", 0.15)
        
        # Phase 2: Company Deep Dive (comprehensive only for private companies)
        if self.mode == ResearchMode.COMPREHENSIVE or self.info_tier in [
            CompanyInfoTier.PRIVATE_LIMITED,
            CompanyInfoTier.STARTUP_STEALTH,
        ]:
            self._report_progress("company_deep_dive", 0.2)
            self._execute_phase("company_deep_dive", company_name, industry)
        
        # Phase 3: Industry Analysis
        self._report_progress("industry_analysis", 0.35)
        self._execute_phase("industry_analysis", company_name, industry)
        
        # Phase 4: Competitive Intelligence
        self._report_progress("competitive_intelligence", 0.5)
        self._execute_phase("competitive_intelligence", company_name, industry)
        
        # Phase 5: Technology Landscape
        self._report_progress("technology_landscape", 0.65)
        self._execute_phase("technology_landscape", company_name, industry)
        
        # Phase 6: Regulatory Context (comprehensive only)
        if self.mode == ResearchMode.COMPREHENSIVE:
            self._report_progress("regulatory_context", 0.8)
            self._execute_phase("regulatory_context", company_name, industry)
        
        # Build final output
        self._report_progress("Processing results", 0.9)
        output = self.result_processor.build_research_output(
            company_name=company_name,
            mode=self.mode,
            results=self.results,
            user_context=context,
        )
        
        # Update info tier in output
        output.information_tier = self.info_tier
        
        self._report_progress("Research complete", 1.0)
        
        return output
    
    def _execute_phase(
        self,
        phase: str,
        company_name: str,
        industry: str,
    ) -> None:
        """
        Execute all queries for a research phase.
        
        Args:
            phase: Phase name.
            company_name: Company name.
            industry: Industry.
        """
        self.current_phase = phase
        queries = self.PHASE_QUERIES.get(phase, [])
        
        # Filter queries based on mode
        if self.mode == ResearchMode.QUICK:
            queries = [
                q for q in queries
                if self.templates.get_template(q) and 
                self.templates.get_template(q).required_for_quick_mode
            ]
        
        for i, query_name in enumerate(queries):
            template = self.templates.get_template(query_name)
            if not template:
                continue
            
            # Render query
            query = self.templates.render_query(
                template,
                company_name=company_name,
                industry=industry,
            )
            
            # Select model
            selection = self.model_selector.select_model(
                template.category,
                info_tier=self.info_tier,
            )
            
            # Execute query
            result = self.client.search(
                query=query,
                max_results=10,
                search_recency_filter=template.recency_filter,
                model=selection.model,
            )
            
            # Store result
            self.results[query_name] = result
            
            # Update progress within phase
            phase_progress = (i + 1) / len(queries)
            self._report_progress(f"{phase}: {query_name}", None)
    
    def _report_progress(self, message: str, progress: Optional[float]) -> None:
        """Report progress to callback if set."""
        if self.progress_callback and progress is not None:
            self.progress_callback(message, progress)
    
    def get_cost_summary(self) -> Dict[str, Any]:
        """Get cost summary for the research session."""
        return self.client.get_cost_summary()
    
    def save_research_cache(self, output_dir: Path) -> None:
        """
        Save research results to cache file.
        
        Args:
            output_dir: Directory to save cache.
        """
        output_dir.mkdir(parents=True, exist_ok=True)
        cache_file = output_dir / "research_cache.json"
        
        cache_data = {
            "timestamp": datetime.now().isoformat(),
            "mode": self.mode.value,
            "info_tier": self.info_tier.value,
            "results": {
                name: {
                    "query": r.query,
                    "model_used": r.model_used,
                    "result_count": r.result_count,
                    "cost_estimate": r.cost_estimate,
                    "results": [
                        {
                            "title": sr.title,
                            "url": sr.url,
                            "snippet": sr.snippet[:500],  # Truncate for storage
                            "date": sr.date,
                        }
                        for sr in r.results
                    ],
                }
                for name, r in self.results.items()
            },
        }
        
        with open(cache_file, "w") as f:
            json.dump(cache_data, f, indent=2)
    
    def load_research_cache(self, cache_file: Path) -> bool:
        """
        Load research results from cache.
        
        Args:
            cache_file: Path to cache file.
        
        Returns:
            True if cache was loaded successfully.
        """
        if not cache_file.exists():
            return False
        
        try:
            with open(cache_file, "r") as f:
                data = json.load(f)
            
            self.mode = ResearchMode(data["mode"])
            self.info_tier = CompanyInfoTier(data["info_tier"])
            
            # Reconstruct results
            from ..models import SearchResult
            
            for name, result_data in data["results"].items():
                results = [
                    SearchResult(
                        title=r["title"],
                        url=r["url"],
                        snippet=r["snippet"],
                        date=r.get("date"),
                    )
                    for r in result_data["results"]
                ]
                
                self.results[name] = QueryResult(
                    query=result_data["query"],
                    model_used=result_data["model_used"],
                    results=results,
                    result_count=result_data["result_count"],
                    timestamp=datetime.fromisoformat(data["timestamp"]),
                    cost_estimate=result_data["cost_estimate"],
                )
            
            return True
            
        except Exception as e:
            print(f"Warning: Could not load cache: {e}")
            return False


def run_research(
    company_name: str,
    context: str = "",
    industry: str = "",
    mode: ResearchMode = ResearchMode.QUICK,
    cache_dir: Optional[Path] = None,
    progress_callback: Optional[Callable[[str, float], None]] = None,
) -> ResearchOutput:
    """
    Convenience function to run research for a company.
    
    Args:
        company_name: Company name.
        context: User-provided context.
        industry: Company industry.
        mode: Research mode.
        cache_dir: Cache directory.
        progress_callback: Progress callback.
    
    Returns:
        ResearchOutput with research results.
    """
    company_input = CompanyInput(
        name=company_name,
        context=context,
        mode=mode,
        industry=industry,
    )
    
    orchestrator = ResearchOrchestrator(
        mode=mode,
        cache_dir=cache_dir,
        progress_callback=progress_callback,
    )
    
    return orchestrator.research(company_input)
