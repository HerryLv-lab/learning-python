while True:
    exgr = input("计算机支持，+-*/,请输入算式，例如，2 * 5\n")
    if exgr == "quit":
        break
    try:
        parts = exgr.split()
        number1 = float(parts[0])
        number2 = float(parts[2])
        op = parts[1]
        if exgr == "quit":
            break
        if op == "/" and number2 == 0.0:
            print("分母不能为零")
            continue

        if op == "+":
            number = number1 + number2
        elif op == "-":
             number = number1 - number2
        elif op == "*":
             number = number1 * number2
        elif op == "/":
             number = number1 / number2
        else:
            print("只支持+-*/")
            continue
        print(f"{number}")
    except(IndexError,ValueError):
        print("格式不对，请按 数字 运算符 数字 输入")


