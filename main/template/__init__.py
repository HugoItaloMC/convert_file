import PySimpleGUIQt as pygui

from src.utils import *
from template.main import MainBox, SecondBox

__all__ = ['Template']


# helpers
def clear_frame(df):
    return df.fillna('XXXX')


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
        
        # BEGIN TEMPLATE
        while True:
        
            # GLOBAL VAR
            factory = None
            tasks = None

            # CLASSES `Concrets`
            DataFrame = None

            # VERIFICANDO EVENTOS E DADOS
            event, values = self.__window_main.read()

            if event in ('stop', pygui.WIN_CLOSED):
                self.__window_main.close()
                exit()


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
                    DataFrame = factory.send(tasks)
                except Exception as err:
                    print(err)

                df = DataFrame.run().data
                self.__window_main['data'].update(df.head())
                clear_frame(df)
                
                if 'csv' in tasks and values['file_path'].endswith(".csv"):
                    df.to_csv(values['file_path'], index=False)
                    
                elif 'json' in tasks and values['file_path'].endswith('.json'):
                    df.to_json(values['file_path'], orient="records", lines=True)
                    
                elif 'excel' in tasks and values['file_path'].endswith('.xlsx'):
                    df.to_excel(values['file_path'], index=False)

            else:
                continue
                                        

 
        return self
