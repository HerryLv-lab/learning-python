import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 log_analyzer_v2.py log_file")
        return

    filename = sys.argv[1]
    info = 0
    warn = 0
    error = 0

    try:
        with open(filename,encoding="utf-8")as f:
            for line in f:
                if "INFO" in line:
                    info = info + 1
                elif "WARN" in line:
                    warn = warn + 1
                elif "ERROR" in line:
                    error = error + 1
    except FileNotFoundError:
        print("File not found")
        return

    print(f"INFO:{info},WARN:{warn},ERROR:{error}")

if __name__ == "__main__":
    main()

