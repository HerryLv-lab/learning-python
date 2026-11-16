def timer(func):
    def wrapper():
        print("开始")
        func()
        print("结束")
    return wrapper
@timer
def work():
    print("work")



work()