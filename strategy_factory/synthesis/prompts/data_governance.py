"""Prompt for Data Governance Framework."""

PROMPT = """
# Task: Generate Data Governance Framework

Based on the technology inventory, regulatory context, and AI policy above, create a comprehensive data governance framework for AI initiatives.

## Required Sections

### 1. Executive Summary
- Data governance maturity assessment
- Key risks identified
- Priority recommendations
- Resource requirements

### 2. Data Governance Vision

#### Principles
1. **Data as an Asset**: Treat data as a strategic resource
2. **Quality at Source**: Ensure accuracy at point of entry
3. **Security by Design**: Build protection into all processes
4. **Transparency**: Clear ownership and lineage
5. **Compliance First**: Regulatory requirements are non-negotiable

#### Objectives
- Enable AI initiatives with trusted data
- Minimize data-related risks
- Establish clear accountability
- Streamline data access

### 3. Data Governance Structure

#### Organizational Model

```
[Data Governance Council]
        |
[Data Governance Office]
        |
    ----------
    |        |
[Domain Stewards] [Technical Stewards]
```

#### Roles & Responsibilities

| Role | Responsibilities | Reports To |
|------|-----------------|------------|
| Executive Sponsor | Strategy, budget, escalations | CEO |
| Data Governance Council | Policy approval, priorities | Exec Sponsor |
| Chief Data Officer | Program leadership | Council |
| Domain Data Stewards | Business data ownership | CDO |
| Technical Data Stewards | Data quality, metadata | CDO |
| Data Custodians | System-level management | Tech Stewards |

### 4. Data Classification Framework

#### Classification Levels

| Level | Definition | Examples | Handling Requirements |
|-------|------------|----------|----------------------|
| Public | Freely shareable | Marketing content | None |
| Internal | Company use only | Org charts, policies | Access controls |
| Confidential | Business sensitive | Financial data, strategies | Encryption, logging |
| Restricted | Highly sensitive | PII, health data, secrets | Full controls, approval |

#### AI-Specific Classifications

| Data Type | AI Training | AI Input | AI Output |
|-----------|-------------|----------|-----------|
| Customer data | Prohibited | Restricted | Review required |
| Transaction data | With consent | Anonymized | Permitted |
| Operational data | Permitted | Permitted | Permitted |
| Public data | Permitted | Permitted | Permitted |

### 5. Data Quality Framework

#### Quality Dimensions

| Dimension | Definition | Measurement | Target |
|-----------|------------|-------------|--------|
| Accuracy | Correctness | Error rate | <1% |
| Completeness | No missing values | Null rate | >95% |
| Consistency | Same across systems | Match rate | >99% |
| Timeliness | Current/updated | Freshness | <24 hrs |
| Uniqueness | No duplicates | Dup rate | <0.1% |
| Validity | Conforms to rules | Validation rate | >99% |

#### Quality Monitoring

| System | Quality Checks | Frequency | Owner |
|--------|---------------|-----------|-------|
| [System 1] | | Daily | |
| [System 2] | | Weekly | |

### 6. Data Lifecycle Management

#### Lifecycle Stages

| Stage | Activities | Controls | Retention |
|-------|-----------|----------|-----------|
| Creation | Capture, entry | Validation | - |
| Storage | Persistence | Encryption | Per policy |
| Processing | Transform, analyze | Logging | - |
| Sharing | Distribution | Access control | - |
| Archival | Long-term storage | Integrity checks | Per regulation |
| Disposal | Secure deletion | Verification | - |

#### AI Data Lifecycle

| Stage | Considerations | Requirements |
|-------|---------------|--------------|
| Collection | Consent, purpose | Documentation |
| Preparation | Anonymization | Quality checks |
| Training | Version control | Audit trail |
| Inference | Input validation | Monitoring |
| Model Updates | Retraining data | Approval |

### 7. Data Privacy & Protection

#### Privacy Principles
- Data minimization
- Purpose limitation
- Consent management
- Individual rights

#### Compliance Requirements

| Regulation | Scope | Key Requirements | Status |
|------------|-------|------------------|--------|
| GDPR | EU data | Consent, rights | |
| CCPA | CA residents | Disclosure, opt-out | |
| [Industry-specific] | | | |

#### Privacy Controls
| Control | Purpose | Implementation |
|---------|---------|----------------|
| Anonymization | Remove identifiers | [Method] |
| Pseudonymization | Replace identifiers | [Method] |
| Encryption | Protect data | [Standard] |
| Access controls | Limit access | [System] |

### 8. Metadata Management

#### Metadata Standards

| Metadata Type | Description | Required Fields |
|---------------|-------------|-----------------|
| Technical | Schema, formats | Table name, columns, types |
| Business | Definitions, ownership | Definition, steward, domain |
| Operational | Quality, lineage | Quality score, source, updates |

#### Data Catalog Requirements
- Searchable inventory of all data assets
- Business glossary integration
- Lineage visualization
- Quality metrics display

### 9. Data Access & Security

#### Access Control Model

| Data Classification | Access Model | Approval Required |
|--------------------|--------------|-------------------|
| Public | Open | No |
| Internal | Role-based | No |
| Confidential | Need-to-know | Manager |
| Restricted | Explicit grant | Data owner + Security |

#### AI Model Access
| Model Type | Data Access | Restrictions |
|------------|-------------|--------------|
| Internal models | Full (approved data) | Audit logging |
| External AI tools | Limited | No restricted data |
| Vendor models | As contracted | DPA required |

### 10. Implementation Roadmap

#### Phase 1: Foundation (Months 1-3)
- [ ] Establish governance council
- [ ] Define classification scheme
- [ ] Identify critical data assets
- [ ] Appoint data stewards

#### Phase 2: Build (Months 4-6)
- [ ] Implement data catalog
- [ ] Deploy quality monitoring
- [ ] Create privacy controls
- [ ] Develop training program

#### Phase 3: Scale (Months 7-12)
- [ ] Expand coverage
- [ ] Automate quality checks
- [ ] Advanced lineage tracking
- [ ] Continuous improvement

### 11. Metrics & Monitoring

| Metric | Target | Frequency | Owner |
|--------|--------|-----------|-------|
| Data quality score | >90% | Weekly | |
| Policy compliance | 100% | Monthly | |
| Incident response time | <4 hrs | Per incident | |
| Training completion | 100% | Quarterly | |

## Output Format
- Use professional governance language
- Include specific policies and procedures
- Customize to industry requirements
- Make roles and responsibilities clear
- Include actionable implementation steps
"""
