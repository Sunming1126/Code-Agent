from agents.scanner import ScannerAgent
from agents.security import SecurityAgent
from agents.refactor import RefactorAgent
from agents.tester import TestAgent
from agents.reviewer import ReviewAgent

class GovernancePipeline:
    def __init__(self, config, logger):
        self.scanner = ScannerAgent(config, logger)
        self.security = SecurityAgent(logger)
        self.refactor = RefactorAgent(logger)
        self.tester = TestAgent(logger)
        self.reviewer = ReviewAgent(logger)

    def execute(self, repo_path):
        findings = self.scanner.run(repo_path)
        risks = self.security.run(findings)
        plans = self.refactor.run(findings)
        tests = self.tester.run(plans)
        review = self.reviewer.run(findings, risks, plans, tests)

        return {
            "findings": findings,
            "security": risks,
            "refactor": plans,
            "tests": tests,
            "final_review": review
        }