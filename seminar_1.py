#how to create object

# example 1
# наследование
# A- класс-родитель

import sys
from PyQt5 import QtGui, QtCore, QtWidgets
import numpy as np


class Example(QtWidgets.QWidget):

    def __init__(self, parent):
        super(Example, self).__init_(parent)

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Hello')

    def paintEvent(self, event):
        qp = QtGui.QPainter()
        qp.begin(self)
        r = self.rect().adjusted(5,5,-5,-5)
        qp.drawrect(r)

        pen = QtGui.QPen(QtGui.QColor(150,40,120),3)
        brush = QtGui.QBrush(QtCore.Qt.green)
        qp.setPen(pen)
        qp.setBrush(brush)


        qp.end