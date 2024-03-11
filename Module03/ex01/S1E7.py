from S1E9 import Character


class Baratheon(Character):
    '''IDK I don't speak GoT, but this is the Baratheon class'''
    def __init__(self, _first_name: str, _is_alive=True):
        '''Constructor that takes either one or two parameters'''
        super().__init__(_first_name, _is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    @classmethod
    def create_baratheon(self, _first_name: str, _is_alive=True):
        '''Creates a Baratheon'''
        return self(_first_name, _is_alive)

    def __str__(self):
        '''Sets the str so the class is printable'''
        return str("Vector: ('{0}', '{1}', '{2}')".format(
            self.family_name, self.eyes, self.hairs))

    def __repr__(self):
        '''Sets the repr so the class is printable'''
        return str("Vector: ('{0}', '{1}', '{2}')".format(
            self.family_name, self.eyes, self.hairs))


class Lannister(Character):
    '''IDK I don't speak GoT, but this is the Lannister class'''
    def __init__(self, _first_name: str, _is_alive=True):
        '''Constructor that takes either one or two parameters'''
        super().__init__(_first_name, _is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    @classmethod
    def create_lannister(self, _first_name: str, _is_alive=True):
        '''Creates a Lannister'''
        return self(_first_name, _is_alive)

    def __str__(self):
        '''Sets the str so the class is printable'''
        return str("Vector: ('{0}', '{1}', '{2}')".format(
            self.family_name, self.eyes, self.hairs))

    def __repr__(self):
        '''Sets the repr so the class is printable'''
        return str("Vector: ('{0}', '{1}', '{2}')".format(
            self.family_name, self.eyes, self.hairs))
