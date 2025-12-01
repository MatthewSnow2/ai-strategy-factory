"""
Prompt templates for deliverable synthesis.

Each prompt module exports:
- SYSTEM_INSTRUCTION: System instruction for the model
- PROMPT_TEMPLATE: Main prompt template
- get_prompt(): Function to get the complete prompt
"""

from .tech_inventory import PROMPT as TECH_INVENTORY_PROMPT
from .pain_points import PROMPT as PAIN_POINTS_PROMPT
from .mermaid_diagrams import PROMPT as MERMAID_DIAGRAMS_PROMPT
from .maturity_assessment import PROMPT as MATURITY_ASSESSMENT_PROMPT
from .roadmap import PROMPT as ROADMAP_PROMPT
from .quick_wins import PROMPT as QUICK_WINS_PROMPT
from .vendor_comparison import PROMPT as VENDOR_COMPARISON_PROMPT
from .license_consolidation import PROMPT as LICENSE_CONSOLIDATION_PROMPT
from .roi_calculator import PROMPT as ROI_CALCULATOR_PROMPT
from .ai_policy import PROMPT as AI_POLICY_PROMPT
from .data_governance import PROMPT as DATA_GOVERNANCE_PROMPT
from .prompt_library import PROMPT as PROMPT_LIBRARY_PROMPT
from .glossary import PROMPT as GLOSSARY_PROMPT
from .use_case_library import PROMPT as USE_CASE_LIBRARY_PROMPT
from .change_management import PROMPT as CHANGE_MANAGEMENT_PROMPT

# Map deliverable IDs to prompts
PROMPTS = {
    "01_tech_inventory": TECH_INVENTORY_PROMPT,
    "02_pain_points": PAIN_POINTS_PROMPT,
    "03_mermaid_diagrams": MERMAID_DIAGRAMS_PROMPT,
    "04_maturity_assessment": MATURITY_ASSESSMENT_PROMPT,
    "05_roadmap": ROADMAP_PROMPT,
    "06_quick_wins": QUICK_WINS_PROMPT,
    "07_vendor_comparison": VENDOR_COMPARISON_PROMPT,
    "08_license_consolidation": LICENSE_CONSOLIDATION_PROMPT,
    "09_roi_calculator": ROI_CALCULATOR_PROMPT,
    "10_ai_policy": AI_POLICY_PROMPT,
    "11_data_governance": DATA_GOVERNANCE_PROMPT,
    "12_prompt_library": PROMPT_LIBRARY_PROMPT,
    "13_glossary": GLOSSARY_PROMPT,
    "14_use_case_library": USE_CASE_LIBRARY_PROMPT,
    "15_change_management": CHANGE_MANAGEMENT_PROMPT,
}


def get_prompt(deliverable_id: str) -> str:
    """Get the prompt template for a deliverable."""
    return PROMPTS.get(deliverable_id, "")
