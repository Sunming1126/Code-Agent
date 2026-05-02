import os

def sanitize_path(path: str) -> str:
    return os.path.abspath(path)

def validate_repo(path: str):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Repository not found: {path}")
    if not os.path.isdir(path):
        raise ValueError("Path must be a directory")
    return True