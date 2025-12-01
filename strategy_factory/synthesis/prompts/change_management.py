"""Prompt for Change Management & Training Playbook."""

PROMPT = """
# Task: Generate Change Management & Training Playbook

Based on the roadmap, use case library, and organizational context above, create a comprehensive change management and training playbook for AI adoption.

## Required Sections

### 1. Executive Summary
- Change management approach
- Key stakeholder groups
- Training program overview
- Critical success factors
- Timeline and milestones

### 2. Change Management Framework

#### ADKAR Model Application

| Phase | Focus | Activities | Metrics |
|-------|-------|-----------|---------|
| **A**wareness | Why change is needed | Communications, town halls | Survey scores |
| **D**esire | Willingness to participate | WIIFM messaging, champions | Engagement rates |
| **K**nowledge | How to change | Training, documentation | Competency tests |
| **A**bility | Capability to implement | Practice, coaching, support | Usage metrics |
| **R**einforcement | Sustaining change | Recognition, feedback loops | Adoption rates |

#### Change Readiness Assessment

| Factor | Current State | Gap | Action |
|--------|--------------|-----|--------|
| Leadership support | | | |
| Employee openness | | | |
| Historical change success | | | |
| Communication channels | | | |
| Training infrastructure | | | |

### 3. Stakeholder Analysis

#### Stakeholder Matrix

| Stakeholder Group | Impact | Influence | Position | Strategy |
|-------------------|--------|-----------|----------|----------|
| Executive team | High | High | Champion | Engage as sponsors |
| Middle managers | High | Medium | Varies | Convert to advocates |
| Front-line employees | High | Low | Varies | Enable and support |
| IT team | Medium | Medium | Supportive | Technical partnership |
| HR team | Medium | Medium | Supportive | Process alignment |

#### Key Messages by Stakeholder

**For Executives**
- Strategic value and competitive advantage
- ROI projections and efficiency gains
- Risk mitigation through governance

**For Managers**
- Team productivity improvements
- Reduced administrative burden
- Better decision-making tools
- Support for implementation

**For Employees**
- Job enhancement, not replacement
- New skills development
- Reduced tedious tasks
- Career growth opportunities

### 4. Communication Plan

#### Communication Calendar

| Week | Audience | Message | Channel | Owner |
|------|----------|---------|---------|-------|
| 1 | All | AI initiative announcement | Town hall | CEO |
| 2 | Managers | Implementation details | Manager meeting | Project lead |
| 3 | All | FAQ and Q&A | Email + intranet | Comms |
| 4 | Teams | Department-specific plans | Team meetings | Managers |

#### Key Communication Touchpoints

**Launch Communications**
- Executive announcement email
- Town hall presentation
- FAQ document
- Intranet landing page

**Ongoing Communications**
- Weekly progress updates
- Success story spotlights
- Tips and tricks newsletter
- Feedback channels

#### Communication Templates

**Announcement Email Template**
```
Subject: Introducing AI at {company_name}: Enhancing How We Work

Dear Team,

[Opening about company's commitment to innovation]

[Brief overview of AI initiative]

[What this means for employees - emphasize augmentation]

[Timeline and next steps]

[Invitation to learn more]

[Signature]
```

### 5. Training Program Design

#### Training Curriculum Overview

| Level | Audience | Duration | Format | Content |
|-------|----------|----------|--------|---------|
| Foundations | All employees | 2 hours | Self-paced | AI basics, policy, tools |
| Practitioner | Power users | 8 hours | Workshop | Advanced usage, prompting |
| Champion | AI champions | 16 hours | Cohort | Best practices, coaching |
| Technical | IT/Dev | 24 hours | Technical | Integration, security |

#### Course 1: AI Foundations for Everyone

**Learning Objectives**
- Understand what AI is and isn't
- Know approved tools and policies
- Perform basic AI tasks
- Identify AI opportunities in your role

**Modules**
1. Introduction to AI (30 min)
   - What is AI?
   - Types of AI we use
   - Common misconceptions
   
2. AI at {company_name} (30 min)
   - Our AI strategy
   - Approved tools
   - Acceptable use policy
   
3. Getting Started (45 min)
   - Accessing AI tools
   - Basic prompting
   - Hands-on exercises
   
4. AI in Your Role (15 min)
   - Department-specific use cases
   - Next steps

**Assessment**
- Knowledge check quiz (80% pass)
- Practical exercise completion

#### Course 2: AI Practitioner Workshop

**Learning Objectives**
- Master advanced prompting techniques
- Apply AI to complex tasks
- Ensure quality and accuracy
- Share knowledge with peers

**Modules**
1. Advanced Prompting (2 hours)
2. Complex Use Cases (2 hours)
3. Quality Assurance (2 hours)
4. Practical Application (2 hours)

#### Training Resources

| Resource | Description | Access |
|----------|-------------|--------|
| Learning portal | All courses | [URL] |
| Prompt library | Ready-to-use prompts | [URL] |
| Best practices guide | Tips and tricks | [URL] |
| Office hours | Live Q&A | [Calendar] |

### 6. AI Champions Program

#### Program Overview
- Select 1-2 champions per department
- Additional training and early access
- Peer support and coaching role
- Feedback loop to central team

#### Champion Responsibilities
- Complete champion training
- Support colleagues with AI adoption
- Gather and relay feedback
- Share success stories
- Escalate issues to project team

#### Champion Selection Criteria
- Enthusiasm for technology
- Respected by peers
- Good communication skills
- Available capacity

### 7. Resistance Management

#### Anticipated Resistance

| Concern | Response | Action |
|---------|----------|--------|
| "AI will take my job" | Augmentation focus, reskilling | Training, WIIFM |
| "I don't trust AI" | Governance, human oversight | Policy education |
| "Too much to learn" | Incremental approach | Bite-sized training |
| "My work is too complex" | Start simple, build up | Quick wins demo |
| "Privacy concerns" | Data policies, controls | Transparency |

#### Resistance Mitigation Strategies
1. Early involvement in pilots
2. Success story sharing
3. One-on-one coaching
4. Manager support
5. Feedback incorporation

### 8. Measurement & Feedback

#### Adoption Metrics

| Metric | Target | Measurement | Frequency |
|--------|--------|-------------|-----------|
| Training completion | 90% | LMS data | Weekly |
| Tool activation | 80% | Login data | Weekly |
| Active usage | 60% | Usage logs | Monthly |
| Satisfaction score | 4.0/5 | Survey | Monthly |

#### Feedback Mechanisms
- Post-training surveys
- Monthly pulse checks
- AI feedback form
- Champion feedback sessions
- Manager check-ins

### 9. Sustainability Plan

#### Reinforcement Activities
- Monthly best practices webinars
- Quarterly AI innovation showcases
- Annual AI skills refresher
- Continuous prompt library updates

#### Long-term Support
- Ongoing help desk
- Community of practice
- Updated training for new features
- Performance integration

### 10. Implementation Timeline

| Month | Activities | Milestones |
|-------|-----------|------------|
| 1 | Communications launch, champion selection | Awareness established |
| 2 | Foundations training rollout | 50% trained |
| 3 | Practitioner workshops, first pilots | First use cases live |
| 4 | Full deployment, advanced training | 80% trained |
| 5 | Optimization, feedback incorporation | Adoption targets met |
| 6 | Sustainability handoff | Self-sustaining program |

## Output Format
- Practical, actionable guidance
- Templates and examples
- Specific to company context
- Measurable outcomes
- Realistic timeline
"""
