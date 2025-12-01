"""Prompt for AI Acceptable Use Policy Template."""

PROMPT = """
# Task: Generate AI Acceptable Use Policy Template

Based on the company context, industry regulations, and governance requirements above, create a comprehensive AI Acceptable Use Policy.

## Required Sections

### 1. Policy Overview

#### Purpose
This policy establishes guidelines for the responsible use of Artificial Intelligence (AI) tools and technologies at {company_name}.

#### Scope
- All employees, contractors, and third parties
- All AI tools (internal and external)
- All use cases involving AI

#### Effective Date
{current_date}

### 2. Definitions

| Term | Definition |
|------|------------|
| Artificial Intelligence (AI) | |
| Generative AI | |
| Machine Learning Model | |
| AI-Generated Content | |
| Prompt | |
| Training Data | |

### 3. Approved AI Tools

#### Sanctioned Tools
| Tool | Approved Use Cases | Restrictions | Data Classification |
|------|-------------------|--------------|---------------------|
| [Tool 1] | | | |
| [Tool 2] | | | |

#### Evaluation Process for New Tools
1. Submit request to [team/role]
2. Security review
3. Privacy impact assessment
4. Approval process

### 4. Acceptable Use Guidelines

#### Permitted Uses
- [List permitted use cases]
- [Research and analysis]
- [Content drafting]
- [Code assistance]
- [Data analysis]

#### Prohibited Uses
- [ ] Processing customer PII without approval
- [ ] Generating content for legal/compliance documents without review
- [ ] Training models on proprietary company data
- [ ] Sharing confidential information with external AI tools
- [ ] Automated decision-making affecting individuals
- [ ] [Industry-specific prohibitions]

### 5. Data Classification & AI

#### Data Handling by Classification

| Classification | Can Use with AI? | Requirements |
|---------------|------------------|--------------|
| Public | Yes | None |
| Internal | Yes | Approved tools only |
| Confidential | Limited | Approval required |
| Restricted | No | Prohibited |

#### Sensitive Data Types
Never input into AI tools without explicit approval:
- Customer personal information
- Employee personal information
- Financial data
- Health information (if applicable)
- Trade secrets
- Legal privileged information

### 6. Content Review Requirements

#### AI-Generated Content Review Matrix

| Content Type | Review Required | Approver |
|--------------|-----------------|----------|
| External communications | Yes | [Role] |
| Customer-facing materials | Yes | [Role] |
| Internal documentation | No | Self |
| Code | Yes | Peer review |
| Legal/Compliance | Yes | Legal team |

#### Attribution Requirements
- Disclose AI assistance when required by [context]
- Maintain records of AI-generated content

### 7. Security Requirements

#### Authentication
- Use company SSO when available
- Never share credentials
- Enable MFA where supported

#### Data Protection
- Use approved data transfer methods
- Encrypt sensitive communications
- Log AI tool usage

#### Incident Reporting
Report immediately:
- Data exposure incidents
- Unexpected AI behavior
- Policy violations

Contact: [Security team contact]

### 8. Compliance Considerations

#### Regulatory Requirements
Based on industry context:
- [Regulation 1]: [Requirements]
- [Regulation 2]: [Requirements]
- [AI-specific regulations]: [Requirements]

#### Audit & Monitoring
- AI usage may be monitored
- Logs retained for [X] months
- Annual policy compliance review

### 9. Roles & Responsibilities

| Role | Responsibilities |
|------|-----------------|
| All Employees | Follow policy, report issues |
| Managers | Ensure team compliance |
| IT/Security | Tool evaluation, monitoring |
| Legal/Compliance | Policy updates, guidance |
| AI Committee | Strategy, governance |

### 10. Training Requirements

| Role | Training | Frequency |
|------|----------|-----------|
| All employees | AI basics & policy | Annual |
| Power users | Advanced AI tools | Bi-annual |
| Developers | AI development guidelines | As needed |

### 11. Policy Violations

#### Consequences
- First violation: Coaching
- Second violation: Written warning
- Severe violation: Disciplinary action

#### Reporting Violations
- Anonymous hotline: [Contact]
- Direct report: [Contact]

### 12. Policy Governance

#### Review Cycle
- Quarterly review for updates
- Annual comprehensive review

#### Change Management
- Changes communicated via [channel]
- 30-day notice for major changes

#### Questions & Exceptions
Contact: [AI Governance Team contact]

---

## Acknowledgment

I have read and understand the AI Acceptable Use Policy. I agree to comply with its terms.

Employee Name: _________________
Employee Signature: _________________
Date: _________________

## Output Format
- Use professional policy language
- Include specific examples where helpful
- Customize based on industry context
- Make requirements clear and actionable
- Include acknowledgment section
"""
