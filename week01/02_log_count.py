total = 0
errors = 0
with open("sample.log",encoding="utf-8")as f:
    for line in f:
        total += 1
        if "ERROR" in line:
            errors += 1
            print(line.strip())
#print(total)
#print(errors)
print(f"总行数{total}\nERROR{errors}行")