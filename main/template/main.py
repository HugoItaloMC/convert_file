class MainBox:

    def __init__(self, gui_engine):
        self.__gui_engine = gui_engine
        self.__LAYOUT: list = [
        [self.__gui_engine.Text("FILE CONVERSOR", justification='center', font=("Goto", 13))],
        [self.__gui_engine.Text("convert file to :", justification='center', font=("Goto", 11))],
        [self.__gui_engine.Text("_" * 50, justification='center')],
        [self.__gui_engine.Stretch(key=None),
        self.__gui_engine.Checkbox('EXCEL', font=("Sans-serif", 13), key='excel'),
        self.__gui_engine.Checkbox('CSV', font=("Sans-serif", 13), key='csv'),
        self.__gui_engine.Checkbox('JSON', font=("Sans-serif", 13), key='json'), self.__gui_engine.Stretch(key=None)],
        [self.__gui_engine.Text('_' * 50, justification='center')],
        [self.__gui_engine.Text('Open file to convert \nsupport files: (*.json, *.csv, *.xlsx, *.txt)', justification='center', font=("Goto", 15))],
        [self.__gui_engine.Stretch(),self.__gui_engine.Text("File from: ", size=(10, 1), auto_size_text=False, font=("Goto", 12)), 
        self.__gui_engine.InputText("path to open file", key='path', justification='left', size=(27, 1), font=("Goto", 15)), 
        self.__gui_engine.FileBrowse(), self.__gui_engine.Stretch(key=None)],
        [self.__gui_engine.Text("Save file in: ", justification="center", font=("Goto", 12)),
        self.__gui_engine.InputText("path file to save", key="file_path", font=("Goto", 10)),
        self.__gui_engine.FileSaveAs("Choice", key="output_path", file_types=(("csv", "*.csv"), ("xlsx", "*.xlsx"), ("json", "*.json"), ("txt", "*.txt")), font=("Goto", 11))],

        ]
    
    def get(self) -> list:
         
        return self.__LAYOUT
         
class SecondBox:

    def __init__(self, gui_engine):
        self.__gui_engine = gui_engine
        self.__LAYOUT: list = [[self.__gui_engine.Stretch(), self.__gui_engine.Multiline(size=(50, 10), key="data", disabled=False, autoscroll=True),
        self.__gui_engine.Stretch()],
        [self.__gui_engine.Stretch(key=None), self.__gui_engine.Button('start', size=(100, 30), key='start_task'), self.__gui_engine.Button('stop', size=(100, 30), key='stop'), self.__gui_engine.Stretch(key=None)]]
    
    def get(self) -> list:
        return self.__LAYOUT