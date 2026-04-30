# Autonomous AI Agent

A starter Python project for an autonomous AI agent backend using FastAPI.

## Project structure

- `app/` - backend application code
  - `main.py` - FastAPI application entrypoint
  - `routes.py` - API route registration
  - `core/` - configuration and core helpers
  - `schemas/` - request/response models

- `mobile/` - future mobile app client structure for Android/iOS
- `tests/` - automated test cases
- `.venv/` - Python virtual environment (created locally)
- `requirements.txt` - runtime Python dependencies

## Setup

1. Open the folder in VS Code.
2. Create and activate the virtual environment:
   - Windows PowerShell:
     ```powershell
     python -m venv .venv
     .\.venv\Scripts\Activate.ps1
     ```
3. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
4. Run the server:
   ```powershell
   uvicorn app.main:app --reload
   ```

## Notes

This is a foundation for an AI-enabled mobile app backend. The `mobile/` folder is ready for future Android and iOS code.
