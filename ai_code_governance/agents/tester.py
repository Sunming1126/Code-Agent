class TestAgent:
    def __init__(self, logger):
        self.logger = logger

    def run(self, plans):
        results = []

        for plan in plans:
            results.append({
                "file": plan["file"],
                "status": "PASS",
                "details": "Simulated validation success"
            })

        return results