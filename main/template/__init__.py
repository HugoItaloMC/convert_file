import PySimpleGUIQt as pygui

from src.utils import *
from template.main import MainBox

__all__ = ['Template']

class Template:

    def __init__(self, schema) -> None:
        self.__schema: object = schema  # Data-classe, dados recebidos através do template
        
        self.__window_main: 'PySimpleGUIQt.Window' = None
        
    
    def __iter__(self) -> object:
        global tasks, factory, DataFrame
        
        # ENGINE INTERFACE GRAFICA
        if self.__window_main is None:
            self.__window_main = pygui.Window('Main Menu', MainBox(gui_engine=pygui).get(), finalize=True)
        
        else:
            self.__window_main.close()
        
        while True:
        
            # GLOBAL VAR
            factory = None
            tasks = None

            # CLASSES `Concrets`
            DataFrame = None

            # VERIFICANDO EVENTOS E DADOS
            event, values = self.__window_main.read()

            if event in (None, 'stop'):
                self.__window_main.close()
                exit(1)

            # BEGIN TEMPLATE
            if event == 'start_task':
                #self.__window_main.close()  # CLOSED MAIN WINDOW    
                # ENVIANDO DADOS    
                schema: Coroutine = iter(self.__schema(Request=(values['path'])))

                # BUSCANDO FACTORY
                factory = next(schema)
                schema.close()
                
                
                
                if factory is not None:
                   next(factory)
                
                try:
                    tasks = {key for key, _ in values.items() if type(_) is not str and _}
                    DataFrame = factory.send(bool(tasks))
                except Exception as err:
                    print(err)
                finally:
                    df = DataFrame.run().data
                    print(df)
                    factory.close()
            else:
                exit(1)
 
        return self
