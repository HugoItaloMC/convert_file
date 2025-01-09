# MY IMPORTS
from src.factory.core import *
__all__ = ["AbstractDataFrame"]

# Classes Abstratas
class AbstractDataFrame(Handler):

    def __init__(self, path: str):
        super().__init__()
        self._path: str = path
        self.data = None
    
    
    def __next__(self):
        +self
        while self._exit > 0:
            if self._path:  
                self.data = self._pd.read_excel(self._path)
            -self
        else:
            +self
            ~self
            raise StopIteration
