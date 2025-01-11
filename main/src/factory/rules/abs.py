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
            if self._path.endswith(".xlsx"):  
                self.data = self._pd.read_excel(self._path)

            elif self._path.endswith(".csv"):
                self.data = self._pd.read_csv(self._path, tab="\t")

            elif self._path.endswith(".json"):
                self.data = self._pd.read_json(self._path)
            
            elif self._path.endswith(".txt"):
                self.data = self._pd.read_csv(self._path, tab="\t")

            else:
                raise ValueError("Not found or file not allowed %s " % self._path)

            -self
        else:
            +self
            ~self
            raise StopIteration

