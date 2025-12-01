"""
Knowledge loader for TLDR consulting guides.

Handles selective loading of TLDR guides based on deliverable needs
to optimize context window usage.
"""

from pathlib import Path
from typing import List, Dict, Optional, Set
import logging

from .config import TLDR_GUIDES_DIR, DELIVERABLES, TLDR_TOPIC_MAPPING

logger = logging.getLogger(__name__)


class KnowledgeLoader:
    """
    Loads and manages TLDR consulting guide content.

    Usage:
        loader = KnowledgeLoader()

        # Load guides for a specific deliverable
        content = loader.load_for_deliverable("04_maturity_assessment")

        # Load guides for a topic
        content = loader.load_for_topic("maturity")

        # Load specific guides
        content = loader.load_guides(["bcg-wheres-the-value-in-ai_TLDR.md"])
    """

    def __init__(self, guides_dir: Path = TLDR_GUIDES_DIR):
        """
        Initialize knowledge loader.

        Args:
            guides_dir: Path to TLDR guides directory
        """
        self.guides_dir = Path(guides_dir)
        self._cache: Dict[str, str] = {}
        self._available_guides: Optional[List[str]] = None

    @property
    def available_guides(self) -> List[str]:
        """Get list of available TLDR guide files."""
        if self._available_guides is None:
            self._available_guides = [
                f.name for f in self.guides_dir.glob("*_TLDR.md")
            ]
        return self._available_guides

    def load_guide(self, filename: str) -> Optional[str]:
        """
        Load a single guide file.

        Args:
            filename: Name of the guide file

        Returns:
            Content of the guide or None if not found
        """
        # Check cache first
        if filename in self._cache:
            return self._cache[filename]

        file_path = self.guides_dir / filename
        if not file_path.exists():
            logger.warning(f"Guide not found: {filename}")
            return None

        try:
            content = file_path.read_text(encoding='utf-8')
            self._cache[filename] = content
            logger.debug(f"Loaded guide: {filename} ({len(content)} chars)")
            return content
        except Exception as e:
            logger.error(f"Error loading guide {filename}: {e}")
            return None

    def load_guides(self, filenames: List[str]) -> str:
        """
        Load multiple guide files and combine them.

        Args:
            filenames: List of guide filenames to load

        Returns:
            Combined content with separators
        """
        contents = []
        for filename in filenames:
            content = self.load_guide(filename)
            if content:
                # Add header for context
                header = f"\n{'='*60}\n# Source: {filename}\n{'='*60}\n"
                contents.append(header + content)

        return "\n\n".join(contents)

    def load_for_deliverable(self, deliverable_id: str) -> str:
        """
        Load relevant guides for a specific deliverable.

        Args:
            deliverable_id: ID of the deliverable (e.g., "04_maturity_assessment")

        Returns:
            Combined content of relevant guides
        """
        deliverable_info = DELIVERABLES.get(deliverable_id, {})
        guide_files = deliverable_info.get("tldr_guides", [])

        if not guide_files:
            logger.info(f"No specific guides for {deliverable_id}")
            return ""

        return self.load_guides(guide_files)

    def load_for_topic(self, topic: str) -> str:
        """
        Load guides relevant to a topic.

        Args:
            topic: Topic key from TLDR_TOPIC_MAPPING

        Returns:
            Combined content of relevant guides
        """
        guide_files = TLDR_TOPIC_MAPPING.get(topic, [])

        if not guide_files:
            logger.warning(f"Unknown topic: {topic}")
            return ""

        return self.load_guides(guide_files)

    def load_for_deliverables(self, deliverable_ids: List[str]) -> str:
        """
        Load guides for multiple deliverables (deduplicated).

        Args:
            deliverable_ids: List of deliverable IDs

        Returns:
            Combined content of all relevant guides (no duplicates)
        """
        guide_files: Set[str] = set()

        for deliverable_id in deliverable_ids:
            deliverable_info = DELIVERABLES.get(deliverable_id, {})
            guide_files.update(deliverable_info.get("tldr_guides", []))

        return self.load_guides(list(guide_files))

    def load_all(self) -> str:
        """
        Load all available guides.

        Warning: This may be too large for a single context window.

        Returns:
            Combined content of all guides
        """
        return self.load_guides(self.available_guides)

    def get_guide_summary(self) -> Dict[str, Dict[str, any]]:
        """
        Get summary information about available guides.

        Returns:
            Dict mapping filename to {size, topics, deliverables}
        """
        summary = {}

        for filename in self.available_guides:
            content = self.load_guide(filename)
            if content:
                # Find which topics use this guide
                topics = [
                    topic for topic, guides in TLDR_TOPIC_MAPPING.items()
                    if filename in guides
                ]

                # Find which deliverables use this guide
                deliverables = [
                    d_id for d_id, d_info in DELIVERABLES.items()
                    if filename in d_info.get("tldr_guides", [])
                ]

                summary[filename] = {
                    "size_chars": len(content),
                    "size_tokens_estimate": len(content) // 4,  # Rough estimate
                    "topics": topics,
                    "deliverables": deliverables
                }

        return summary

    def estimate_tokens(self, content: str) -> int:
        """
        Estimate token count for content.

        Uses rough approximation of 1 token ≈ 4 characters.

        Args:
            content: Text content

        Returns:
            Estimated token count
        """
        return len(content) // 4

    def get_loading_plan(self, deliverable_ids: List[str]) -> Dict[str, any]:
        """
        Get a loading plan for a set of deliverables.

        Args:
            deliverable_ids: List of deliverable IDs to generate

        Returns:
            Dict with guides to load and estimated token usage
        """
        guide_files: Set[str] = set()
        guide_to_deliverables: Dict[str, List[str]] = {}

        for deliverable_id in deliverable_ids:
            deliverable_info = DELIVERABLES.get(deliverable_id, {})
            for guide in deliverable_info.get("tldr_guides", []):
                guide_files.add(guide)
                if guide not in guide_to_deliverables:
                    guide_to_deliverables[guide] = []
                guide_to_deliverables[guide].append(deliverable_id)

        # Calculate sizes
        total_chars = 0
        guide_sizes = {}
        for guide in guide_files:
            content = self.load_guide(guide)
            if content:
                size = len(content)
                guide_sizes[guide] = size
                total_chars += size

        return {
            "guides": list(guide_files),
            "guide_sizes": guide_sizes,
            "guide_to_deliverables": guide_to_deliverables,
            "total_chars": total_chars,
            "estimated_tokens": total_chars // 4,
            "deliverable_count": len(deliverable_ids)
        }

    def clear_cache(self):
        """Clear the content cache."""
        self._cache.clear()
        logger.info("Knowledge cache cleared")


# Framework extraction helpers
def extract_framework(content: str, framework_name: str) -> Optional[str]:
    """
    Extract a specific framework section from guide content.

    Args:
        content: Full guide content
        framework_name: Name of the framework to extract

    Returns:
        Extracted framework section or None
    """
    # Look for the framework name in headers
    import re

    # Try to find a section with this framework name
    patterns = [
        rf"##\s*{re.escape(framework_name)}.*?(?=\n##|\Z)",
        rf"###\s*{re.escape(framework_name)}.*?(?=\n###|\n##|\Z)",
        rf"\*\*{re.escape(framework_name)}\*\*.*?(?=\n\*\*|\n##|\Z)",
    ]

    for pattern in patterns:
        match = re.search(pattern, content, re.IGNORECASE | re.DOTALL)
        if match:
            return match.group(0).strip()

    return None


def get_key_frameworks() -> Dict[str, Dict[str, str]]:
    """
    Get mapping of key frameworks to their source files and descriptions.

    Returns:
        Dict mapping framework names to their metadata
    """
    return {
        "BCG AI Maturity Curve": {
            "source": "bcg-wheres-the-value-in-ai_TLDR.md",
            "description": "Four stages: Stagnating, Emerging, Scaling, Future-Built",
            "use_for": ["maturity_assessment"]
        },
        "10-20-70 Model": {
            "source": "bcg-wheres-the-value-in-ai_TLDR.md",
            "description": "Resource allocation: 10% new ventures, 20% scaling, 70% core",
            "use_for": ["roadmap", "roi_calculator"]
        },
        "KPMG TACO Framework": {
            "source": "kpmg-agentic-ai-advantage_TLDR.md",
            "description": "Agent types: Taskers, Automators, Collaborators, Orchestrators",
            "use_for": ["use_case_library", "maturity_assessment"]
        },
        "Six AI Primitives": {
            "source": "identifying-and-scaling-ai-use-cases_TLDR.md",
            "description": "Content creation, Research, Coding, Data analysis, Ideation, Automation",
            "use_for": ["use_case_library", "quick_wins"]
        },
        "Impact/Effort Framework": {
            "source": "identifying-and-scaling-ai-use-cases_TLDR.md",
            "description": "Prioritization matrix for use cases",
            "use_for": ["use_case_library", "quick_wins", "roadmap"]
        },
        "Five ROI Areas": {
            "source": "google_cloud_roi_of_ai_2025_TLDR.md",
            "description": "Productivity, Customer experience, Business growth, Marketing, Security",
            "use_for": ["roi_calculator", "use_case_library"]
        },
        "Agentic Organization Model": {
            "source": "the-agentic-organization-contours-of-the-next-paradigm-for-the-ai-era_TLDR.md",
            "description": "Hybrid human-agent teams, M-shaped supervisors, T-shaped experts",
            "use_for": ["change_management", "roadmap"]
        },
        "Trusted AI Principles": {
            "source": "kpmg-agentic-ai-advantage_TLDR.md",
            "description": "Transparency, explainability, data privacy, compliance",
            "use_for": ["ai_policy", "data_governance"]
        }
    }


# Singleton instance for easy access
_loader_instance: Optional[KnowledgeLoader] = None


def get_knowledge_loader() -> KnowledgeLoader:
    """
    Get singleton knowledge loader instance.

    Returns:
        KnowledgeLoader instance
    """
    global _loader_instance
    if _loader_instance is None:
        _loader_instance = KnowledgeLoader()
    return _loader_instance
