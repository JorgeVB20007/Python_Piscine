class calculator:
    '''It's a calculator which is in a class.'''
    def __init__(self, thelist):
        '''It's a calculator which is in a class.'''
        self.vector = thelist

    def __add__(self, object) -> None:
        '''haha vector goes a+b'''
        try:
            self.vector = [item + object for item in self.vector]
            print(self.vector)
        except Exception:
            print("Exception Found")

    def __mul__(self, object) -> None:
        '''haha vector goes a*b'''
        try:
            self.vector = [item * object for item in self.vector]
            print(self.vector)
        except Exception:
            print("Exception Found")

    def __sub__(self, object) -> None:
        '''haha vector goes a-b'''
        try:
            self.vector = [item - object for item in self.vector]
            print(self.vector)
        except Exception:
            print("Exception Found")

    def __truediv__(self, object) -> None:
        '''haha vector goes a/b'''
        try:
            assert object != 0, "AssertionError: Tried to divide by 0"
        except AssertionError as msg:
            print(msg)
            return
        try:
            self.vector = [item / object for item in self.vector]
            print(self.vector)
        except Exception:
            print("Exception Found")
