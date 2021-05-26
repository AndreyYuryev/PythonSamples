

class RequestNumber():
    def __init__(self):
        self.number = str()

    def is_exist(self):
        if self.number is None:
            return False
        elif self.number == '':
            return False
        else:
            return True
