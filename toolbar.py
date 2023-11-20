from PySide6.QtWidgets import QToolBar
from PySide6.QtGui import QIcon, QAction, QActionEvent
from PySide6.QtCore import QSize, Slot

class Pencil(QAction):
    def __init__(self, parent, func):
        super().__init__()
        self.selected = False
    
        self.setIcon(QIcon("C:\\Users\\ferna\\OneDrive\\Área de Trabalho\\Programação\\PixelEditor\\icons\\pencil.png"))
        self.setToolTip("Desenha um pixel na tela")
        self.triggered.connect(func)
        
    @Slot()
    def select(self):
        self.selected = True
    
    def isSelected(self):
        return self.selected

class Eraser(QAction):
    def __init__(self, parent, func):
        super().__init__(parent)
        self.selected = False
        
        self.setIcon(QIcon("C:\\Users\\ferna\\OneDrive\\Área de Trabalho\\Programação\\PixelEditor\\icons\\eraser.png"))
        self.setToolTip("Apaga um pixel")
        self.triggered.connect(func)
        
    @Slot()
    def select(self):
        self.selected = True
        
class ColorPicker(QAction):
    def __init__(self, parent, func):
        super().__init__(parent)
        self.selected = False
        
        self.setIcon(QIcon("C:\\Users\\ferna\\OneDrive\\Área de Trabalho\\Programação\\PixelEditor\\icons\\color-picker.png"))
        self.setToolTip("Seleciona a cor de um pixel")
        self.triggered.connect(func)
        
    @Slot()
    def select(self):
        self.selected = True

class ToolBar(QToolBar):
    """
    TODO: Fazer com que só seja possível utilizar uma ferramenta se ela estiver selecionada
    """
    def __init__(self, parent = None):
        super().__init__(parent)
        
        self.setStyleSheet("QToolBar { background-color: #73C7FF; }"
                            "QToolButton { width: 50px; height: 50px; border-radius: 5px; background-color: None;}"
                            "QToolButton:hover { background-color: #DAF0FF; }")
        
        self.setIconSize(QSize(35, 35))
        
        pencil = Pencil(self, Pencil.select) # type: ignore
        eraser = Eraser(self, Eraser.select)
        colorPicker = ColorPicker(self, ColorPicker.select)
        
        self.addAction(pencil) # Adiciono à barra de ferramentas o lápis
        self.addAction(eraser) # Adiciono à barra de ferramentas a borracha
        self.addAction(colorPicker) # Adiciono à barra de ferramentas o color picker
                
    # def tool(self, event):
    #     actualTool = event.__name__()
    #     return actualTool
