# -*- coding: utf-8 -*-
"""

Script Name: PLM.py
Author: Do Trinh/Jimmy - 3D artist.

Description:
    This script is master file of Pipeline Manager

"""
# -------------------------------------------------------------------------------------------------------------
from __future__ import absolute_import, unicode_literals
from __buildtins__ import globalSetting
# -------------------------------------------------------------------------------------------------------------
""" import """

# Python
import os, sys, requests

# PLM
from appData                            import __localServer__, SYSTRAY_UNAVAI, SERVER_CONNECT_FAIL, KEY_RELEASE
from utils                              import LocalDatabase, clean_file_ext
from ui.SplashUI                        import SplashUI
from ui.assets                          import ThreadManager, LayoutManager
from plugins.Browser                    import Browser
from devkit.Application                 import Application

# -------------------------------------------------------------------------------------------------------------
""" Operation """

class DAMGTEAM(Application):

    key                                 = 'PLM'

    def __init__(self):
        Application.__init__(self)

        splash                          = SplashUI(self)
        self.plmInfo                    = splash.plmInfo
        self.appInfo                    = splash.appInfo

        self.browser                    = Browser()
        self.database                   = LocalDatabase()

        self.threadManager              = ThreadManager()
        self.layoutManager              = LayoutManager(self.threadManager, self)

        self.layoutManager.registLayout(self.browser)
        self.layoutManager.buildLayouts()
        self.layoutManager.globalSetting()

        self.mainUI, self.sysTray, self.shortcutCMD, self.signIn, self.signUp, self.forgotPW = self.layoutManager.mains
        self.layouts                    = self.layoutManager.register

        for layout in [self.mainUI, self.sysTray, self.signIn, self.signUp, self.forgotPW]:
            layout.signals._emitable    = True
            layout.signals.connect('loginChanged', self.loginChanged)

        self.set_styleSheet('dark')

        try:
            r = requests.get(__localServer__)
        except requests.exceptions.ConnectionError:
            self.logger.info('Cannot connect to server')
            connectServer = False
        else:
            connectServer = True

        try:
            self.username, token, cookie, remember = self.database.query_table('curUser')
        except (ValueError, IndexError):
            self.logger.info("There is no user login data")
            self.username, token, cookie, remember = (None, None, None, None)
            queryUserLogin = False
        else:
            queryUserLogin = True

        if queryUserLogin:
            if connectServer:
                try:
                    r = requests.get(__localServer__, verify=False, headers={'Authorization': 'Bearer {0}'.format(token)}, cookies={'connect.sid': cookie})
                except Exception:
                    if not globalSetting.modes.allowLocalMode:
                        self.messageBox(self, 'Connection Failed', 'critical', SERVER_CONNECT_FAIL, 'close')
                        sys.exit()
                    else:
                        self.sysNotify('Offline', 'Can not connect to Server', 'crit', 500)
                        self.mainUI.show()
                        splash.finish(self.mainUI)
                else:
                    if r.status_code == 200:
                        if not self.sysTray.isSystemTrayAvailable():
                            self.logger.report(SYSTRAY_UNAVAI)
                            self.exitEvent()
                        else:
                            self.loginChanged(True)
                            self.sysTray.log_in()
                            self.mainUI.show()
                            splash.finish(self.mainUI)
                    else:
                        self.signIn.show()
                        splash.finish(self.signIn)
            else:
                if not globalSetting.modes.allowLocalMode:
                    self.messageBox(self, 'Connection Failed', 'critical', SERVER_CONNECT_FAIL, 'close')
                    sys.exit()
                else:
                    self.sysNotify('Offline', 'Can not connect to Server', 'crit', 500)
                    self.mainUI.show()
                    splash.finish(self.mainUI)
        else:
            if connectServer:
                self.signIn.show()
                splash.finish(self.signIn)
            else:
                if not globalSetting.modes.allowLocalMode:
                    self.messageBox(self, 'Connection Failed', 'critical', SERVER_CONNECT_FAIL, 'close')
                    sys.exit()
                else:
                    self.sysNotify('Offline', 'Can not connect to Server', 'crit', 500)
                    self.mainUI.show()
                    splash.finish(self.mainUI)

    def notify(self, receiver, event):

        if event.type() == KEY_RELEASE:
            if event.key() == 16777249 and 32:
                pos = self.cursor.pos()
                self.shortcutCMD.show()
                self.shortcutCMD.move(pos)

        elif event.type() == 18:                                            # QHideEvent
            if hasattr(receiver, 'key'):
                if self.layoutManager:
                    if receiver.key in self.layouts.keys():
                        geometry = receiver.saveGeometry()
                        receiver.setValue('geometry', geometry)

        elif event.type() == 17:                                            # QShowEvent
            if hasattr(receiver, 'key'):
                if self.layoutManager:
                    if receiver.key in self.layoutManager.keys():
                        geometry = receiver.settings.value('geometry', b'')
                        receiver.restoreGeometry(geometry)

        return super(DAMGTEAM, self).notify(receiver, event)

    def command(self, key):
        try:
            cmdData = self.plmInfo[key]
        except KeyError:
            return print('There is no key: {0}'.format(key))

        print(cmdData.code, cmdData.value)

        if cmdData.code == 'os.startfile':
            func = os.startfile
            arg = cmdData.value
        elif cmdData.code == 'os.system':
            func = os.system
            arg = cmdData.value
        elif cmdData.code == 'showUI':
            func = self.showUI
            arg = cmdData.key
        elif cmdData.code == 'openURL':
            func = self.openURL
            arg = cmdData.value
        elif cmdData.code == 'shortcut':
            func = self.shortcut
            arg = cmdData.value
        elif cmdData.code == 'appEvent':
            func = self.appEvent
            arg = cmdData.key
        elif cmdData.code == 'stylesheet':
            func = self.changeStyleSheet
            arg = cmdData.value
        else:
            if cmdData.value == 'CleanPyc':
                func = clean_file_ext
                arg = 'py'
            elif cmdData.value == 'Debug':
                func = self.mainUI.botTabUI.botTab2.test
                arg = None
            elif cmdData.value == 'Restore':
                func = self.mainUI.showNormal
                arg = None
            elif cmdData.value == 'Maximize':
                func = self.mainUI.showMaximized
                arg = None
            elif cmdData.value == 'Minimize':
                func = self.mainUI.showMinimized
                arg = None
            elif cmdData.value in ['Organisation', 'Project', 'Team', 'Task']:
                func = self.showUI
                arg = '{0}Manager'.format(cmdData.value)
            else:
                func = print
                arg = key

        if arg is None:
            return func()
        else:
            return func(arg)

    def appEvent(self, event):
        if event == 'ShowAll':
            self.showAll()
        elif event == 'CloseAll':
            self.closeAll()
        elif event == 'HideAll':
            self.hideAll()
        elif event == 'SwitchAccount':
            self.switchAccountEvent()
        elif event == 'LogIn':
            self.signInEvent()
        elif event == 'LogOut':
            self.signOutEvent()
        elif event == 'Quit':
            self.quit()
        elif event == 'Exit':
            self.exit()
        elif event == 'ChangePassword':
            pass
        else:
            pass

    def showUI(self, key):
        try:
            ui = self.layouts[key]
        except KeyError:
            return print('There is no layout: {0}'.format(key))
        else:
            return ui.show()

    def openURL(self, url):
        self.browser.setUrl(url)
        self.browser.update()
        self.browser.show()

    def loginChanged(self, val):
        self._login = val

        if not self._login:
            self.mainUI.close()
        else:
            self.mainUI.show()
            for layout in [self.signIn, self.signUp, self.forgotPW]:
                layout.close()

        self.sysTray.loginChanged(self._login)
        self.signIn.loginChanged(self._login)
        self.signUp.loginChanged(self._login)

        return self._login

    def showAll(self):
        for ui in self.layouts.values():
            ui.show()

    def closeAll(self):
        for ui in self.layouts.values():
            ui.close()

    def hideAll(self):
        return self.closeAll()

    def signInEvent(self):
        self.switchAccountEvent()

    def signOutEvent(self):
        self.loginChanged(False)
        self.signIn.show()
        for layout in [self.mainUI, self.signUp, self.forgotPW] + self.layoutManager.infos + \
                      self.layoutManager.setts + self.layoutManager.tools + self.layoutManager.prjs:
            layout.hide()

    def signUpEvent(self):
        self.loginChanged(False)
        self.signUp.show()
        for layout in [self.mainUI, self.signUp, self.forgotPW] + self.layoutManager.infos + \
                      self.layoutManager.setts + self.layoutManager.tools + self.layoutManager.prjs:
            layout.hide()

    def sysNotify(self, *arg):
        title, mess, iconType, timeDelay = arg
        return self.sysTray.sysNotify(title, mess, iconType, timeDelay)

    def switchAccountEvent(self):
        self.signOutEvent()

if __name__ == '__main__':
    app = DAMGTEAM()
    app.startLoop()

# -------------------------------------------------------------------------------------------------------------
# Created by panda on 19/06/2018 - 2:26 AM
# © 2017 - 2019 DAMGteam. All rights reserved