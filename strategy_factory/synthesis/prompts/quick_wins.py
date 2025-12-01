"""Prompt for Quick Wins List."""

PROMPT = """
# Task: Generate Quick Wins List

Based on the use case library and maturity assessment provided above, identify and prioritize AI quick wins that can be implemented within 30-60 days.

## Required Sections

### 1. Executive Summary
- Total quick wins identified
- Estimated combined value
- Resource requirements summary
- Recommended starting point

### 2. Quick Win Selection Criteria

Explain the criteria used:
- Implementation time: < 60 days
- Investment: < $50K (or internal resources)
- Risk level: Low
- Value potential: Demonstrable ROI
- Prerequisites: Minimal

### 3. Top 10 Quick Wins

For each quick win, provide:

---

#### Quick Win #1: [Name]

**Overview**
| Attribute | Value |
|-----------|-------|
| Department | |
| Time to Implement | |
| Estimated Investment | |
| Expected ROI | |
| Risk Level | Low/Medium |
| Prerequisites | |

**Description**
[2-3 sentence description of the initiative]

**Current State**
- How is this done today?
- Pain points addressed

**Proposed Solution**
- AI/automation approach
- Tool/platform recommendation
- Implementation approach

**Implementation Steps**
1. Week 1: [Activity]
2. Week 2: [Activity]
3. Week 3-4: [Activity]
4. Week 5-6: [Launch & optimize]

**Success Metrics**
- Primary KPI: [Metric and target]
- Secondary KPIs: [List]

**Resources Required**
- Internal: [Roles/time]
- External: [Tools/vendors]
- Budget: [$X]

---

[Repeat for Quick Wins #2-10]

### 4. Quick Win Comparison Matrix

| # | Quick Win | Dept | Time | Investment | ROI | Risk | Priority |
|---|-----------|------|------|------------|-----|------|----------|
| 1 | | | | | | | |
| 2 | | | | | | | |
[...]

### 5. Implementation Sequence

Recommended order of implementation:

```
Month 1: Quick Wins 1, 2, 3
Month 2: Quick Wins 4, 5, 6
Month 3: Quick Wins 7, 8, 9, 10
```

Rationale for sequencing:
- Dependencies between wins
- Resource optimization
- Learning and momentum building

### 6. Resource Pooling Opportunities

Identify where quick wins can share:
- Tools and platforms
- Training and change management
- Data and integrations
- Team resources

### 7. Risk Mitigation

Common risks and mitigation:
| Risk | Affected Quick Wins | Mitigation |
|------|---------------------|------------|

### 8. Success Tracking Dashboard

Proposed metrics dashboard:
| Quick Win | Status | Progress | Value Realized |
|-----------|--------|----------|----------------|

### 9. Escalation Path

If a quick win encounters obstacles:
1. Week 1-2: Project team resolves
2. Week 3: Escalate to sponsor
3. Week 4+: Re-evaluate or pivot

### 10. Next Wave Preview

Quick wins that didn't make the cut but should be considered next:
- [Initiative name]: Why not now, what's needed

## Output Format
- Provide detailed analysis for each quick win
- Use consistent formatting across all entries
- Include specific numbers for ROI estimates
- Make implementation steps actionable
- Prioritize based on value and feasibility
"""
