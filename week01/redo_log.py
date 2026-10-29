# D1（10.29）：不看 02_log_count.py，重写日志统计
#
# 要求：
#   1. 打开 sample.log
#   2. 数出总行数
#   3. 数出 ERROR 行数
#   4. 输出一行：总行数 15，ERROR 4 行
#
# 这四步在 02 里都写过，这次唯一的区别是不许看原文件。
# 想不起来就自己想，或者改一点跑一遍看效果。

# 在下面开始写 ↓
with open("sample.log",encoding="utf-8")as f:
    total = 0
    errors = 0
    for line in f:
        total += 1
        if "ERROR" in line:
            errors += 1
    print(f"总行数{total},error{errors}行")