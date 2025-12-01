"""Prompt for Prompt Library Starter Kit."""

PROMPT = """
# Task: Generate Prompt Library Starter Kit

Based on the use case library and department analysis above, create a comprehensive prompt library for common AI tasks.

## Required Sections

### 1. Introduction

#### Purpose
This prompt library provides ready-to-use prompts for common tasks at {company_name}, optimized for [approved AI tools].

#### How to Use
1. Find the relevant category
2. Copy the prompt template
3. Replace [bracketed placeholders] with your specifics
4. Review and refine the output

#### Best Practices
- Be specific with context
- Include examples when helpful
- Iterate on outputs
- Always review AI-generated content

### 2. Sales & Marketing Prompts

#### Lead Qualification
```
Analyze this lead information and provide a qualification score:

Company: [Company Name]
Industry: [Industry]
Size: [Employee Count]
Budget: [If Known]
Timeline: [If Known]
Pain Points: [Known Challenges]

Provide:
1. Qualification score (1-10)
2. Key buying signals
3. Potential objections
4. Recommended next steps
5. Suggested talk track
```

#### Email Personalization
```
Write a personalized outreach email for:

Prospect: [Name, Title]
Company: [Company]
Industry: [Industry]
Context: [Recent news, shared connection, or trigger event]
Our Value Prop: [Relevant value proposition]

Requirements:
- Professional but conversational tone
- Under 150 words
- Clear call to action
- Reference the specific context
```

#### Competitive Analysis
```
Analyze our competitor [Competitor Name] for the [Product/Service] market:

Information available:
[Paste any research, website content, or notes]

Provide:
1. Product/service comparison
2. Pricing analysis (if available)
3. Strengths and weaknesses
4. Common objections when competing
5. Winning strategies against them
```

### 3. Customer Service Prompts

#### Response Generation
```
Generate a response to this customer inquiry:

Customer Message:
[Paste customer message]

Context:
- Product/Service: [What they're asking about]
- Customer History: [Any relevant history]
- Sentiment: [Frustrated/Neutral/Happy]

Requirements:
- Professional and empathetic tone
- Address all concerns
- Provide clear next steps
- [Company] brand voice
```

#### Issue Escalation Summary
```
Summarize this customer issue for escalation:

Customer: [Name/Account]
Issue Timeline:
[Paste conversation or notes]

Provide:
1. Issue summary (2-3 sentences)
2. Customer impact
3. Steps already taken
4. Recommended resolution
5. Urgency level (Low/Medium/High/Critical)
```

### 4. Operations Prompts

#### Process Documentation
```
Create a standard operating procedure for:

Process: [Process Name]
Purpose: [Why this process exists]
Current Steps:
[List current steps or describe the process]

Generate:
1. Formatted SOP with numbered steps
2. Required inputs
3. Expected outputs
4. Common exceptions and handling
5. Quality checkpoints
```

#### Meeting Summary
```
Summarize this meeting transcript:

Meeting: [Name/Purpose]
Attendees: [List]
Transcript:
[Paste transcript or notes]

Provide:
1. Executive summary (3-5 sentences)
2. Key decisions made
3. Action items with owners
4. Open questions
5. Next steps
```

### 5. Finance Prompts

#### Report Narrative
```
Write a narrative summary for this financial data:

Report Type: [Monthly P&L / Quarterly Review / etc.]
Period: [Date Range]
Key Metrics:
[Paste key metrics and figures]

Generate:
1. Executive summary
2. Highlight positive trends
3. Areas of concern
4. Comparison to previous period
5. Recommended focus areas
```

#### Expense Analysis
```
Analyze this expense data and identify optimization opportunities:

Data:
[Paste expense summary or categories]

Provide:
1. Top expense categories
2. Month-over-month trends
3. Anomalies or outliers
4. Consolidation opportunities
5. Recommended actions
```

### 6. HR Prompts

#### Job Description Enhancement
```
Improve this job description for better candidate attraction:

Current JD:
[Paste job description]

Requirements:
- Modern, inclusive language
- Clear responsibilities
- Compelling company pitch
- Realistic requirements vs nice-to-haves
- SEO-optimized for job boards
```

#### Interview Questions
```
Generate interview questions for:

Role: [Position Title]
Level: [Entry/Mid/Senior/Executive]
Key Skills: [Top 3-5 required skills]
Company Values: [Key values to assess]

Provide:
1. 5 behavioral questions
2. 3 technical/skill questions
3. 2 culture fit questions
4. Sample follow-up probes
5. Red flags to watch for
```

### 7. Engineering/IT Prompts

#### Code Review
```
Review this code for best practices:

Language: [Programming Language]
Purpose: [What the code does]
Code:
[Paste code]

Assess:
1. Code quality and readability
2. Potential bugs or issues
3. Performance considerations
4. Security concerns
5. Suggested improvements
```

#### Documentation Generation
```
Generate documentation for this code/API:

Code/API:
[Paste code or API specification]

Generate:
1. Overview description
2. Parameters/inputs
3. Return values/outputs
4. Usage examples
5. Error handling
```

### 8. General Productivity Prompts

#### Email Drafting
```
Draft an email:

Purpose: [What you want to achieve]
Recipient: [Who, their role/relationship]
Tone: [Formal/Casual/Urgent]
Key Points:
[List main points to cover]

Requirements:
- Clear subject line
- Appropriate length
- Professional signature
```

#### Research Summary
```
Summarize this research/article:

Content:
[Paste article or research]

Provide:
1. Key findings (bullet points)
2. Implications for [our industry/company]
3. Recommended actions
4. Related topics to explore
5. Source reliability assessment
```

### 9. Prompt Engineering Tips

#### Making Prompts Better
1. **Be Specific**: Include context, constraints, and desired format
2. **Use Examples**: Show what good output looks like
3. **Iterate**: Refine prompts based on results
4. **Chain Prompts**: Break complex tasks into steps

#### Common Mistakes to Avoid
- Too vague or open-ended
- No context about audience or purpose
- Forgetting to specify format
- Not reviewing/editing output

### 10. Custom Prompt Template

```
# [Task Name] Prompt

## Context
[Background information the AI needs]

## Input
[What you're providing]
[Paste input here]

## Requirements
- [Requirement 1]
- [Requirement 2]
- [Requirement 3]

## Output Format
[Specify how you want the response structured]

## Additional Notes
[Any constraints, preferences, or guidelines]
```

## Output Format
- Provide copy-paste ready prompts
- Include clear placeholder indicators [like this]
- Organize by department/function
- Include usage tips
- Make prompts customizable
"""
