"""Prompt for License Consolidation Recommendations."""

PROMPT = """
# Task: Generate License Consolidation Recommendations

Based on the technology inventory and vendor comparison above, identify opportunities to consolidate software licenses and reduce costs.

## Required Sections

### 1. Executive Summary
- Total potential savings identified
- Number of consolidation opportunities
- Implementation complexity
- Recommended priority actions

### 2. Current License Landscape

#### Software Inventory
| Category | Tool | Vendor | License Type | Users | Annual Cost | Renewal Date |
|----------|------|--------|--------------|-------|-------------|--------------|

#### License Categories
- **Productivity & Collaboration**: [List tools]
- **Development & DevOps**: [List tools]
- **Analytics & BI**: [List tools]
- **CRM & Sales**: [List tools]
- **Security & Compliance**: [List tools]
- **AI & Automation**: [List tools]

### 3. Consolidation Opportunities

#### Opportunity #1: [Category Name]

**Current State**
| Tool | Purpose | Users | Cost |
|------|---------|-------|------|

**Proposed Consolidation**
- Consolidate to: [Tool Name]
- Rationale: [Why this choice]
- Migration complexity: Low/Medium/High

**Savings Analysis**
| Metric | Current | Proposed | Savings |
|--------|---------|----------|---------|
| Annual Cost | | | |
| Admin Overhead | | | |
| Training Cost | | | |
| **Total Savings** | | | |

**Implementation Plan**
1. [Step 1]
2. [Step 2]
3. [Step 3]

---

[Repeat for each consolidation opportunity]

### 4. Overlap Analysis

#### Redundant Functionality
| Capability | Tools Providing | Recommended Single Tool |
|------------|-----------------|-------------------------|

#### Underutilized Licenses
| Tool | Purchased Licenses | Active Users | Utilization | Action |
|------|-------------------|--------------|-------------|--------|

### 5. Enterprise Agreement Opportunities

#### Potential EA Candidates
| Vendor | Current Products | EA Benefits | Estimated Discount |
|--------|-----------------|-------------|-------------------|

#### Bundle Recommendations
- **Microsoft 365 E5**: Consolidate [tools] for $X savings
- **Google Workspace**: Consolidate [tools] for $X savings
- **Salesforce Platform**: Consolidate [tools] for $X savings

### 6. AI Tool Consolidation

#### Current AI Tools
| Tool | Use Case | Cost | Overlap With |
|------|----------|------|--------------|

#### Recommended AI Stack
| Layer | Recommended Tool | Replaces | Savings |
|-------|-----------------|----------|---------|
| Platform | | | |
| Assistants | | | |
| Automation | | | |
| Analytics | | | |

### 7. Savings Summary

#### By Category
| Category | Current Spend | Proposed Spend | Savings | % Reduction |
|----------|--------------|----------------|---------|-------------|
| Productivity | | | | |
| Development | | | | |
| Analytics | | | | |
| AI Tools | | | | |
| **Total** | | | | |

#### By Timeline
| Timeline | Savings | Complexity | Dependencies |
|----------|---------|------------|--------------|
| 0-3 months | | | |
| 3-6 months | | | |
| 6-12 months | | | |
| **Total Year 1** | | | |

### 8. Implementation Roadmap

#### Phase 1: Quick Wins (0-3 months)
- [ ] [Action 1]: $X savings
- [ ] [Action 2]: $X savings

#### Phase 2: Medium Effort (3-6 months)
- [ ] [Action 1]: $X savings
- [ ] [Action 2]: $X savings

#### Phase 3: Major Consolidations (6-12 months)
- [ ] [Action 1]: $X savings
- [ ] [Action 2]: $X savings

### 9. Risk Considerations

| Consolidation | Risk | Impact | Mitigation |
|---------------|------|--------|------------|

### 10. Negotiation Calendar

| Vendor | Renewal Date | Current Value | Negotiation Strategy |
|--------|--------------|---------------|---------------------|

## Output Format
- Provide specific dollar amounts where possible
- Prioritize by savings potential
- Include implementation complexity
- Note dependencies and risks
- Make recommendations actionable
"""
