import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    '''Generates a random id'''
    return "".join(random.choices(string.ascii_lowercase, k=15))


def generate_login(name: str, surname: str) -> str:
    '''Generates a login based on the name and surname'''
    return "{0}{1}".format(name[0], surname[0:7])


@dataclass
class Student:
    '''A Student and its parameters'''
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False)

    def __post_init__(self):
        self.login = generate_login(self.name, self.surname)
        self.id = generate_id()
