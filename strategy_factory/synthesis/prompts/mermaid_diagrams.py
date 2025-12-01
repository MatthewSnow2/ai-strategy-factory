"""Prompt for Mermaid Diagrams (Current State + Future State)."""

PROMPT = """
# Task: Generate Mermaid Diagrams for Current and Future State

Based on the technology inventory and pain points identified above, create Mermaid diagrams that visualize the company's AI transformation journey.

## Required Diagrams

### 1. Current State Architecture

Create a Mermaid flowchart showing the current technology landscape:

```mermaid
flowchart TB
    subgraph "Current State: {company_name}"
        subgraph "Data Sources"
            DS1[Source 1]
            DS2[Source 2]
        end
        
        subgraph "Core Systems"
            CS1[System 1]
            CS2[System 2]
        end
        
        subgraph "Users"
            U1[Department 1]
            U2[Department 2]
        end
    end
```

Include:
- Data sources and databases
- Core business systems
- Integration points
- User touchpoints
- Known bottlenecks (mark with red/warning indicators)

### 2. Future State Architecture (AI-Enabled)

Create a Mermaid flowchart showing the target AI-enabled architecture:

```mermaid
flowchart TB
    subgraph "Future State: {company_name}"
        subgraph "Data Layer"
            DL[Unified Data Platform]
        end
        
        subgraph "AI Layer"
            AI1[AI Service 1]
            AI2[AI Service 2]
        end
        
        subgraph "Application Layer"
            APP1[Enhanced App 1]
        end
    end
```

Include:
- Unified data platform
- AI/ML services layer
- Enhanced applications
- New integrations
- Automation flows

### 3. Data Flow Diagram

Create a Mermaid sequence or flowchart showing how data flows through the organization:

```mermaid
flowchart LR
    subgraph "Data Flow"
        Input --> Processing --> Storage --> Analytics --> Action
    end
```

Show:
- Data ingestion points
- Processing steps
- Storage locations
- Analytics touchpoints
- Action triggers

### 4. AI Implementation Roadmap (Visual)

Create a Mermaid Gantt chart showing implementation phases:

```mermaid
gantt
    title AI Implementation Roadmap
    dateFormat  YYYY-MM-DD
    section Phase 1
    Foundation    :a1, 2024-01-01, 30d
    section Phase 2
    Quick Wins    :a2, after a1, 60d
    section Phase 3
    Scale         :a3, after a2, 90d
```

### 5. Integration Architecture

Create a Mermaid diagram showing system integrations:

```mermaid
flowchart TB
    subgraph "Integration Hub"
        API[API Gateway]
        ETL[ETL Pipeline]
        MSG[Message Queue]
    end
```

## Output Format

For each diagram:
1. Provide the complete Mermaid code block
2. Add a brief description explaining the diagram
3. Highlight key transformation points
4. Note any assumptions made

## Important Notes
- Use valid Mermaid syntax
- Keep diagrams readable (not too complex)
- Use consistent naming conventions
- Include legends where helpful
- Customize to the specific company context
"""
