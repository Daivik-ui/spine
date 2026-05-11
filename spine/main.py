from cli.main import run_cli
from gui.app import run_gui
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: SPINE [cli|gui]")
        return

    command = sys.argv[1].lower()

    if command == "cli":
        run_cli()
    elif command == "gui":
        run_gui()
    else:
        print(f"Unknown command: {command}")
        print("Use: SPINE [cli|gui]")

if __name__ == "__main__":
    main()
