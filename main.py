
import os, sys
from pathlib import Path

# Ensure the app works whether run as python or packaged exe
if getattr(sys, 'frozen', False):
    ROOT = Path(sys.executable).resolve().parent
else:
    ROOT = Path(__file__).resolve().parent

os.chdir(ROOT)
sys.path.insert(0, str(ROOT))

def main():
    try:
        # Try UI first
        from src.agent.ui_bezi import Level3BeziUI
        app = Level3BeziUI()
        app.mainloop()
    except Exception as e:
        print("Failed to start UI:", e)
        input("Press Enter to exit...")

if __name__ == "__main__":
    main()
