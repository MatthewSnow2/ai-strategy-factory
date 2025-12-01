"""Prompt for AI Maturity Model & Readiness Assessment."""

PROMPT = """
# Task: Generate AI Maturity Model & Readiness Assessment

Based on the research and context provided above, create a comprehensive AI maturity assessment using the BCG AI Maturity Curve framework and other industry standards.

## Required Sections

### 1. Executive Summary
- Current maturity level (1-5 scale)
- Key strengths and gaps
- Recommended focus areas
- Estimated timeline to next maturity level

### 2. AI Maturity Assessment

#### BCG AI Maturity Curve Position

Assess the company against these stages:
1. **Passive** - No AI initiatives, traditional processes
2. **Aware** - Exploring AI, initial pilots
3. **Active** - Multiple AI projects, some in production
4. **Operational** - AI integrated into core processes
5. **Transformational** - AI-native organization, competitive advantage

**Current Assessment:** [Stage X]

Provide evidence from research supporting this assessment.

### 3. Dimension-by-Dimension Analysis

Rate each dimension on a 1-5 scale:

| Dimension | Score | Evidence | Gap Analysis |
|-----------|-------|----------|--------------|
| Strategy & Vision | | | |
| Data & Infrastructure | | | |
| Technology & Tools | | | |
| Talent & Skills | | | |
| Governance & Ethics | | | |
| Culture & Change | | | |
| Use Cases & Value | | | |

#### Detailed Dimension Analysis

For each dimension, provide:

##### Strategy & Vision (X/5)
- Current state observations
- Strengths identified
- Gaps and weaknesses
- Recommendations

##### Data & Infrastructure (X/5)
- Data availability and quality
- Infrastructure readiness
- Integration capabilities
- Recommendations

##### Technology & Tools (X/5)
- Current AI/ML tools
- Platform maturity
- Technical debt considerations
- Recommendations

##### Talent & Skills (X/5)
- AI expertise in-house
- Training programs
- External partnerships
- Recommendations

##### Governance & Ethics (X/5)
- AI policies in place
- Risk management approach
- Compliance considerations
- Recommendations

##### Culture & Change (X/5)
- Change readiness
- Innovation culture
- Leadership support
- Recommendations

##### Use Cases & Value (X/5)
- Current AI use cases
- Value realization
- Scaling approach
- Recommendations

### 4. Maturity Radar Chart

Provide data for a radar chart visualization:
```
Strategy & Vision: X
Data & Infrastructure: X
Technology & Tools: X
Talent & Skills: X
Governance & Ethics: X
Culture & Change: X
Use Cases & Value: X
```

### 5. Peer Comparison

Compare to industry benchmarks:
| Dimension | Company Score | Industry Average | Gap |
|-----------|--------------|------------------|-----|

### 6. Readiness Assessment

#### Immediate Readiness (Ready to Start)
List AI initiatives the company could begin immediately.

#### Near-term Readiness (3-6 months)
List AI initiatives requiring some preparation.

#### Long-term Readiness (6-12 months)
List AI initiatives requiring significant investment.

### 7. Maturity Improvement Roadmap

#### To reach next maturity level:
- Key initiatives required
- Investment areas
- Timeline estimate
- Critical success factors

## Output Format
- Use markdown tables as specified
- Include numeric scores for quantitative assessment
- Provide specific evidence from research
- Be realistic about gaps and challenges
- Make recommendations actionable
"""
