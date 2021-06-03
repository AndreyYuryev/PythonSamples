class OldClass:
    pass

class NewClass(object):
    pass


if __name__ == '__main__':
    print(OldClass.__class__)
    print(NewClass.__class__)
    print(type(OldClass))
    print(type(NewClass))