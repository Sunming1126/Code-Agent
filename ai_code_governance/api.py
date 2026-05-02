from fastapi import FastAPI
from pydantic import BaseModel

from config import Settings
from core.logger import get_logger
from core.security import sanitize_path, validate_repo
from pipeline import GovernancePipeline

app = FastAPI(title="AI Code Governance API")

config = Settings()
logger = get_logger(config.log_path)
pipeline = GovernancePipeline(config, logger)

class ScanRequest(BaseModel):
    repo_path: str

@app.post("/scan")
def scan_repo(req: ScanRequest):
    repo_path = sanitize_path(req.repo_path)
    validate_repo(repo_path)
    return pipeline.execute(repo_path)