# Enterprise Change Risk Platform

AI-assisted operational platform designed to evaluate deployment risks, analyze operational impact, and support enterprise change management workflows.

---

## Current Capabilities

- Deployment change dataset modeling
- Change retrieval APIs
- Operational risk metadata structure
- FastAPI backend foundation
- Modular project architecture
- Deployment risk scoring engine
- Operational risk intelligence APIs
- Dynamic deployment risk classification
- Historical deployment failure retrieval
- Context-aware operational risk analysis
- Historical intelligence enrichment workflows
- Operational deployment advisory engine
- Monitoring strategy recommendations
- Rollback planning guidance
- Dynamic deployment submission APIs
- Schema-based request validation
- User-driven risk intelligence workflows
- Deployment approval recommendation engine
- Operational governance workflows
- CAB-style decision support
- Executive deployment reporting
- Business impact summarization
- Stakeholder-oriented risk communication

---

## Tech Stack

- Python
- FastAPI
- Pydantic
- Pandas
- Conda Environment

---

## API Endpoints

### Health Check

```http
GET /
```

### Retrieve Deployment Changes

```http
GET /changes
```

---

### Deployment Advisory

```http
GET /changes/advisory/{risk_level}
```

Generates operational deployment recommendations, monitoring guidance, and rollback strategies based on calculated deployment risk.


### Analyze Deployment Change

```http
POST /changes/analyze
```

Accepts deployment change requests and generates operational risk intelligence dynamically.

Example Request:

```json
{
  "service": "Payment Gateway",
  "change_type": "Infrastructure Update",
  "deployment_window": "Peak Hours",
  "affected_regions": 3,
  "rollback_available": false,
  "recent_failures": 2
}
```

### Deployment Approval Decision

```http
GET /changes/approval/{risk_level}
```

Generates deployment approval recommendations based on calculated operational risk levels.


### Executive Deployment Report

```http
POST /changes/report
```

Generates a stakeholder-friendly deployment report containing deployment risk, approval status, business impact, and recommended actions.

## Project Structure

```text
enterprise-change-risk-platform/
│
├── app/
│   ├── api/
│   ├── core/
│   ├── datasets/
│   ├── models/
│   ├── services/
│   ├── utils/
│   └── main.py
│
├── tests/
│
├── requirements.txt
├── README.md
└── .env
```

---

## Development Focus

Ongoing development areas include:
- deployment risk scoring
- historical change retrieval
- AI-assisted operational advisory
- contextual operational intelligence
- workflow orchestration


---

## Current Development Status

The platform is currently in the foundational architecture phase.

Upcoming enhancements include:
- deployment risk scoring
- historical change retrieval
- AI-assisted deployment advisory
- contextual operational intelligence
- semantic risk analysis workflows


### Deployment Risk Analysis

```http
GET /changes/risk-analysis
```

Calculates operational deployment risk scores using deployment metadata, rollback availability, regional impact, and historical failure indicators.



---

## Risk Intelligence Workflow

The platform includes a deterministic operational risk engine designed to evaluate deployment safety using enterprise operational signals.

Current scoring considers:
- deployment timing
- rollback availability
- regional impact
- historical deployment failures


### Historical Deployment Intelligence

```http
GET /changes/history/{service_name}
```

Retrieves historical deployment failures, operational root causes, and resolution workflows for enterprise services.


---

## Historical Intelligence Workflow

The platform includes a historical retrieval layer for enriching deployment risk analysis with operational context and known failure patterns.

Current implementation uses service-based retrieval and is designed to evolve toward semantic operational intelligence workflows.


---

## Operational Advisory Workflow

The platform includes an operational advisory engine that converts deployment risk classifications into actionable deployment recommendations.

Recommendations currently include:
- deployment approval guidance
- monitoring requirements
- rollback planning strategies

The advisory layer is designed to support enterprise change management and deployment governance workflows.


---

## Dynamic Risk Analysis Workflow

Deployment requests are submitted through API endpoints and validated using typed request models before entering the risk intelligence pipeline.

Workflow:

Request Validation
→ Risk Scoring
→ Historical Intelligence
→ Operational Advisory
→ Response Generation


---

## Deployment Governance Workflow

The platform includes an approval recommendation layer designed to support enterprise deployment governance processes.

Current decisions include:

- Approved
- Conditional Approval
- Rejected

Approval recommendations are generated using deployment risk classifications and operational intelligence outputs.


---

## Executive Reporting Workflow

The platform includes a reporting layer that transforms technical deployment analysis into business-oriented deployment summaries.

Reporting outputs include:

- deployment risk classification
- approval recommendation
- business impact summary
- operational action guidance