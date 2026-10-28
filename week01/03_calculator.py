def main():
    print("简易计算机，支持 + - * / 四则运算，输入 quit 退出")
    while True:
        expr = input("请输入算式：")
        expr = expr.strip()
        if expr == "quit":
            print("已退出计算机")
            break

        try:
            parts = expr.split()
            num1 = float(parts[0])
            num2 = float(parts[2])
            op =  parts[1]
            if op =="/" and num2 == 0:
                print("错误：除数不能为零")
                continue
            if op == "+":
                result = num1 + num2
            elif op == "-":
                result = num1 - num2
            elif op == "*":
                result = num1 * num2
            elif op == '/':
                result = num1 / num2
            else:
                print("不支持的运算符，只能输入 + - * /")
                continue
            print(f"结果：{result}")

        except(IndexError,ValueError):
            print("输入格式错误，请按'数字 运算符 数字'的格式输入，例如 3 + 5")

if __name__ == "__main__":
    main()