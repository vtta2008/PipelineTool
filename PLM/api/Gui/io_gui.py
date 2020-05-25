# -*- coding: utf-8 -*-
"""

Script Name: 
Author: Do Trinh/Jimmy - 3D artist.

Description:


"""
# -------------------------------------------------------------------------------------------------------------
""" Import """
from PLM import qtBinding


if qtBinding == 'PyQt5':
    from PyQt5.QtGui        import ( QBrush, QColor, QCursor, QFont, QFontDatabase, QFontMetrics, QIcon, QImage,
                                     QKeySequence, QPaintDevice, QPainter, QPainterPath, QPalette, QPen, QPixmap,
                                     QPolygon, QTransform, QTextTableFormat, QTextCharFormat, QIntValidator,
                                     QWheelEvent)
elif qtBinding == 'PySide2':
    from PySide2.QtGui      import ( QBrush, QColor, QCursor, QFont, QFontDatabase, QFontMetrics, QIcon, QImage,
                                     QKeySequence, QPaintDevice, QPainter, QPainterPath, QPalette, QPen, QPixmap,
                                     QPolygon, QTransform, QTextTableFormat, QTextCharFormat, QIntValidator,
                                     QWheelEvent)



# -------------------------------------------------------------------------------------------------------------
# Created by Trinh Do on 5/6/2020 - 3:13 AM
# © 2017 - 2020 DAMGteam. All rights reserved