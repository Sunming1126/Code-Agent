from config import Settings
from core.logger import get_logger
from core.security import sanitize_path, validate_repo
from core.reporting import save_json_report, save_html_report
from pipeline import GovernancePipeline

def main():
    config = Settings()
    logger = get_logger(config.log_path)

    repo_path = sanitize_path("./sample_repo")
    validate_repo(repo_path)

    pipeline = GovernancePipeline(config, logger)
    report = pipeline.execute(repo_path)

    json_path = save_json_report(report, config.report_dir)
    html_path = save_html_report(report, config.report_dir)

    print("Governance completed.")
    print("JSON:", json_path)
    print("HTML:", html_path)

if __name__ == "__main__":
    main()