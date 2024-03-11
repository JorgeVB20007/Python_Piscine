from abc import ABC, abstractmethod


class Character(ABC):
    '''Character Class. It has a first_name and a is_alive variable.'''
    @abstractmethod
    def __init__(self, _first_name: str, _is_alive=True):
        '''Constructor that takes either one or two parameters'''
        self.first_name = _first_name
        self.is_alive = _is_alive

    def die(self):
        '''Sets _is_alive to 0'''
        self.is_alive = False


class Stark(Character):
    '''Character Class. Inherits from Character.'''
    def __init__(self, _first_name: str, _is_alive=True):
        '''Constructor that takes either one or two parameters'''
        super().__init__(_first_name, _is_alive)
