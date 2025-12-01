"""Prompt for ROI Calculator & Cost Analysis."""

PROMPT = """
# Task: Generate ROI Calculator & Cost Analysis

Based on the quick wins and use case library above, create a comprehensive ROI analysis using the Google Cloud ROI framework and industry benchmarks.

## Required Sections

### 1. Executive Summary
- Total projected ROI (Year 1)
- Payback period
- Net Present Value (3-year)
- Key value drivers
- Investment requirements

### 2. ROI Framework Overview

Using the value creation framework:
- **Efficiency Gains**: Time and cost savings
- **Revenue Enhancement**: New revenue or increased sales
- **Risk Reduction**: Avoided costs and compliance
- **Strategic Value**: Competitive advantage and innovation

### 3. Investment Requirements

#### Technology Costs
| Category | Year 1 | Year 2 | Year 3 | Total |
|----------|--------|--------|--------|-------|
| AI Platform Licenses | | | | |
| Infrastructure | | | | |
| Integration | | | | |
| Security/Compliance | | | | |
| **Subtotal** | | | | |

#### Implementation Costs
| Category | Year 1 | Year 2 | Year 3 | Total |
|----------|--------|--------|--------|-------|
| Consulting/Professional Services | | | | |
| Internal Team Time | | | | |
| Training & Change Management | | | | |
| Contingency (15%) | | | | |
| **Subtotal** | | | | |

#### Ongoing Costs
| Category | Year 1 | Year 2 | Year 3 | Total |
|----------|--------|--------|--------|-------|
| Maintenance & Support | | | | |
| Model Updates/Retraining | | | | |
| Additional Compute | | | | |
| **Subtotal** | | | | |

**Total Investment**: $[X] over 3 years

### 4. Value Creation Analysis

#### Efficiency Gains
| Initiative | Metric | Current | Improved | Savings/Year |
|------------|--------|---------|----------|--------------|
| [Use Case 1] | Hours saved | | | |
| [Use Case 2] | Cost reduction | | | |
| [Use Case 3] | Error reduction | | | |

**Total Efficiency Gains**: $[X]/year

#### Revenue Enhancement
| Initiative | Metric | Current | Improved | Revenue/Year |
|------------|--------|---------|----------|--------------|
| [Use Case 1] | Conversion rate | | | |
| [Use Case 2] | Deal velocity | | | |
| [Use Case 3] | Customer retention | | | |

**Total Revenue Enhancement**: $[X]/year

#### Risk Reduction
| Initiative | Risk Type | Probability | Impact | Avoided Cost |
|------------|-----------|-------------|--------|--------------|
| [Use Case 1] | Compliance | | | |
| [Use Case 2] | Security | | | |
| [Use Case 3] | Operational | | | |

**Total Risk Reduction**: $[X]/year

### 5. ROI Calculations

#### Simple ROI
```
Total Benefits (Year 1): $[X]
Total Investment (Year 1): $[Y]
ROI = (Benefits - Investment) / Investment × 100
ROI = [Z]%
```

#### Payback Period
```
Total Investment: $[X]
Monthly Benefits: $[Y]
Payback Period: [Z] months
```

#### Net Present Value (3-Year)
| Year | Benefits | Costs | Net | Discount Factor | NPV |
|------|----------|-------|-----|-----------------|-----|
| 0 | | | | 1.00 | |
| 1 | | | | 0.91 | |
| 2 | | | | 0.83 | |
| 3 | | | | 0.75 | |
| **Total** | | | | | |

(Using 10% discount rate)

### 6. By Initiative Analysis

| Initiative | Investment | Year 1 Value | ROI | Payback | Priority |
|------------|------------|--------------|-----|---------|----------|
| Quick Win 1 | | | | | |
| Quick Win 2 | | | | | |
| Major Project 1 | | | | | |
| **Total** | | | | | |

### 7. Sensitivity Analysis

#### Best Case Scenario
- Assumptions: [List]
- ROI: [X]%
- NPV: $[X]

#### Base Case Scenario
- Assumptions: [List]
- ROI: [X]%
- NPV: $[X]

#### Conservative Scenario
- Assumptions: [List]
- ROI: [X]%
- NPV: $[X]

### 8. Industry Benchmarks

| Metric | Company Projection | Industry Average | Top Quartile |
|--------|-------------------|------------------|--------------|
| AI ROI | | | |
| Payback Period | | | |
| Productivity Gain | | | |

### 9. Value Realization Timeline

| Milestone | Timeline | Value Released | Cumulative |
|-----------|----------|----------------|------------|
| First Quick Win | Month 2 | | |
| Full Quick Wins | Month 4 | | |
| Scale Phase | Month 8 | | |
| Full Value | Month 12 | | |

### 10. Recommendations

#### Investment Priorities
1. [Highest ROI initiative]
2. [Second highest]
3. [Third highest]

#### Value Capture Actions
- Track metrics from day 1
- Establish baseline measurements
- Report progress monthly
- Adjust based on actuals

## Output Format
- Use specific dollar amounts
- Show calculation methodology
- Include sensitivity ranges
- Reference industry benchmarks
- Make assumptions explicit
"""
