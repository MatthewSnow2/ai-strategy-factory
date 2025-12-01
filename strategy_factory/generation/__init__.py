"""
Generation module - Document creation (Markdown, PPTX, DOCX, Mermaid images).

This module handles the final generation phase, converting synthesized content
into polished deliverables in various formats.
"""

from .markdown_generator import MarkdownGenerator, save_markdown_deliverables
from .mermaid_renderer import MermaidRenderer, render_mermaid_diagrams
from .pptx_generator import PowerPointGenerator, generate_executive_deck, generate_full_findings_deck
from .docx_generator import DocxGenerator, generate_strategy_report, generate_statement_of_work
from .orchestrator import GenerationOrchestrator, run_generation

__all__ = [
    # Markdown
    "MarkdownGenerator",
    "save_markdown_deliverables",
    # Mermaid
    "MermaidRenderer",
    "render_mermaid_diagrams",
    # PowerPoint
    "PowerPointGenerator",
    "generate_executive_deck",
    "generate_full_findings_deck",
    # Word
    "DocxGenerator",
    "generate_strategy_report",
    "generate_statement_of_work",
    # Orchestrator
    "GenerationOrchestrator",
    "run_generation",
]
