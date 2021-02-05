class MyClass():
    """ MyClass description"""
    attr = 100

    def __init__(self, init_attr=None):
        if init_attr is None:
            self.attr = MyClass.attr
        else:
            self.attr = init_attr

    def change_attr(self, new_attr):
        self.attr = new_attr


print(MyClass.attr)
a = MyClass(120)
b = MyClass(110)
c = MyClass()
print(MyClass.attr)
print(a.attr)
print(b.attr)
print(c.attr)
a.change_attr(125)
MyClass.attr = 200
print(MyClass.attr)
print(a.attr)
print(b.attr)
print(c.attr)
