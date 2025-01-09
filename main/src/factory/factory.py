from src.factory.rules import * 
__all__ = ['AbstractFactory']

# AbstractFactory instância classes Concretas que herdam de classes Abstratas contendo tarefas solicitadas
class AbstractFactory:
    # Refrênciando classes concretas em atributos  métodos

   def data_frame(self, path: str):
    return ConcretDataFrame(path=path) 
    