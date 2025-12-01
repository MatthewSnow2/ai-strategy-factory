"""Prompt for Pain Point Matrix by Department."""

PROMPT = """
# Task: Generate Pain Point Matrix by Department

Based on the company research and industry context provided above, create a comprehensive pain point analysis organized by department.

## Required Sections

### 1. Executive Summary
- Overview of most critical pain points across the organization
- Common themes identified
- Highest-impact opportunities for AI intervention

### 2. Pain Point Matrix by Department

For each relevant department, create a detailed analysis:

#### Sales & Marketing
| Pain Point | Impact (H/M/L) | Frequency | Current Workaround | AI Solution Potential |
|------------|----------------|-----------|-------------------|----------------------|

Common pain points to consider:
- Lead qualification and scoring
- Content creation and personalization
- Campaign performance analysis
- Customer segmentation
- Competitive intelligence gathering

#### Operations
| Pain Point | Impact (H/M/L) | Frequency | Current Workaround | AI Solution Potential |
|------------|----------------|-----------|-------------------|----------------------|

Common pain points:
- Process bottlenecks
- Quality control issues
- Capacity planning
- Vendor management
- Documentation and SOPs

#### Finance & Accounting
| Pain Point | Impact (H/M/L) | Frequency | Current Workaround | AI Solution Potential |
|------------|----------------|-----------|-------------------|----------------------|

Common pain points:
- Manual data entry
- Report generation
- Expense management
- Forecasting accuracy
- Compliance documentation

#### Human Resources
| Pain Point | Impact (H/M/L) | Frequency | Current Workaround | AI Solution Potential |
|------------|----------------|-----------|-------------------|----------------------|

Common pain points:
- Resume screening
- Employee onboarding
- Performance reviews
- Training program management
- Policy questions and support

#### Customer Service
| Pain Point | Impact (H/M/L) | Frequency | Current Workaround | AI Solution Potential |
|------------|----------------|-----------|-------------------|----------------------|

Common pain points:
- Response time
- Ticket routing
- Knowledge base maintenance
- Customer sentiment tracking
- Escalation management

#### IT & Engineering
| Pain Point | Impact (H/M/L) | Frequency | Current Workaround | AI Solution Potential |
|------------|----------------|-----------|-------------------|----------------------|

Common pain points:
- Code review bottlenecks
- Documentation gaps
- Incident response
- Technical debt management
- Security monitoring

### 3. Cross-Functional Pain Points

Identify pain points that span multiple departments:
- Communication silos
- Data accessibility issues
- Approval workflow delays
- Reporting inconsistencies

### 4. Prioritization Matrix

Create a 2x2 matrix visualization description:
- X-axis: Effort to solve (Low to High)
- Y-axis: Business Impact (Low to High)

Categorize pain points into:
- **Quick Wins** (High Impact, Low Effort)
- **Major Projects** (High Impact, High Effort)
- **Fill-ins** (Low Impact, Low Effort)
- **Thankless Tasks** (Low Impact, High Effort)

### 5. AI Intervention Opportunities

For each high-priority pain point, suggest:
- Specific AI/ML solution type
- Expected benefit
- Implementation complexity
- Prerequisites needed

## Output Format
- Use markdown tables as specified
- Include impact ratings (High/Medium/Low)
- Be specific to the industry context
- Prioritize based on research findings
- Note assumptions where information is limited
"""
