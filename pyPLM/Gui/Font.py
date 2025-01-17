# -*- coding: utf-8 -*-
"""

Script Name: Font.py
Author: Do Trinh/Jimmy - 3D artist.

Description:

"""
# -------------------------------------------------------------------------------------------------------------
""" Import """

from PySide2.QtGui                 import QFont


class Font(QFont):

    Type                                = 'DAMGFONT'
    key                                 = 'Font'
    _name                               = 'DAMG Font'

    def __init__(self, *__args):
        super(Font, self).__init__(*__args)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, newName):
        self._name                      = newName

# -------------------------------------------------------------------------------------------------------------
# Created by panda on 3/12/2019 - 3:25 AM
# © 2017 - 2018 DAMGteam. All rights reserved