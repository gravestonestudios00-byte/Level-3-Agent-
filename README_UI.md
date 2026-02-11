# Level3Agent UI

This build restores a simple UI so you can open the agent and type requests.

## Start (UI)
```powershell
python main.py
```
Or double-click:
`run_agent.bat`

## Start (CLI)
```powershell
python main.py --project-root "C:\path\to\project" --request "scan and report issues"
```

## API Keys
In the UI you can:
- Apply keys for current session
- Save to `.env` locally (kept next to main.py)
