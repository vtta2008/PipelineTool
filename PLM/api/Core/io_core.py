# -*- coding: utf-8 -*-
"""

Script Name: 
Author: Do Trinh/Jimmy - 3D artist.

Description:


"""
# -------------------------------------------------------------------------------------------------------------
""" Import """
from PLM import glbSettings


if glbSettings.qtBinding == 'PyQt5':
    from PyQt5.QtCore           import (QObject, QByteArray, QDate, QDateTime, QEventLoop, QFile, QFileInfo, QIODevice,
                                        QPoint, QProcess, QRect, QRectF, QRunnable, QSettings, QSize, QTextStream, QThread,
                                        QThreadPool, QTime, QTimer, QTimeZone, QUrl, Qt, )
elif glbSettings.qtBinding == 'PySide2':
    from PySide2.QtCore         import (QObject, QByteArray, QDate, QDateTime, QEventLoop, QFile, QFileInfo, QIODevice,
                                        QPoint, QProcess, QRect, QRectF, QRunnable, QSettings, QSize, QTextStream, QThread,
                                        QThreadPool, QTime, QTimer, QTimeZone, QUrl, Qt, )


# -------------------------------------------------------------------------------------------------------------
# Created by Trinh Do on 5/6/2020 - 3:13 AM
# © 2017 - 2020 DAMGteam. All rights reserved