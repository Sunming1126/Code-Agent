# Fullstack AI Code Governance Platform

Enterprise-grade multi-agent code governance system with:
- FastAPI backend
- Repository scanning
- Security validation
- Refactor planning
- Test simulation
- Audit logging
- HTML + JSON reporting
- Docker support
- Modular architecture

## Quick Start

### Local
```bash
pip install -r requirements.txt
python main.py
```

### API Server
```bash
uvicorn api:app --reload
```

### Docker
```bash
docker build -t ai-code-governance .
docker run -p 8000:8000 ai-code-governance
```

## API Endpoint
POST /scan

## Workflow
Scan → Security → Refactor → Test → Review → Report

## Production Features
- Input sanitization
- Structured config
- Exception isolation
- Repository validation
- Audit logs
- Exportable reports