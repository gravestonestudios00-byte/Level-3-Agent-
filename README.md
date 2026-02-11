# Level3Agent — Bezi-style UI build

## Start (UI)
```powershell
python main.py
```
or double-click:
`run_agent.bat`

## Key features
- Chat UI (back and forth messages)
- Project picker + Unity.exe auto-detect
- Auto-smoke checkbox (batch playtest)
- Bridge installer (recommended for playtest/scene tools)
- Per-response buttons:
  - Keep changes
  - Undo changes (restore from backup)
  - Restore this version

## CLI still works
```powershell
python main.py --cli --project-root "C:\path\to\project" --request "scan and report issues"
```

## Build an exe
See: `build_exe_windows.md`
