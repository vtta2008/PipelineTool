# -*- coding: utf-8 -*-
"""

Script Name: ThreadPool.py
Author: Do Trinh/Jimmy - 3D artist.

Description:
    

"""
# -------------------------------------------------------------------------------------------------------------

import time

from PLM                                    import __copyright__

from PyQt5.QtCore                           import QThreadPool

from .Runnable                              import Runnable
from .Thread                                import Thread


class ThreadPool(QThreadPool):

    Type                                    = 'DAMGTHREADPOOL'
    key                                     = 'BaseThreadPool'
    _name                                   = 'DAMG Thread Pool'
    _copyright                              = __copyright__()


    def __init__(self, parent=None):
        QThreadPool.__init__(self)

        self.parent                         = parent

    @property
    def copyright(self):
        return self._copyright

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        self._name                          = val

# -------------------------------------------------------------------------------------------------------------
# Created by panda on 3/20/2020 - 8:06 AM
# © 2017 - 2019 DAMGteam. All rights reserved