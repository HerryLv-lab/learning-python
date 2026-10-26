# W1（10.26–11.01）用 Python 重写 3 个 C 程序

## 三个练习

1. **字符串处理**：统计一段文本里每个单词出现的次数（C 里要手写哈希表或数组，Python 一个 `dict` 搞定）
2. **文件 IO**：读一个日志文件，按行解析、筛选出含关键字的行、统计条数
3. **控制台交互**：一个命令行小计算器，支持 + - * / 和退出

## 重点体会这些差异

| C 里要手写 | Python 里是什么 |
|---|---|
| `malloc` / `free` | 不用管，自动回收 |
| 数组 + 长度变量 | `list`，自带 `append` / `len` |
| 手写哈希表 | `dict` |
| `strlen` / `strcpy` / `strcmp` | `len()` / `=` / `==` |
| `printf("%d")` | f-string：`f"{x}"` |
| 编译再运行 | 直接 `python x.py` |

## 提交检查点

做完三个练习，跑通，然后：

```bash
git add .
git commit -m "W1: 用 Python 重写 3 个 C 程序"
git push
```

## 顺手做

LeetCode 第 1 题「两数之和」，用 Python 写，放 `../leetcode/0001_two_sum.py`。
