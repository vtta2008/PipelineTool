# -*- coding: utf-8 -*-
"""

Script Name: StyleSheet.py
Author: Do Trinh/Jimmy - 3D artist.

Description:

"""
# -------------------------------------------------------------------------------------------------------------
""" Import """

# Python
import os, platform

# PyQt5
from PyQt5.QtCore import QObject, QFile, QTextStream

# Plm
from appData import QSSDIR
from appData.Loggers import SetLogger
logger = SetLogger()

class StyleSheetManager(QObject):

    def __init__(self, style=None, parent=None):
        super(StyleSheetManager, self).__init__(parent)

        self.style = style
        if self.style == 'darkstyle':
            stylesheet = self.darkstyle()
        elif self.style == 'stylesheet':
            stylesheet = self.stylesheet()
        else:
            stylesheet = None

        self.changeStylesheet = stylesheet

    def darkstyle(self):
        from plg_ins import pyqt5_style_rc
        f = QFile(os.path.join(QSSDIR, 'darkstyle.qss'))
        stylesheet = self.load_stylesheet(f)
        return stylesheet

    def stylesheet(self):
        f = QFile(os.path.join(QSSDIR, 'stylesheet.qss'))
        stylesheet = self.load_stylesheet(f)
        return stylesheet

    def load_stylesheet(self, f):
        if not f.exists():
            logger.error('Unable to load stylesheet, file not found in resources')
            return ''
        else:
            f.open(QFile.ReadOnly | QFile.Text)
            ts = QTextStream(f)
            stylesheet = ts.readAll()
            if platform.system().lower() == 'darwin':  # see issue #12 on github
                mac_fix = '''
                QDockWidget::title
                {
                    background-color: #31363b;
                    text-align: center;
                    height: 12px;
                }
                '''
                stylesheet += mac_fix
            return stylesheet

StyleSheetManager()

# -------------------------------------------------------------------------------------------------------------
# Created by panda on 22/06/2018 - 3:51 AM
# © 2017 - 2018 DAMGteam. All rights reserved