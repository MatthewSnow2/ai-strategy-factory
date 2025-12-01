"""Prompt for Vendor Comparison & Build vs Buy Framework."""

PROMPT = """
# Task: Generate Vendor Comparison & Build vs Buy Framework

Based on the technology inventory and use cases identified above, create a comprehensive vendor comparison and build vs buy analysis.

## Required Sections

### 1. Executive Summary
- Key vendor recommendations by category
- Build vs buy recommendations
- Estimated total cost of ownership
- Critical decision factors

### 2. AI Platform Comparison

#### Enterprise AI Platforms
| Vendor | Strengths | Weaknesses | Best For | Pricing Model |
|--------|-----------|------------|----------|---------------|
| Microsoft Azure AI | | | | |
| Google Cloud AI | | | | |
| AWS AI Services | | | | |
| OpenAI/ChatGPT Enterprise | | | | |
| Anthropic Claude | | | | |

#### Category-Specific Tools

**Document Processing**
| Vendor | Features | Integration | Pricing | Fit Score |
|--------|----------|-------------|---------|-----------|

**Conversational AI**
| Vendor | Features | Integration | Pricing | Fit Score |
|--------|----------|-------------|---------|-----------|

**Analytics & BI**
| Vendor | Features | Integration | Pricing | Fit Score |
|--------|----------|-------------|---------|-----------|

**Process Automation**
| Vendor | Features | Integration | Pricing | Fit Score |
|--------|----------|-------------|---------|-----------|

### 3. Build vs Buy Framework

#### Decision Matrix
For each use case, evaluate:

| Factor | Weight | Build Score | Buy Score |
|--------|--------|-------------|-----------|
| Time to Value | 25% | | |
| Total Cost (3 yr) | 20% | | |
| Customization Need | 15% | | |
| Strategic Value | 15% | | |
| Internal Capability | 10% | | |
| Maintenance Burden | 10% | | |
| Risk Level | 5% | | |
| **Weighted Total** | 100% | | |

#### Use Case Recommendations

| Use Case | Recommendation | Rationale | Vendor (if Buy) |
|----------|---------------|-----------|-----------------|

### 4. Vendor Evaluation Criteria

#### Must-Have Requirements
- [ ] SOC 2 compliance
- [ ] Data residency options
- [ ] API availability
- [ ] SSO integration
- [ ] Audit logging

#### Nice-to-Have Requirements
- [ ] Custom model training
- [ ] On-premise option
- [ ] White-label capability
- [ ] 24/7 support

### 5. Cost Analysis

#### Build Scenario (Internal Development)
| Cost Category | Year 1 | Year 2 | Year 3 | Total |
|---------------|--------|--------|--------|-------|
| Development | | | | |
| Infrastructure | | | | |
| Maintenance | | | | |
| Training | | | | |
| **Total** | | | | |

#### Buy Scenario (Vendor Solution)
| Cost Category | Year 1 | Year 2 | Year 3 | Total |
|---------------|--------|--------|--------|-------|
| Licensing | | | | |
| Implementation | | | | |
| Integration | | | | |
| Training | | | | |
| **Total** | | | | |

### 6. Vendor Shortlist

#### Recommended Primary Vendors
1. **[Vendor Name]** - [Category]
   - Why: [Rationale]
   - Fit score: X/10
   - Estimated cost: $X/year

2. **[Vendor Name]** - [Category]
   - Why: [Rationale]
   - Fit score: X/10
   - Estimated cost: $X/year

#### Recommended for Evaluation
- [Vendor]: Schedule demo for [use case]
- [Vendor]: POC for [use case]

### 7. Integration Considerations

#### Current Stack Compatibility
| Vendor | CRM Integration | ERP Integration | Data Warehouse | Auth/SSO |
|--------|-----------------|-----------------|----------------|----------|

#### API & Extensibility
| Vendor | REST API | Webhooks | SDK | Custom Models |
|--------|----------|----------|-----|---------------|

### 8. Risk Assessment

| Vendor | Vendor Risk | Lock-in Risk | Security Risk | Mitigation |
|--------|-------------|--------------|---------------|------------|

### 9. Negotiation Guidance

#### Leverage Points
- Multi-year commitment discounts
- Volume pricing tiers
- Bundling opportunities
- Competitive alternatives

#### Key Terms to Negotiate
- Data portability clauses
- SLA guarantees
- Price protection
- Exit provisions

### 10. Recommendation Summary

| Category | Recommendation | Vendor | Action |
|----------|---------------|--------|--------|
| Platform | Build/Buy | [Name] | [Next step] |
| Document AI | Build/Buy | [Name] | [Next step] |
| Conversational AI | Build/Buy | [Name] | [Next step] |

## Output Format
- Use comparison tables extensively
- Include specific vendor names
- Provide cost estimates where possible
- Make recommendations clear and actionable
- Note assumptions in cost calculations
"""
