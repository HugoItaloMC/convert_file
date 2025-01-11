from src.factory.factory import *
__all__ = ['Factory']

class Factory(AbstractFactory):
    #  Factory, classe concreta de AbstractFactory 
    # acessa classes Concretas através de métodos
    def __init__(self, path: str):

        self._path = path

    
    def __iter__(self):
        yield
        xbool: bool = yield self.data_frame(path=self._path)
        raise StopIteration
        

        