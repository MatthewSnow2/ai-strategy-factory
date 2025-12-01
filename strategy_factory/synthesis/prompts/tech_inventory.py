"""Prompt for Technology Inventory & Data Infrastructure Assessment."""

PROMPT = """
# Task: Generate Technology Inventory & Data Infrastructure Assessment

Based on the company research and context provided above, create a comprehensive technology inventory document.

## Required Sections

### 1. Executive Summary
- Brief overview of current technology landscape
- Key findings and critical gaps
- Readiness for AI adoption (high-level assessment)

### 2. Current Technology Stack

Create a table with the following columns:
| Category | Tool/Platform | Purpose | AI-Ready | Data Integration |
|----------|--------------|---------|----------|------------------|

Categories to include:
- Core Business Systems (ERP, CRM, etc.)
- Communication & Collaboration
- Data & Analytics
- Development & DevOps
- Security & Compliance
- Industry-Specific Tools

### 3. Data Infrastructure Assessment

#### Data Sources
List all identified data sources:
- Internal databases
- Third-party integrations
- Manual data entry points
- External data feeds

#### Data Quality Indicators
- Structured vs unstructured data ratio
- Data freshness and update frequency
- Known data quality issues
- Data governance maturity

#### Data Accessibility
- API availability
- Export capabilities
- Real-time access potential
- Security/privacy constraints

### 4. Integration Landscape

Create a diagram description of how systems connect:
- Primary integrations
- Data flow direction
- Integration methods (API, file transfer, manual)
- Integration gaps

### 5. AI Readiness Assessment

| Dimension | Current State | Gap | Priority |
|-----------|--------------|-----|----------|
| Data Quality | | | |
| Data Accessibility | | | |
| Compute Infrastructure | | | |
| Technical Skills | | | |
| Integration Capability | | | |

### 6. Recommendations

#### Immediate Actions (0-30 days)
- Quick data quality improvements
- Essential integrations to enable

#### Short-term Priorities (30-90 days)
- Infrastructure upgrades needed
- Tools to evaluate or adopt

#### Long-term Considerations (90+ days)
- Platform modernization
- Strategic technology investments

## Output Format
- Use markdown formatting
- Include tables where specified
- Be specific with tool names and versions where known
- Note assumptions clearly where information is limited
- Keep recommendations actionable and prioritized
"""
