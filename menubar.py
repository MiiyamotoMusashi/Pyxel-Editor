from PySide6.QtWidgets import QMenuBar, QMenu
from PySide6.QtGui import QAction

class FileMenu(QMenu):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.setTitle("File")
        
        _open = Open(self)
        save = Save(self)
        saveAs = SaveAs(self)
        
        self.addActions([_open, save, saveAs])

class Open(QAction):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.setText("Open")

class Save(QAction):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.setText("Save")
        
class SaveAs(QAction):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.setText("Save As")
        
class MenuBar(QMenuBar):
    """
    Todo: Colocar uma opção de alterar a fonte do programa
    """
    def __init__(self, parent = None):
        super().__init__(parent)
        
        self.setStyleSheet("QMenuBar { background-color: #73C7FF; }"
                           "QToolButton { width: 50px; height: 25px; background-color: #73C7FF; color: #000000; font-size: 18px; }"
                           "QToolButton:hover { background-color: #DAF0FF }")
        
        # Menu chamado FILE e seus ACTIONS
        file_menu = self.addMenu(FileMenu(self))