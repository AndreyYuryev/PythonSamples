class Person:
    name = 'Test'
    age = 30

if __name__ == '__main__':
    print(Person.name)
    print(setattr(Person, 'X', 100))
    print(Person.X)
    print(Person.__dict__)
    del Person.X
    print(Person.__dict__)