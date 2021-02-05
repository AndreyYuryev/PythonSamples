

class GrandParent():
    def __init__(self):
        pass

    def hi_there_grand_parent(self):
        print('GrandParent')


class ParentA(GrandParent):
    def __init__(self):
        pass

    def hi_there_parent(self):
        print('ParentA')


class ParentB():
    def __init__(self):
        pass

    def hi_there(self):
        print('ParentB')


class ChildA(ParentA, ParentB):
    def __init__(self):
        pass

    def new_hi_there(self):
        self.hi_there()


a = ChildA()
a.new_hi_there()
