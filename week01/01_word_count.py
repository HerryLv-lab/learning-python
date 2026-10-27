sentence = input("请输入一句英语")
counts = {}
for word in sentence.lower().split():
    if word in counts :
        counts[word] +=1
    else:
        counts[word] = 1
pairs = sorted(counts.items(),key = lambda x:x[1],reverse = True)
print("|".join(f"{w} {n}"for w,n in pairs))

