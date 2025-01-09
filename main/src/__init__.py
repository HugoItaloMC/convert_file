from src.factory import *
__all__ = ['Facade']

class Facade:
    #  Chama factory

    def __init__(self, args: str):
        self.__args: str = args
        self.__factory: object = iter(Factory(path=self.__args))
    
    def __iter__(self):
        yield self.__factory
        raise StopIteration