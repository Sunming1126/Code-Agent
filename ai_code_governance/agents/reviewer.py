class ReviewAgent:
    def __init__(self, logger):
        self.logger = logger

    def run(self, findings, risks, plans, tests):
        score = max(0, 100 - len(findings)*5 - len(risks)*10)

        return {
            "summary": {
                "issues": len(findings),
                "security_risks": len(risks),
                "refactors": len(plans),
                "tests_passed": len([t for t in tests if t["status"] == "PASS"])
            },
            "governance_score": score,
            "status": "APPROVED" if score >= 70 else "REQUIRES_REMEDIATION"
        }