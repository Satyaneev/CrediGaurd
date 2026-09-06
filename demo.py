import json
from schemas import LoanApplication, FinancialStatement
from risk_engine import CrediGuardEngine

def run_demo():
    print("=== CrediGuard AI: Autonomous BFSI Risk Engine Demo ===")
    
    # Test case 1: Prime Commercial Borrower
    app1 = LoanApplication(
        applicant_id="APP-9901",
        company_name="Apex Global Logistics Inc.",
        requested_amount=1500000.0,
        loan_term_months=36,
        industry="Logistics",
        financials=FinancialStatement(
            revenue=12000000.0,
            ebitda=2800000.0,
            total_debt=4000000.0,
            cash_reserves=1500000.0,
            operating_cash_flow=2200000.0
        ),
        bank_statement_anomalies=0,
        tax_compliance_status="Compliant"
    )
    
    # Test case 2: High Risk / Fraud Flagged Borrower
    app2 = LoanApplication(
        applicant_id="APP-9902",
        company_name="Vanguard Retail Solutions",
        requested_amount=800000.0,
        loan_term_months=24,
        industry="Retail",
        financials=FinancialStatement(
            revenue=3500000.0,
            ebitda=300000.0,
            total_debt=1800000.0,
            cash_reserves=100000.0,
            operating_cash_flow=150000.0
        ),
        bank_statement_anomalies=2,
        tax_compliance_status="Non-Compliant"
    )
    
    engine = CrediGuardEngine()
    
    for app in [app1, app2]:
        print(f"\n--- Evaluating Application: {app.company_name} ({app.applicant_id}) ---")
        res = engine.evaluate(app)
        print(f"Risk Score   : {res.risk_score}/100")
        print(f"Decision     : {res.decision}")
        print(f"Approved Max : ${res.recommended_max_loan:,.2f}")
        print(f"Pricing Rate : {res.interest_rate_pricing}%")
        print(f"DSCR Ratio   : {res.dscr_ratio}x")
        print(f"Risk Factors : {res.risk_factors}")
        print(f"Audit Trail  : {json.dumps(res.audit_trail, indent=2)}")

if __name__ == "__main__":
    run_demo()
