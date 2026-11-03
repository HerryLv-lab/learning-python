with open("output.txt","w",encoding="utf-8")as f:
    f.write("第一行：Python\n")
    f.write("第二行：从c转来\n")

with open("output.txt","r",encoding="utf-8")as f:
     for line in f:
        print(line.strip())
