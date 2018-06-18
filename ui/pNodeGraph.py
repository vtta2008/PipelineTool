# -*- coding: utf-8 -*-
"""

Script Name: NoderViewer.py
Author: Do Trinh/Jimmy - 3D artist.

Description:

"""
# -------------------------------------------------------------------------------------------------------------
""" Import """

# Python
import sys

import qdarkgraystyle

# PyQt5
from PyQt5.QtCore import pyqtSignal, QRectF
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QMenu, QGraphicsScene, QMenuBar
from PyQt5.QtGui import QIcon, QColor, QFont

# Plt
import appData as app
from utilities import utils as func

from appData._pNN import *

from ui.pNode import pNode
from ui.pView import pView

# -------------------------------------------------------------------------------------------------------------
""" Configure the current level to make it disable certain log """

logger = app.logger

# -------------------------------------------------------------------------------------------------------------
""" Variables """

# -------------------------------------------------------------------------------------------------------------
""" NoderViewer """

class pScene(QGraphicsScene):

    def __init__(self, parent=None):
        super(pScene, self).__init__(parent)

        self.setSceneRect(0, 0, 100, 30)

class pMenuBar(QMenuBar):

    def __init__(self, parent=None):
        super(pMenuBar, self).__init__(parent)

        self.fm = QMenu('File')
        self.fm.addMenu(QMenu('New Scene'))
        self.fm.addMenu(QMenu('New Node'))

        self.addSeparator()

        self.addMenu(self.fm)
        self.addMenu(QMenu('Tools'))
        self.addMenu(QMenu('Nodes'))

    def createNode(self):
        pass

    def regisNode(self):
        pass

class pNodeGraph(QWidget):

    def __init__(self, parent=None):
        super(pNodeGraph, self).__init__(parent)

        self.setWindowTitle("Scenegraph PLM")
        self.setWindowIcon(QIcon(func.getLogo(32, 'Logo')))

        self.menuBar = pMenuBar(self)

        self.scene = pScene()
        self.view = pView()
        self.view.setScene(self.scene)
        self.view.setRenderHint(ANTIALIAS)
        self.view.setViewportUpdateMode(FULLVIEWUPDATE)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.view)
        self.setLayout(self.layout)

        self.pNodes = []

        node1 = pNode("Node 1")
        node1.setPos(0, 0)

        node2 = pNode("Node 2")
        node2.setPos(20, 20)


        self.scene.addItem(node1)
        self.scene.addItem(node2)

        self.resize(1000, 500)

    def clearScene(self):
        pass

    def addSceneMenuAction(self, menu):
        pass

    def loadScene(self):
        pass

    def mergeScene(self):
        pass

    def storeCurrentScene(self):
        pass

    def keyPressEvent(self, event):
        if event.key() == DELKEY:
            selectedNodes = [i for i in self.scene.selectedItems() if isinstance(i, pNode)]
            for node in selectedNodes:
                node.destroy()
        super(pNodeGraph, self).keyPressEvent(event)

    def contextMenuEvent(self, event):
        pass

    def resizeEvent(self, event):
        print(self.width(), self.height())

def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkgraystyle.load_stylesheet())
    layout = pNodeGraph()
    layout.show()
    app.exec_()


if __name__ == '__main__':
    main()

# -------------------------------------------------------------------------------------------------------------
# Created by panda on 17/06/2018 - 1:45 PM
# © 2017 - 2018 DAMGteam. All rights reserved