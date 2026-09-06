import random
from typing import Dict, List, Tuple
from schemas import LoanApplication, RiskAssessmentResponse

class CrediGuardEngine:
    """
    Multi-Agent Financial Risk Assessment & Fraud Detection Engine.
    Simulates autonomous financial analysis, debt service coverage calculation,
    and fraud anomaly detection.
    """
    
    def __init__(self, random_seed: int = 42):
        random.seed(random_seed)

    def evaluate(self, app: LoanApplication) -> RiskAssessmentResponse:
        audit_trail = ["Agent initialized: Parsing financial statements & tax records."]
        
        # 1. Financial Ratio Analysis Agent
        fin = app.financials
        dscr = (fin.ebitda - 0.1 * fin.total_debt) / max((app.requested_amount / (app.loan_term_months / 12)), 1.0)
        leverage = fin.total_debt / max(fin.ebitda, 1.0)
        
        audit_trail.append(f"Financial Agent calculated DSCR: {dscr:.2f}, Leverage Ratio: {leverage:.2f}.")

        # 2. Fraud & Anomaly Agent
        fraud_penalty = app.bank_statement_anomalies * 15.0
        if app.tax_compliance_status.lower() != "compliant":
            fraud_penalty += 25.0
        
        audit_trail.append(f"Fraud Agent computed penalty index: {fraud_penalty:.1f} based on bank anomalies & tax status.")

        # 3. Base Risk Calculation Engine
        base_score = 30.0
        if dscr < 1.25:
            base_score += 25.0
        elif dscr > 2.0:
            base_score -= 10.0
            
        if leverage > 4.0:
            base_score += 20.0
            
        total_risk_score = min(max(base_score + fraud_penalty, 0.0), 100.0)

        # 4. Decision & Pricing Agent
        risk_factors = []
        mitigation_strategies = []

        if dscr < 1.25:
            risk_factors.append("Low Debt Service Coverage Ratio (DSCR < 1.25x).")
            mitigation_strategies.append("Require collateral backstop or founder personal guarantee.")
        if leverage > 3.5:
            risk_factors.append("High leverage ratio (> 3.5x debt/EBITDA).")
            mitigation_strategies.append("Cap maximum loan tenure to 24 months.")
        if app.bank_statement_anomalies > 0:
            risk_factors.append(f"Detected {app.bank_statement_anomalies} suspicious bank statement transactions.")
            mitigation_strategies.append("Flag for manual forensic audit before disbursement.")

        if total_risk_score < 35.0:
            decision = "APPROVED"
            pricing = 8.5
            recommended_max = app.requested_amount
        elif total_risk_score < 65.0:
            decision = "MANUAL_REVIEW"
            pricing = 11.5
            recommended_max = app.requested_amount * 0.75
        else:
            decision = "REJECTED"
            pricing = 16.0
            recommended_max = 0.0

        audit_trail.append(f"Underwriting Agent finalized Decision: {decision} with Risk Score: {total_risk_score:.1f}/100.")

        return RiskAssessmentResponse(
            applicant_id=app.applicant_id,
            company_name=app.company_name,
            risk_score=round(total_risk_score, 1),
            decision=decision,
            recommended_max_loan=round(recommended_max, 2),
            interest_rate_pricing=pricing,
            dscr_ratio=round(dscr, 2),
            leverage_ratio=round(leverage, 2),
            risk_factors=risk_factors if risk_factors else ["No critical risk factors identified."],
            mitigation_strategies=mitigation_strategies if mitigation_strategies else ["Standard loan terms apply."],
            audit_trail=audit_trail
        )
