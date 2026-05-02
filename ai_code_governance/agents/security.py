class SecurityAgent:
    def __init__(self, logger):
        self.logger = logger

    def run(self, findings):
        risks = []

        for item in findings:
            if "Unsafe" in item["issue"] or "eval" in item["issue"]:
                risks.append({
                    "file": item["file"],
                    "risk": "High",
                    "action": "Replace insecure execution"
                })

        return risks