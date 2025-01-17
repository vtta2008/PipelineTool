# -*- coding: utf-8 -*-
"""

Script Name: Polygon.py
Author: Do Trinh/Jimmy - 3D artist.

Description:
    

"""
# -------------------------------------------------------------------------------------------------------------
""" Import """


from PySide2.QtGui                          import QPolygon


class Polygon(QPolygon):

    Type                                = 'DAMGPOLYGON'
    key                                 = 'Polygon'
    _name                               = 'DAMG Polygon'

    def __init__(self, *__args):
        super(Polygon, self).__init__(*__args)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, newName):
        self._name                      = newName

# -------------------------------------------------------------------------------------------------------------
# Created by panda on 5/4/2020 - 6:34 PM
# © 2017 - 2019 DAMGteam. All rights reserved