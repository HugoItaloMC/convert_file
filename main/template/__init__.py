import PySimpleGUIQt as pygui

from src.utils import *
from template.main import MainBox, SecondBox

__all__ = ['Template']

class Template:

    def __init__(self, schema) -> None:
        self.__schema: object = schema  # Data-classe, dados recebidos através do template
        
        self.__window_main: 'PySimpleGUIQt.Window' = None
        
    
    def __iter__(self) -> object:
        global tasks, factory, DataFrame
        
        # ENGINE INTERFACE GRAFICA
        if self.__window_main is None:
            main_layout = [
                [pygui.TabGroup([
                    [pygui.Tab('Main', MainBox(gui_engine=pygui).get()),
                    pygui.Tab('Data', SecondBox(gui_engine=pygui).get())]
                ],
                key='tab_group', enable_events=True)]
                ]
            self.__window_main = pygui.Window('Manager Files', main_layout)
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

            if event in 'stop':
                self.__window_main.close()
                exit(1)

            # BEGIN TEMPLATE
            if event == "tab_group":
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
                    self.__window_main['data'].update(df.head())
                    factory.close()
            else:
                exit(1)
 
        return self
