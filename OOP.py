#---Python OOP------

"""def hello():
    print("Hello")

x = 1
hello()
print(type(hello))
print(type(x))

string = "hello"
print(string.upper())"""

class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def add_one(self, x):
        return x + 1

    def bark(self):
        print("bark")

d = Dog("Tim", 24)
print(f'Dog info is: {d.get_name()} and {d.get_age()}')
d.set_age(56)
print(f'New Dog info is: {d.get_name()}, {d.get_age()}')