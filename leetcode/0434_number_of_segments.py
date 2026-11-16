def count_words(s:str) -> int:
    return len(s.split())



print(count_words("Hello, my name is John"))  # 5
print(count_words("   "))  # 0
print(count_words("a b  c"))  # 3
print(count_words(""))  # 0
print(count_words("one"))  # 1
    