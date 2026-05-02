import os

class ScannerAgent:
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger

    def run(self, repo_path):
        findings = []

        for root, _, files in os.walk(repo_path):
            for file in files:
                if any(file.endswith(ext) for ext in self.config.allowed_extensions):
                    full_path = os.path.join(root, file)

                    try:
                        with open(full_path, "r", encoding="utf-8") as f:
                            content = f.read()

                        if "TODO" in content:
                            findings.append({
                                "file": full_path,
                                "issue": "TODO markers detected"
                            })

                        if "eval(" in content:
                            findings.append({
                                "file": full_path,
                                "issue": "Unsafe eval usage"
                            })

                        if len(content) > self.config.max_file_size:
                            findings.append({
                                "file": full_path,
                                "issue": "Oversized file"
                            })

                    except Exception as e:
                        self.logger.error(f"Scan failed for {full_path}: {e}")

        return findings