from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    '''King class. Inherits from Baratheon and Lannister'''
    def __init__(self, _first_name: str, _is_alive=True):
        '''Constructor'''
        super().__init__(_first_name, _is_alive)

    def set_eyes(self, _color: str):
        '''Sets the eyes'''
        self.eyes = _color

    def set_hairs(self, _color: str):
        '''Sets the "hAiRs"'''
        self.hairs = _color

    def get_eyes(self) -> str:
        '''Gets the eyes'''
        return self.eyes

    def get_hairs(self) -> str:
        '''Gets the "hAiRs"'''
        return self.hairs
