import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QWidget
import qdarkstyle
from toolbar import Pencil, ToolBar
from menubar import MenuBar
from PySide6.QtGui import QFont
from drawBoard import DrawBoard


# Classe da janela principal
class MainWindow(QMainWindow):
    def __init__(self,parent = None, flags = Qt.WindowType.FramelessWindowHint) -> None:
        super().__init__(parent, flags)
        
        self.InitUI() # Chamo o construtor da UI no construtor da função para a UI ser construída sem preciar chamar a função depois de instanciar a classe
        
    def InitUI(self):        
        self.resize(QApplication.primaryScreen().size().width(), QApplication.primaryScreen().size().height()) # Redimensiono a janela
        self.setWindowTitle("Sprite Editor") # Título da janela
        self.drawArea = QHBoxLayout() # Crio o layout para a area de desenho
        
        pencil = Pencil()
        drawBoard = DrawBoard(pencil)
        self.drawArea.addWidget(drawBoard)
        
        drawBoardContainer = QWidget()
        drawBoardContainer.setLayout(self.drawArea)
        
        self.setCentralWidget(drawBoardContainer)
        
        menuBar = MenuBar() # Crio o menu
        self.setMenuBar(menuBar) # Defino uma barra de menu pra nossa janela e passo o menubar criado na linha anterior
        
        toolBar = ToolBar(self) # Instancio a classe da barra/Crio a barra
        self.addToolBar(Qt.ToolBarArea.RightToolBarArea, toolBar) # Coloco a barra de ferramentas na esquerda da tela

        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv) # Crio o app
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyside6()) # Ativo o darkmode
    app.setFont(QFont("Pixelify Sans", 16))

    window = MainWindow() # Crio a janela
    
    sys.exit(app.exec()) # Executo o app