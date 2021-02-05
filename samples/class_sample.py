class MyClass():
    """ MyClass description"""
    attr = 100

    def __init__(self, init_attr=None):
        if init_attr is None:
            self.attr = MyClass.attr
        else:
            self.attr = init_attr

    def change_attr(self, new_attr, second_attr):
        self.attr = new_attr
        self.second_attr = self.__add(second_attr)

    def __add(self, added):
        return added + self.attr


print(MyClass.attr)
a = MyClass(120)
b = MyClass(110)
c = MyClass()
print(MyClass.attr)
print(a.attr)
print(b.attr)
print(c.attr)
a.change_attr(new_attr=125, second_attr=2000)
MyClass.attr = 200
print(MyClass.attr)
print(a.attr, a.second_attr)
print(b.attr)
print(c.attr)
print(c._MyClass__add(100))
