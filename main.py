from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from schemas import LoanApplication, RiskAssessmentResponse
from risk_engine import CrediGuardEngine

app = FastAPI(
    title="CrediGuard AI - Autonomous BFSI Underwriting API",
    version="1.0.0",
    description="Real-time multi-agent underwriting and fraud risk scoring engine."
)

engine = CrediGuardEngine()

HTML_CONTENT = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CrediGuard AI - Underwriting Dashboard</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap" rel="stylesheet">
    <style>body { font-family: 'Inter', sans-serif; }</style>
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen">
    <div class="max-w-6xl mx-auto px-4 py-8">
        <!-- Header -->
        <header class="flex items-center justify-between border-b border-slate-800 pb-5 mb-8">
            <div class="flex items-center space-x-3">
                <div class="h-10 w-10 bg-indigo-600 rounded-lg flex items-center justify-center font-bold text-xl shadow-lg shadow-indigo-500/30">CG</div>
                <div>
                    <h1 class="text-2xl font-bold tracking-tight text-white">CrediGuard AI</h1>
                    <p class="text-xs text-slate-400">Autonomous Enterprise Underwriting & Fraud Risk Engine</p>
                </div>
            </div>
            <span class="bg-emerald-500/10 text-emerald-400 text-xs px-3 py-1.5 rounded-full border border-emerald-500/20 flex items-center gap-2">
                <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span> Engine Online
            </span>
        </header>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8">
            <!-- Application Form -->
            <div class="lg:col-span-5 bg-slate-900/80 border border-slate-800 rounded-2xl p-6 shadow-xl">
                <h2 class="text-lg font-semibold text-white mb-4 flex items-center gap-2">
                    <svg class="w-5 h-5 text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg>
                    Loan Application Form
                </h2>
                
                <form id="loanForm" class="space-y-4">
                    <div>
                        <label class="block text-xs font-medium text-slate-400 mb-1">Applicant / Company Name</label>
                        <input type="text" id="company_name" value="Apex Global Logistics Inc." class="w-full bg-slate-950 border border-slate-800 rounded-lg px-3 py-2 text-sm text-white focus:outline-none focus:border-indigo-500">
                    </div>
                    
                    <div class="grid grid-cols-2 gap-3">
                        <div>
                            <label class="block text-xs font-medium text-slate-400 mb-1">Requested Loan ($)</label>
                            <input type="number" id="requested_amount" value="1500000" class="w-full bg-slate-950 border border-slate-800 rounded-lg px-3 py-2 text-sm text-white focus:outline-none focus:border-indigo-500">
                        </div>
                        <div>
                            <label class="block text-xs font-medium text-slate-400 mb-1">Tenure (Months)</label>
                            <input type="number" id="loan_term_months" value="36" class="w-full bg-slate-950 border border-slate-800 rounded-lg px-3 py-2 text-sm text-white focus:outline-none focus:border-indigo-500">
                        </div>
                    </div>

                    <div class="grid grid-cols-2 gap-3">
                        <div>
                            <label class="block text-xs font-medium text-slate-400 mb-1">Annual Revenue ($)</label>
                            <input type="number" id="revenue" value="12000000" class="w-full bg-slate-950 border border-slate-800 rounded-lg px-3 py-2 text-sm text-white focus:outline-none focus:border-indigo-500">
                        </div>
                        <div>
                            <label class="block text-xs font-medium text-slate-400 mb-1">EBITDA ($)</label>
                            <input type="number" id="ebitda" value="2800000" class="w-full bg-slate-950 border border-slate-800 rounded-lg px-3 py-2 text-sm text-white focus:outline-none focus:border-indigo-500">
                        </div>
                    </div>

                    <div class="grid grid-cols-2 gap-3">
                        <div>
                            <label class="block text-xs font-medium text-slate-400 mb-1">Total Debt ($)</label>
                            <input type="number" id="total_debt" value="4000000" class="w-full bg-slate-950 border border-slate-800 rounded-lg px-3 py-2 text-sm text-white focus:outline-none focus:border-indigo-500">
                        </div>
                        <div>
                            <label class="block text-xs font-medium text-slate-400 mb-1">Cash Reserves ($)</label>
                            <input type="number" id="cash_reserves" value="1500000" class="w-full bg-slate-950 border border-slate-800 rounded-lg px-3 py-2 text-sm text-white focus:outline-none focus:border-indigo-500">
                        </div>
                    </div>

                    <div class="grid grid-cols-2 gap-3">
                        <div>
                            <label class="block text-xs font-medium text-slate-400 mb-1">Bank Statement Anomalies</label>
                            <input type="number" id="bank_anomalies" value="0" class="w-full bg-slate-950 border border-slate-800 rounded-lg px-3 py-2 text-sm text-white focus:outline-none focus:border-indigo-500">
                        </div>
                        <div>
                            <label class="block text-xs font-medium text-slate-400 mb-1">Tax Status</label>
                            <select id="tax_status" class="w-full bg-slate-950 border border-slate-800 rounded-lg px-3 py-2 text-sm text-white focus:outline-none focus:border-indigo-500">
                                <option value="Compliant">Compliant</option>
                                <option value="Non-Compliant">Non-Compliant</option>
                            </select>
                        </div>
                    </div>

                    <button type="button" onclick="evaluateRisk()" class="w-full mt-4 bg-indigo-600 hover:bg-indigo-500 text-white font-semibold py-2.5 rounded-lg shadow-lg shadow-indigo-600/30 transition text-sm flex items-center justify-center gap-2">
                        <span>Evaluate Risk & Underwrite</span>
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
                    </button>
                </form>
            </div>

            <!-- Risk Output Results -->
            <div class="lg:col-span-7 space-y-6">
                <div id="resultsCard" class="bg-slate-900/80 border border-slate-800 rounded-2xl p-6 shadow-xl">
                    <h2 class="text-lg font-semibold text-white mb-4 flex items-center justify-between">
                        <span>Underwriting Analysis</span>
                        <span id="decisionBadge" class="text-xs px-3 py-1 rounded-full font-bold bg-slate-800 text-slate-400">AWAITING INPUT</span>
                    </h2>

                    <div class="grid grid-cols-3 gap-4 mb-6">
                        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800/80 text-center">
                            <span class="text-xs text-slate-400 block mb-1">Risk Score</span>
                            <span id="riskScore" class="text-2xl font-bold text-indigo-400">--</span><span class="text-xs text-slate-500">/100</span>
                        </div>
                        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800/80 text-center">
                            <span class="text-xs text-slate-400 block mb-1">Approved Loan</span>
                            <span id="approvedMax" class="text-xl font-bold text-emerald-400">$0</span>
                        </div>
                        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800/80 text-center">
                            <span class="text-xs text-slate-400 block mb-1">Pricing Interest</span>
                            <span id="pricingRate" class="text-xl font-bold text-amber-400">-- %</span>
                        </div>
                    </div>

                    <div class="grid grid-cols-2 gap-4 mb-6">
                        <div class="bg-slate-950/60 p-3 rounded-lg border border-slate-800/50">
                            <span class="text-xs text-slate-400">DSCR Ratio: </span>
                            <span id="dscrRatio" class="text-sm font-semibold text-white">--</span>
                        </div>
                        <div class="bg-slate-950/60 p-3 rounded-lg border border-slate-800/50">
                            <span class="text-xs text-slate-400">Leverage Ratio: </span>
                            <span id="leverageRatio" class="text-sm font-semibold text-white">--</span>
                        </div>
                    </div>

                    <div class="space-y-4">
                        <div>
                            <h4 class="text-xs font-semibold text-slate-400 uppercase tracking-wider mb-2">Identified Risk Factors</h4>
                            <ul id="riskFactors" class="text-xs space-y-1.5 text-slate-300">
                                <li class="text-slate-500 italic">Submit application to generate risk factors</li>
                            </ul>
                        </div>

                        <div>
                            <h4 class="text-xs font-semibold text-slate-400 uppercase tracking-wider mb-2">Multi-Agent Audit Trail</h4>
                            <div id="auditTrail" class="bg-slate-950 p-3 rounded-lg border border-slate-800 text-xs font-mono text-slate-400 space-y-1 max-h-40 overflow-y-auto">
                                <p class="text-slate-600">// Waiting for analysis request...</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script>
        async function evaluateRisk() {
            const payload = {
                applicant_id: "APP-" + Math.floor(1000 + Math.random() * 9000),
                company_name: document.getElementById('company_name').value,
                requested_amount: parseFloat(document.getElementById('requested_amount').value),
                loan_term_months: parseInt(document.getElementById('loan_term_months').value),
                industry: "Commercial Services",
                financials: {
                    revenue: parseFloat(document.getElementById('revenue').value),
                    ebitda: parseFloat(document.getElementById('ebitda').value),
                    total_debt: parseFloat(document.getElementById('total_debt').value),
                    cash_reserves: parseFloat(document.getElementById('cash_reserves').value),
                    operating_cash_flow: parseFloat(document.getElementById('ebitda').value) * 0.8
                },
                bank_statement_anomalies: parseInt(document.getElementById('bank_anomalies').value),
                tax_compliance_status: document.getElementById('tax_status').value
            };

            try {
                const res = await fetch('/api/v1/evaluate', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(payload)
                });
                const data = await res.json();

                document.getElementById('riskScore').innerText = data.risk_score;
                document.getElementById('approvedMax').innerText = '$' + data.recommended_max_loan.toLocaleString();
                document.getElementById('pricingRate').innerText = data.interest_rate_pricing + '%';
                document.getElementById('dscrRatio').innerText = data.dscr_ratio + 'x';
                document.getElementById('leverageRatio').innerText = data.leverage_ratio + 'x';

                const badge = document.getElementById('decisionBadge');
                badge.innerText = data.decision;
                if(data.decision === 'APPROVED') {
                    badge.className = "text-xs px-3 py-1 rounded-full font-bold bg-emerald-500/20 text-emerald-400 border border-emerald-500/30";
                } else if(data.decision === 'MANUAL_REVIEW') {
                    badge.className = "text-xs px-3 py-1 rounded-full font-bold bg-amber-500/20 text-amber-400 border border-amber-500/30";
                } else {
                    badge.className = "text-xs px-3 py-1 rounded-full font-bold bg-rose-500/20 text-rose-400 border border-rose-500/30";
                }

                const factorsList = document.getElementById('riskFactors');
                factorsList.innerHTML = data.risk_factors.map(f => `<li class="flex items-center gap-2"><span class="w-1.5 h-1.5 rounded-full bg-indigo-400"></span>${f}</li>`).join('');

                const auditBox = document.getElementById('auditTrail');
                auditBox.innerHTML = data.audit_trail.map(a => `<p class="text-indigo-300">> ${a}</p>`).join('');
            } catch(e) {
                alert('Error submitting loan evaluation: ' + e);
            }
        }
    </script>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
def read_root():
    return HTML_CONTENT

@app.post("/api/v1/evaluate", response_model=RiskAssessmentResponse)
def evaluate_loan(application: LoanApplication):
    try:
        result = engine.evaluate(application)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
