"""Prompt for Department-Specific Use Case Library."""

PROMPT = """
# Task: Generate Department-Specific Use Case Library

Based on the pain point analysis, technology landscape, and industry context above, create a comprehensive library of AI use cases organized by department.

## Required Sections

### 1. Executive Summary
- Total use cases identified
- High-priority opportunities
- Estimated total value potential
- Recommended starting points

### 2. Use Case Classification Framework

#### Priority Matrix
Use cases are classified by:
- **Impact**: Business value potential (High/Medium/Low)
- **Feasibility**: Implementation complexity (Easy/Medium/Hard)
- **Readiness**: Data and infrastructure readiness (Ready/Some Work/Major Work)

#### KPMG TACO Framework for Agentic Use Cases
- **T**ask Automation: Routine, repetitive tasks
- **A**nalysis: Data interpretation and insights
- **C**reation: Content and asset generation
- **O**rchestration: Multi-step workflow coordination

---

### 3. Sales & Marketing Use Cases

#### Use Case SM-001: Lead Scoring & Prioritization

| Attribute | Value |
|-----------|-------|
| Category | Analysis |
| Impact | High |
| Feasibility | Easy |
| Time to Value | 30-60 days |

**Description**
AI-powered lead scoring that analyzes prospect data, behavior, and engagement to prioritize sales efforts.

**Current State**
- Manual lead assessment
- Inconsistent criteria
- Missed opportunities

**AI Solution**
- ML model trained on historical conversions
- Real-time scoring based on engagement signals
- Automated routing to appropriate sales reps

**Value Potential**
- 20-30% increase in conversion rates
- 15% reduction in sales cycle time
- Better resource allocation

**Prerequisites**
- CRM data history
- Defined scoring criteria
- Sales team buy-in

**Recommended Tools**
- Salesforce Einstein
- HubSpot AI
- Custom ML model

---

#### Use Case SM-002: Content Personalization
[Similar structure]

#### Use Case SM-003: Campaign Performance Optimization
[Similar structure]

#### Use Case SM-004: Competitive Intelligence Automation
[Similar structure]

---

### 4. Customer Service Use Cases

#### Use Case CS-001: Intelligent Ticket Routing

| Attribute | Value |
|-----------|-------|
| Category | Orchestration |
| Impact | High |
| Feasibility | Medium |
| Time to Value | 60-90 days |

**Description**
AI that analyzes incoming tickets, classifies issues, assesses urgency, and routes to the best-suited agent.

[Continue with full details...]

#### Use Case CS-002: AI-Powered Chat Support
[Similar structure]

#### Use Case CS-003: Sentiment Analysis & Escalation
[Similar structure]

#### Use Case CS-004: Knowledge Base Auto-Updates
[Similar structure]

---

### 5. Operations Use Cases

#### Use Case OP-001: Process Documentation Generation

| Attribute | Value |
|-----------|-------|
| Category | Creation |
| Impact | Medium |
| Feasibility | Easy |
| Time to Value | 30 days |

[Continue with full details...]

#### Use Case OP-002: Quality Control Automation
[Similar structure]

#### Use Case OP-003: Inventory Optimization
[Similar structure]

#### Use Case OP-004: Vendor Performance Analysis
[Similar structure]

---

### 6. Finance Use Cases

#### Use Case FN-001: Invoice Processing Automation

| Attribute | Value |
|-----------|-------|
| Category | Task Automation |
| Impact | High |
| Feasibility | Easy |
| Time to Value | 45 days |

[Continue with full details...]

#### Use Case FN-002: Financial Reporting Automation
[Similar structure]

#### Use Case FN-003: Anomaly Detection in Transactions
[Similar structure]

#### Use Case FN-004: Cash Flow Forecasting
[Similar structure]

---

### 7. Human Resources Use Cases

#### Use Case HR-001: Resume Screening & Ranking

| Attribute | Value |
|-----------|-------|
| Category | Analysis |
| Impact | High |
| Feasibility | Easy |
| Time to Value | 30 days |

[Continue with full details...]

#### Use Case HR-002: Employee Onboarding Assistant
[Similar structure]

#### Use Case HR-003: Performance Review Analysis
[Similar structure]

#### Use Case HR-004: Learning Path Personalization
[Similar structure]

---

### 8. IT & Engineering Use Cases

#### Use Case IT-001: Code Review Assistance

| Attribute | Value |
|-----------|-------|
| Category | Analysis |
| Impact | Medium |
| Feasibility | Easy |
| Time to Value | 14 days |

[Continue with full details...]

#### Use Case IT-002: Incident Response Automation
[Similar structure]

#### Use Case IT-003: Documentation Generation
[Similar structure]

#### Use Case IT-004: Security Threat Detection
[Similar structure]

---

### 9. Cross-Functional Use Cases

#### Use Case XF-001: Meeting Summarization

| Attribute | Value |
|-----------|-------|
| Category | Creation |
| Impact | Medium |
| Feasibility | Easy |
| Time to Value | 7 days |

[Continue with full details...]

#### Use Case XF-002: Email Drafting Assistant
[Similar structure]

#### Use Case XF-003: Research & Analysis Assistant
[Similar structure]

---

### 10. Use Case Summary Matrix

| ID | Use Case | Dept | Impact | Feasibility | Priority |
|----|----------|------|--------|-------------|----------|
| SM-001 | Lead Scoring | Sales | High | Easy | 1 |
| CS-001 | Ticket Routing | Service | High | Medium | 2 |
| FN-001 | Invoice Processing | Finance | High | Easy | 1 |
[Continue for all use cases...]

### 11. Implementation Recommendations

#### Quick Start (Month 1)
Based on impact and feasibility:
1. [Use Case ID]: [Name]
2. [Use Case ID]: [Name]
3. [Use Case ID]: [Name]

#### Phase 2 (Months 2-3)
[List use cases]

#### Phase 3 (Months 4-6)
[List use cases]

### 12. Value Summary

| Department | Use Cases | Est. Annual Value | Investment |
|------------|-----------|-------------------|------------|
| Sales & Marketing | X | $Y | $Z |
| Customer Service | X | $Y | $Z |
| Operations | X | $Y | $Z |
| Finance | X | $Y | $Z |
| HR | X | $Y | $Z |
| IT | X | $Y | $Z |
| **Total** | | | |

## Output Format
- Detailed analysis for each use case
- Consistent structure across all entries
- Prioritization based on value and feasibility
- Specific tool recommendations
- Clear prerequisites and dependencies
"""
