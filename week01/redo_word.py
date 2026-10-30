# D2（10.30）：不看 01_word_count.py，重写词频统计
#
# 要求：
#   1. 用 input() 读入一句英文
#   2. 统计每个单词出现的次数（大小写不敏感）
#   3. 按次数从高到低排序
#   4. 输出形如：the->2 | dog->1
#
# 不许看 01_word_count.py。
# 卡住时先自己试：改一点、跑一下、看输出。

# 在下面开始写 ↓
seen = {}
sentence = input("请输入一句英语：")
for word in sentence.lower().split():
    if word in seen:
        seen[word] += 1
    else:
        seen[word] = 1
ordered = sorted(seen.items(), key = lambda x:x[1], reverse = True)
print(" | ".join(f"{w}->{i}" for w,i in ordered))
