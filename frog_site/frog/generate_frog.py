from abc import ABC, abstractmethod
from .models import Frog
from random import choice, randint
from string import ascii_letters


def generate_title(len_text=0):
    return ''.join(choice((ascii_letters + '    ')) for i in range(len_text))


def generate_fake_frog():
    Frog.objects.create(title = generate_title(randint(3, 10)), content = generate_title(randint(20, 60)), honeytoken = True)
    return True

