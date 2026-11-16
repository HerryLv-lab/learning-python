def is_anagram(s:str,t:str) -> bool:
    if len(s)!=len(t):
        return False
    counts = {}
    for ch in s:
        if ch in counts:
            counts[ch] += 1
        else:
            counts[ch] = 1

    for ch in t:
        if ch not in counts:
            return False
        counts[ch] -= 1

    for ch in counts:
        if counts[ch] != 0:
            return False
    return True
print(is_anagram("anagram","nagaram"))
print(is_anagram("rat","car"))
print(is_anagram("a","a"))
print(is_anagram("ab","ab"))
print(is_anagram("aacc","ccac"))
