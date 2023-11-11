from PySide6.QtWidgets import QGraphicsView, QGraphicsScene, QWidget
from PySide6.QtGui import QPainter, QPaintEvent, QMouseEvent, QPen, QColor, QImage, QResizeEvent
from PySide6.QtCore import QPoint, Qt
from toolbar import Pencil, Eraser, ColorPicker

class DrawBoard(QWidget):
    def __init__(self, pencil):
        super().__init__()
        self.pencil = pencil
        
        self.pixels = []
        self.pixelSize = 10
        self.drawing = False
        self.image = QImage(self.size(), QImage.Format.Format_RGB32) # type: ignore
        self.image.fill(QColor("#19233e")) # type: ignore
        
        self.scene = QGraphicsScene()
        self.view = QGraphicsView()
    
    def mousePressEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.LeftButton and self.pencil.isSelected(): # type: ignore
            self.drawing = True
            self.pixels.append(QPoint(round(event.position().x() / self.pixelSize) * self.pixelSize, round(event.position().y() / self.pixelSize) * self.pixelSize))
            
            return super().mousePressEvent(event)
    
    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        if self.drawing and event.buttons() and self.pencil.isSelected(): # type: ignore
            self.pixels.append(QPoint(round(event.position().x() / self.pixelSize) * self.pixelSize, round(event.position().y() / self.pixelSize) * self.pixelSize))
            self.update()
            
            return super().mouseMoveEvent(event)
        
    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.LeftButton: # type: ignore
            self.drawing = False
        
            return super().mouseReleaseEvent(event)
    
    def paintEvent(self, event: QPaintEvent) -> None:
        painter = QPainter(self.image)
        painter.setPen(QPen(QColor("black"), self.pixelSize, Qt.SolidLine)) # type: ignore
        
        canvasPainter = QPainter(self)
        
        for pixel in self.pixels:
            painter.drawPoint(pixel)
        
        canvasPainter.drawImage(self.rect(), self.image, self.image.rect())
        
        return super().paintEvent(event)
    
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