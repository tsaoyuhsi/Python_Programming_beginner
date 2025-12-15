class Person:
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID

    def greet(self):
        print(f"你好，我是 {self.name},  學號{self.ID}")

p = Person("Tom",12)
p.greet(
