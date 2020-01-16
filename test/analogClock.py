# -*- coding: utf-8 -*-
"""

Script Name: analogClock.py
Author: Do Trinh/Jimmy - 3D artist.

Description:

"""
# -------------------------------------------------------------------------------------------------------------
from __future__ import absolute_import, unicode_literals

from PyQt5.QtCore import (pyqtProperty, pyqtSignal, pyqtSlot, QPoint, QSize, Qt, QTime, QTimer)
from PyQt5.QtGui import QBrush, QColor, QPainter, QPen, QPolygon
from PyQt5.QtWidgets import QApplication, QWidget


class PyAnalogClock(QWidget):

    timeChanged = pyqtSignal(QTime)
    timeZoneChanged = pyqtSignal(int)

    def __init__(self, parent=None):

        super(PyAnalogClock, self).__init__(parent)

        self.timeZoneOffset = 0

        timer = QTimer(self)
        timer.timeout.connect(self.update)
        timer.timeout.connect(self.updateTime)
        timer.start(1000)

        self.setWindowTitle("Analog Clock")
        self.resize(200, 200)

        self.hourHand = QPolygon([ QPoint(7, 8), QPoint(-7, 8), QPoint(0, -40)])
        self.minuteHand = QPolygon([QPoint(7, 8), QPoint(-7, 8), QPoint(0, -70)])
        self.hourColor = QColor(0, 127, 0)
        self.minuteColor = QColor(0, 127, 127, 191)

    def paintEvent(self, event):

        side = min(self.width(), self.height())
        time = QTime.currentTime()
        time = time.addSecs(self.timeZoneOffset * 3600)

        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.translate(self.width() / 2, self.height() / 2)
        painter.scale(side / 200.0, side / 200.0)

        painter.setPen(Qt.NoPen)
        painter.setBrush(QBrush(self.hourColor))

        painter.save()
        painter.rotate(30.0 * ((time.hour() + time.minute() / 60.0)))
        painter.drawConvexPolygon(self.hourHand)
        painter.restore()

        painter.setPen(self.hourColor)

        for i in range(0, 12):
            painter.drawLine(88, 0, 96, 0)
            painter.rotate(30.0)

        painter.setPen(Qt.NoPen)
        painter.setBrush(QBrush(self.minuteColor))

        painter.save()
        painter.rotate(6.0 * (time.minute() + time.second() / 60.0))
        painter.drawConvexPolygon(self.minuteHand)
        painter.restore()

        painter.setPen(QPen(self.minuteColor))

        for j in range(0, 60):
            if (j % 5) != 0:
                painter.drawLine(92, 0, 96, 0)
            painter.rotate(6.0)

        painter.end()

    def minimumSizeHint(self):

        return QSize(50, 50)

    def sizeHint(self):
        return QSize(100, 100)

    def updateTime(self):
        self.timeChanged.emit(QTime.currentTime())

    def getTimeZone(self):
        return self.timeZoneOffset

    @pyqtSlot(int)
    def setTimeZone(self, value):
        self.timeZoneOffset = value
        self.timeZoneChanged.emit(value)
        self.update()

    def resetTimeZone(self):
        self.timeZoneOffset = 0
        self.timeZoneChanged.emit(0)
        self.update()

    timeZone = pyqtProperty(int, getTimeZone, setTimeZone, resetTimeZone)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    clock = PyAnalogClock()
    clock.show()
    sys.exit(app.exec_())

# -------------------------------------------------------------------------------------------------------------
# Created by panda on 6/11/2019 - 1:38 AM
# © 2017 - 2018 DAMGteam. All rights reserved