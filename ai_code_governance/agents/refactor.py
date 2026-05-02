class RefactorAgent:
    def __init__(self, logger):
        self.logger = logger

    def run(self, findings):
        plans = []

        for item in findings:
            plans.append({
                "file": item["file"],
                "issue": item["issue"],
                "refactor": f"Resolve: {item['issue']}"
            })

        return plans