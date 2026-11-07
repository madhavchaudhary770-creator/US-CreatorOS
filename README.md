# US CreatorOS

Local-first AI-assisted YouTube creator workspace for creators targeting US audiences.

## Included in this starter release
- FastAPI backend and responsive dashboard
- SQLite content project storage (create, list, update)
- Script fields and production status workflow
- Publishing policy endpoint: publishing disabled, private default, human approval required
- Configurable provider settings; paid-model use is off by default
- Windows setup script and automated API tests

## Windows quick start
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
uvicorn app.main:app --reload
```
Open http://127.0.0.1:8000. API docs: http://127.0.0.1:8000/docs

Run tests: `python -m pytest`

## Important
This is a functioning project-management MVP, not yet a finished autonomous video studio. AI research/generation, speech, media rendering, YouTube OAuth, uploads and analytics are separate integrations still to be implemented and tested. Never commit API keys or OAuth secrets. Publishing must remain human-approved and private by default. Verify licenses for every third-party asset and dependency.
