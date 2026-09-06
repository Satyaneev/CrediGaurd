from pydantic import BaseModel, Field
from typing import List, Dict, Optional

class FinancialStatement(BaseModel):
    revenue: float = Field(..., description="Annual revenue in USD")
    ebitda: float = Field(..., description="EBITDA in USD")
    total_debt: float = Field(..., description="Total outstanding debt in USD")
    cash_reserves: float = Field(..., description="Liquid cash reserves in USD")
    operating_cash_flow: float = Field(..., description="Operating cash flow in USD")

class LoanApplication(BaseModel):
    applicant_id: str
    company_name: str
    requested_amount: float
    loan_term_months: int
    industry: str
    financials: FinancialStatement
    bank_statement_anomalies: int = 0
    tax_compliance_status: str = "Compliant"

class RiskAssessmentResponse(BaseModel):
    applicant_id: str
    company_name: str
    risk_score: float = Field(..., description="Score between 0 (low risk) and 100 (high risk)")
    decision: str = Field(..., description="APPROVED, REJECTED, or MANUAL_REVIEW")
    recommended_max_loan: float
    interest_rate_pricing: float
    dscr_ratio: float
    leverage_ratio: float
    risk_factors: List[str]
    mitigation_strategies: List[str]
    audit_trail: List[str]
