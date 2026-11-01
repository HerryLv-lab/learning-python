with open("sample.log","r",encoding = "utf-8")as f:
    info = 0
    warn = 0
    error = 0
    for line in f:
        if "INFO" in line:
            info += 1
        elif "WARN" in line:
            warn += 1
        elif "ERROR" in line:
            error += 1
print(f"INFO:{info},WARN:{warn},ERROR:{error}")

