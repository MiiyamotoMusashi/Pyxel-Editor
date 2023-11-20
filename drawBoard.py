from PySide6.QtWidgets import QGraphicsView, QGraphicsScene, QWidget
from PySide6.QtGui import QPainter, QPaintEvent, QMouseEvent, QPen, QColor, QImage, QResizeEvent
from PySide6.QtCore import QPoint, Qt

class DrawBoard(QWidget):
    """
    TODO: Centralizar o campo de desenho
    TODO: Fazer com que seja possível dar e tirar zoom
    """
    
    def __init__(self):
        super().__init__()
                
        self.pixels = [] # Lista para armazenar cada posição de um pixel
        self.pixelSize = 10 # Tamanho do pixel
        self.drawing = False # Variável para controlar se o usuário está desenhando
        self.image = QImage(self.size(), QImage.Format.Format_RGB32) # Objeto onde os pixels serão desenhados                                      type: ignore 
        self.image.fill(QColor("#19233e")) # type: ignore
        
        # self.scene = QGraphicsScene()
        # self.view = QGraphicsView()
    
    def mousePressEvent(self, event: QMouseEvent) -> None: # Esse evento é chamado quando o mouse é pressionado
        if event.button() == Qt.LeftButton: # Se o botão pressionado for o esquerdo                                                                   type: ignore
            self.drawing = True
            self.pixels.append(QPoint(round(event.position().x() / self.pixelSize) * self.pixelSize, round(event.position().y() / self.pixelSize) * self.pixelSize)) # Adiciono a posição do mouse a lista de pixels
            self.update() # Atualizo o widget para ser redesenhado com o pixel
            
            return super().mousePressEvent(event)
    
    def mouseMoveEvent(self, event: QMouseEvent) -> None: # Esse evento é chamado quando o mouse é pressionado
        if self.drawing and event.buttons(): # Se o usuário estiver desenhando e pressionando um botão                                                type: ignore
            self.pixels.append(QPoint(round(event.position().x() / self.pixelSize) * self.pixelSize, round(event.position().y() / self.pixelSize) * self.pixelSize))
            self.update()# Atualizo o widget para ser redesenhado com o pixel
            
            return super().mouseMoveEvent(event)
        
    def mouseReleaseEvent(self, event: QMouseEvent) -> None: # Esse evento é disparado quando o usuário "solta" um botão
        if event.button() == Qt.LeftButton: # Se o botão que não está mais pressionado é o esquerdo                                                                                                      type: ignore
            self.drawing = False # Ele para de desenhar
        
            return super().mouseReleaseEvent(event)
    
    def paintEvent(self, event: QPaintEvent) -> None: # Evento que desenha as coisas na tela
        painter = QPainter(self.image) # Criando o pintor que vai pintar na imagem
        painter.setPen(QPen(QColor("black"), self.pixelSize, Qt.SolidLine)) # Definindo uma caneta para o pintor                                                                  type: ignore
        
        canvasPainter = QPainter(self) # Criando o pintor que vai pintar a imagem na janela
        
        # Pra cada posição/pixel na lista de pixels o pintor da imagem desenha um ponto nela
        for pixel in self.pixels:
            painter.drawPoint(pixel)
        
        canvasPainter.drawImage(self.rect(), self.image, self.image.rect()) # O pintor da janela deseha a imagem com os pixels na tela
        
        return super().paintEvent(event)
    
    # Evento para ajustar o tamanho do widget
    def resizeEvent(self, event: QResizeEvent) -> None:
        if self.width() > self.image.width() or self.height() > self.image.height():
            self.resize(self.image.width(), self.image.height())
        
        return super().resizeEvent(event)
    
    # def resizeEvent(self, event):
    #     if self.width() > self.image.width() or self.height() > self.image.height():
    #         newImage = QImage(max(self.width(), self.image.width()), max(self.height(), self.image.height()), QImage.Format.Format_RGB32)
    #         newImage.fill(Qt.white)
    #         painter = QPainter(newImage)
    #         painter.drawImage(QPoint(), self.image)
    #         self.image = newImage
    #     super().resizeEvent(event)