def squares(n:int):
    i = 1
    while i <= n:
        yield i*i
        i += 1


for x in squares(5):
    print(x)