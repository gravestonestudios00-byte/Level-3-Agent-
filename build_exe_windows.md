# Build a Windows .exe (Level3Agent UI)

## 1) Install dependencies
In your venv:
```powershell
pip install -r requirements.txt
pip install pyinstaller
```

## 2) Build the UI exe (no console)
```powershell
pyinstaller --noconsole --onefile --name Level3Agent main.py
```

Output:
- `dist\Level3Agent.exe`

## 3) Debug build (console visible)
```powershell
pyinstaller --console --onefile --name Level3Agent main.py
```

## If the exe can't find config.yaml etc.
Use onedir:
```powershell
pyinstaller --noconsole --onedir --name Level3Agent main.py
```
