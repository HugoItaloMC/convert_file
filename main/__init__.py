from collections import namedtuple
from src import *
__all__ = ['Schema']


class Schema:
    # Client Data-Class
    def __init__(self, Request = namedtuple("Request", ("path")), ):
        self.__Request: tuple = Request
        self.__facade = iter(Facade(args=self.__Request))
    
    def __iter__(self):
        yield next(self.__facade)
        raise StopIteration