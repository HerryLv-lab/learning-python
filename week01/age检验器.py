try:
    age = int(input())
    if age < 0 or age > 150:
        print("年龄不合法！")
    elif 0 <= age <= 150:
        print("你的年龄合法")
except ValueError:
    print("请输入数字")
