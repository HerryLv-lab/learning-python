class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def introduce(self):
        return f"我叫{self.name},今年{self.age}岁"
s = Student("xiaoming",18)
print(s.introduce())
