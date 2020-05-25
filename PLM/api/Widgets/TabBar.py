# -*- coding: utf-8 -*-
"""

Script Name: TabBar.py
Author: Do Trinh/Jimmy - 3D artist.

Description:

"""
# -------------------------------------------------------------------------------------------------------------

from .io_widgets import QTabBar


class TabBar(QTabBar):

    Type                                    = 'DAMGUI'
    key                                     = 'TabBar'
    _name                                   = 'DAMG Tab Bar'

    def __init__(self, parent=None):
        super(TabBar, self).__init__(parent)
        self.parent                         = parent

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, newName):
        self._name                      = newName

# -------------------------------------------------------------------------------------------------------------
# Created by panda on 27/10/2019 - 4:39 PM
# © 2017 - 2018 DAMGteam. All rights reserved