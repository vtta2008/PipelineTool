# -*- coding: utf-8 -*-
"""

Script Name: localSQL.py
Author: Do Trinh/Jimmy - 3D artist.

Description:

"""
# -------------------------------------------------------------------------------------------------------------
from __future__ import absolute_import

""" Import """

# Python
import sqlite3 as lite
from appData                 import DB_PTH
from cores.base              import DAMG, DAMGLIST

# Plt
from utilities import utils as func

class QuerryDB(DAMGLIST):

    key = 'query db'
    conn = lite.connect(DB_PTH)
    cur = conn.cursor()

    def query_table(self, tn="curUser"):

        self.cur.execute("SELECT * FROM {0}".format(tn))

        data = self.cur.fetchall()

        return list(data[0])


class UpdateDB(DAMG):

    key = 'update db'
    conn = lite.connect(DB_PTH)
    cur = conn.cursor()

    def __init__(self, tableName="curUser", tableValue=[]):
        super(UpdateDB, self).__init__()
        if tableName == "curUser":
            self.update_curUser(tableValue)
        elif tableName == 'tmpConfig':
            self.update_tmpCfg(tableValue[0])

    def update_curUser(self, value):
        """ Update value of table curUser in local database """
        self.cur.execute("INSERT INTO curUser (username, token, cookie, remember) VALUES (?,?,?,?)", (value[0], value[1], value[2], value[3]))
        commit = self.conn.commit()
        return True

    def update_tmpCfg(self, value):
        """ Update temporary config """
        self.cur.execute("INSERT INTO curUser (username, token, cookie, remember) VALUES (?,?)", (value[0], value[1]))
        self.conn.commit()
        return True

class RemoveDB(DAMG):

    key = 'delete db'

    conn = lite.connect(DB_PTH)
    cur = conn.cursor()

    def __init__(self, tn="curUser"):
        super(RemoveDB, self).__init__()

        self.remove_data(tn)

    def remove_data(self, tn):
        self.cur.execute("SELECT * FROM {0}".format(tn))
        self.cur.fetchall()
        self.cur.execute("DELETE FROM {0}".format(tn))
        self.conn.commit()

class TimeLog(DAMG):

    key = 'timelog object'

    conn = lite.connect(DB_PTH)
    cur = conn.cursor()

    def __init__(self, details=None):
        super(TimeLog, self).__init__()

        self.username, token, cookie, remember = QuerryDB().query_table("curUser")
        self.time = func.getTime()
        self.date = func.getDate()
        self.details = details
        self.cur.execute("INSERT INTO timelog (username, time, date, details) VALUES (?,?,?,?)", (self.username, self.time, self.date, self.details))
        self.conn.commit()

# -------------------------------------------------------------------------------------------------------------
# Created by panda on 3/06/2018 - 3:58 AM
# Pipeline manager - DAMGteam