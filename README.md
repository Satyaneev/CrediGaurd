# CrediGuard AI - Autonomous Enterprise Credit Risk & Fraud Graph Engine

## Overview
CrediGuard AI is an autonomous, multi-agent financial underwriting and fraud detection engine built for banking, financial services, and commercial lending institutions. It automates financial document parsing, debt service coverage ratio (DSCR) calculations, tax anomaly verification, and risk pricing in under 5 seconds.

## Architecture & Data Flow
```
[ Loan Application ] 
       │
       ▼
[ Multi-Agent Orchestrator ]
 ├──> 1. Financial Ratio Agent (DSCR, Debt/EBITDA, Cashflow metrics)
 ├──> 2. Forensic Fraud Agent (Bank anomaly detection, Tax compliance verification)
 └──> 3. Underwriting & Risk Pricing Agent (Risk score 0-100, Decision, Pricing matrix)
       │
       ▼
[ Audit-Logged Decision Payload ]
```

## Quick Start
```bash
# Install dependencies
pip install -r requirements.txt

# Run CLI verification demo
python demo.py

# Launch FastAPI Server
python main.py
# Open Swagger docs at http://localhost:8001/docs
```
