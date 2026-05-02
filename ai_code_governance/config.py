from pydantic import BaseModel

class Settings(BaseModel):
    max_file_size: int = 50000
    allowed_extensions: list[str] = [".py"]
    log_path: str = "logs/audit.log"
    report_dir: str = "reports"