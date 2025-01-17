# -*- coding: utf-8 -*-
"""

Script Name: sqlPreset.py
Author: Do Trinh/Jimmy - 3D artist.

Description:

"""
# -------------------------------------------------------------------------------------------------------------
""" Import """

# Python
import re
import sqlite3 as lite

from pyPLM.damg import DAMG

from PLM import LOCAL_DB, METADATA, __version__


# -------------------------------------------------------------------------------------------------------------
""" Resource database """

TN  = ['curUser'     , 'userTokenLogin', 'timelog' , 'tmpConfig', 'metadata', ]                   # Table name

MTN = ['organisation', 'application'   , 'domain'  , 'version'  , 'display' , 'author', ]         # Metadata name
IDN = ['id'          , 'userid'        , 'tokenid' , 'pcid'     , ]                               # ID name
CTN = ['username'    , 'token'         , 'cookie'  , 'remember' , 'details' , ]                   # Common name
TCN = ['date'        , 'time'          , 'datetime', ]                                            # Time column name
CCN = ['lastConfig'  , 'curSettingPth' , ]                                                        # Config column name

IDA = ['INTEGER PRIMARY KEY AUTOINCREMENT, ', 'INT PRIMARY KEY, ', ]                              # ID attribute
CTA = ['TEXT NOT NULL, '                    , 'TEXT, '           , 'BOOL, '  , ]                  # Common attribute
STA = ['VACHAR(20,) '                       , 'VARCHAR, '        , ]                              # String attribute

CC = "CREATE TABLE IF NOT EXISTS "                                                                # Create table

# Attribute preset
ATD = dict( id            = IDA[0], userid = IDA[1], tokenid  = IDA[0], pcid     = IDA[0], username     = CTA[0],
            token         = CTA[1], cookie = CTA[1], remember = CTA[2], details  = CTA[1], lastConfig   = STA[1],
            curSettingPth = CTA[1], date   = CTA[1], time     = CTA[1], datetime = CTA[1], organisation = CTA[0],
            application   = CTA[0], domain = CTA[0], version  = CTA[0], display  = CTA[0], author       = CTA[0], )

# Local table details
LTD = dict(
            curUser         = [CTN[0], CTN[1], CTN[2], CTN[3], ],
            userTokenLogin  = [IDN[2], CTN[0], CTN[1], TCN[2], ],
            timelog         = [CTN[0], TCN[1], TCN[0], CTN[4], ],
            tmpConfig       = [CCN[0], CCN[1], ],
            metadata        = MTN
)

# -------------------------------------------------------------------------------------------------------------
""" Create database """



with open(METADATA, 'rb') as f:
    metadata = f.read().decode('utf-8')


def parse(pattern):
    return re.search(pattern, metadata).group(1).replace('"', '').strip()



class PresetDB(DAMG):

    key = "PresetDB"
    conn = lite.connect(LOCAL_DB)
    cur = conn.cursor()

    def __init__(self):
        super(PresetDB, self).__init__()

        for tn in TN:
            self.create_table(tn)

        orgname = parse(r'__organization__\s+=\s+(.*)')
        appname = parse(r'__appname__\s+=\s+(.*)')
        domain = parse(r'__homepage__\s+=\s+(.*)')
        version = __version__
        author = parse(r'__author__\s+=\s+(.*)')
        display = parse(r'__appname__\s+=\s+(.*)')

        self.cur.execute("SELECT * FROM metadata")
        self.cur.fetchall()
        self.cur.execute("DELETE FROM metadata")
        self.cur.execute("INSERT INTO metadata ('organisation', 'application', 'domain', 'version', 'display', 'author') VALUES (?,?,?,?,?,?)",
                         (orgname, appname, domain, version, display, author))
        self.conn.commit()
        self.conn.close()

    def generate_command(self, tn = TN[0]):
        cl = LTD[tn]
        cmd = ""
        for i in range(len(cl)):
            cmd += cl[i] + " " + ATD[cl[i]]
        cmd = cmd[:-2]
        return cmd

    def create_table(self, tn = TN[0]):
        print('create table: {0}'.format(tn))
        cmd = self.generate_command(tn)
        self.cur.execute("CREATE TABLE IF NOT EXISTS `{0}` ({1})".format(tn, cmd))
        self.conn.commit()

PresetDB()

# -------------------------------------------------------------------------------------------------------------
# Created by panda on 3/06/2018 - 3:58 AM
# Pipeline manager - DAMGteam