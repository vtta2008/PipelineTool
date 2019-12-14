# -*- coding: utf-8 -*-
"""

Script Name: path.py
Author: Do Trinh/Jimmy - 3D artist.

Description:

"""
# -------------------------------------------------------------------------------------------------------------
""" Import """

# Python
import os

# PLM
from .metadatas             import __envKey__

cfgdir                      = 'applocal'
# cfgdir                      = 'appdata'

# -------------------------------------------------------------------------------------------------------------
""" Directory system """

PROGRAM86                   = os.getenv('PROGRAMFILES(X86)')
PROGRAM64                   = os.getenv('PROGRAMW6432')
LOCALAPPDATA                = os.getenv('LOCALAPPDATA')
USERAPPDATA                 = os.getenv('APPDATA')
PROGRAMDATA                 = os.getenv('PROGRAMDATA')
DESKTOP_DIR                 = os.path.join(os.environ["HOMEPATH"], "desktop")

# -------------------------------------------------------------------------------------------------------------
""" Directory PLM """
ROOT_DIR                    = os.path.join(os.getenv(__envKey__))

APP_DATA_DIR                = os.path.join(ROOT_DIR, 'appData')
DB_DIR                      = APP_DATA_DIR
RAWS_DATA_DIR               = os.path.join(APP_DATA_DIR, 'raws')
DOCUMENTATION_DIR           = os.path.join(APP_DATA_DIR, 'documentations')
TMP_DIR                     = os.path.join(APP_DATA_DIR, '.tmp')

if cfgdir == 'applocal':
    CFG_DIR                 = os.path.join(APP_DATA_DIR, '.config')
elif cfgdir == 'appdata':
    CFG_DIR                 = os.path.join(USERAPPDATA, '.config')
else:
    CFG_DIR                 = APP_DATA_DIR

SETTING_DIR                 = CFG_DIR
LOG_DIR                     = CFG_DIR
TASK_DIR                    = os.path.join(CFG_DIR, 'task')
TEAM_DIR                    = os.path.join(CFG_DIR, 'team')
ORG_DIR                     = os.path.join(CFG_DIR, 'organisation')
CFG_DAMG_DIR                = os.path.join(ORG_DIR, 'damgteam')

PRJ_DIR                     = os.path.join(CFG_DIR, 'project')
CFG_PLM_DIR                 = os.path.join(PRJ_DIR, 'plm')

CACHE_DIR                   = os.path.join(CFG_DIR, '.cache')
CFG_NODE_DIR                = CFG_DIR
CFG_PREF_DIR                = CFG_DIR
CFG_USER_DIR                = CFG_DIR

BIN_DIR                     = os.path.join(ROOT_DIR, 'bin')
DATA_DIR                    = os.path.join(BIN_DIR, 'data')
DEPENDANCIES_DIR            = os.path.join(BIN_DIR, 'dependencies')
RESOURCES_DIR               = os.path.join(BIN_DIR, 'resources')
SOUND_DIR                   = os.path.join(BIN_DIR, 'sound')

BUILD_DIR                   = os.path.join(ROOT_DIR, 'build')
CORES_DIR                   = os.path.join(ROOT_DIR, 'cores')

HOOK_DIR                    = os.path.join(ROOT_DIR, 'devHook')
MAYA_DIR                    = os.path.join(HOOK_DIR, 'Maya')
MARI_DIR                    = os.path.join(HOOK_DIR, 'Mari')
NUKE_DIR                    = os.path.join(HOOK_DIR, 'Nuke')
ZBRUSH_DIR                  = os.path.join(HOOK_DIR, 'ZBrush')
HOUDINI_DIR                 = os.path.join(HOOK_DIR, 'Houdini')

IMG_DIR                     = os.path.join(ROOT_DIR, 'imgs')
AVATAR_DIR                  = os.path.join(IMG_DIR, 'avatar')
PIC_DIR                     = os.path.join(IMG_DIR, 'pics')

STYLE_DIR                   = os.path.join(IMG_DIR, 'styles')
STYLE_IMAGE_DIR             = os.path.join(STYLE_DIR, 'images')
STYLE_RC_DIR                = os.path.join(STYLE_DIR, 'rc')
STYLE_SVG_DIR               = os.path.join(STYLE_DIR, 'svg')

TAG_DIR                     = os.path.join(IMG_DIR, 'tags')
MAYA_ICON_DIR               = os.path.join(IMG_DIR, 'maya')
NODE_ICON_DIR               = os.path.join(IMG_DIR, 'node')

APP_ICON_DIR                = os.path.join(IMG_DIR, 'icons')
ICON_DIR_12                 = os.path.join(APP_ICON_DIR, 'x12')
ICON_DIR_16                 = os.path.join(APP_ICON_DIR, 'x16')
ICON_DIR_24                 = os.path.join(APP_ICON_DIR, 'x24')
ICON_DIR_32                 = os.path.join(APP_ICON_DIR, 'x32')
ICON_DIR_48                 = os.path.join(APP_ICON_DIR, 'x48')
ICON_DIR_64                 = os.path.join(APP_ICON_DIR, 'x64')

LOGO_DIR                    = os.path.join(IMG_DIR, 'logo')
DAMG_LOGO_DIR               = os.path.join(LOGO_DIR, 'DAMGTEAM')
PLM_LOGO_DIR                = os.path.join(LOGO_DIR, 'PLM')

WEB_ICON_DIR                = os.path.join(IMG_DIR, 'web')
WEB_ICON_16                 = os.path.join(WEB_ICON_DIR, 'x16')
WEB_ICON_24                 = os.path.join(WEB_ICON_DIR, 'x24')
WEB_ICON_32                 = os.path.join(WEB_ICON_DIR, 'x32')
WEB_ICON_48                 = os.path.join(WEB_ICON_DIR, 'x48')
WEB_ICON_64                 = os.path.join(WEB_ICON_DIR, 'x64')
WEB_ICON_128                = os.path.join(WEB_ICON_DIR, 'x128')

PLUGIN_DIR                  = os.path.join(ROOT_DIR, 'plugins')
NODE_GRAPH_DIR              = os.path.join(PLUGIN_DIR, 'NodeGraph')

SCRIPTS_DIR                 = os.path.join(ROOT_DIR, 'scripts')
QSS_DIR                     = os.path.join(SCRIPTS_DIR, 'qss')
JSON_DIR                    = os.path.join(SCRIPTS_DIR, 'json')
RCS_DIR                     = os.path.join(SCRIPTS_DIR, 'rcs')
SCSS_DIR                    = os.path.join(SCRIPTS_DIR, 'scss')

TEST_DIR                    = os.path.join(ROOT_DIR, 'test')

TOOLKIT_DIR                 = os.path.join(ROOT_DIR, 'toolkits')
CORE_DIR                    = os.path.join(TOOLKIT_DIR, 'Core')
GUI_DIR                     = os.path.join(TOOLKIT_DIR, 'Gui')
WIDGETS_DIR                 = os.path.join(TOOLKIT_DIR, 'Widgets')

UI_DIR                      = os.path.join(ROOT_DIR, 'ui')
UI_BASE_DIR                 = os.path.join(UI_DIR, 'base')


FOOTER_DIR                  = os.path.join(UI_DIR, 'Footer')
BODY_DIR                    = os.path.join(UI_DIR, 'Body')
TABS_DIR                    = os.path.join(BODY_DIR, 'Tabs')
HEADER_DIR                  = os.path.join(UI_DIR, 'Header')


SUBUI_DIR                   = os.path.join(UI_DIR, 'SubUi')
FUNCS_DIR                   = os.path.join(SUBUI_DIR, 'Funcs')
PROJECT_DIR                 = os.path.join(SUBUI_DIR, 'Projects')
SETTINGS_DIR                = os.path.join(SUBUI_DIR, 'Settings')
TOOLS_DIR                   = os.path.join(SUBUI_DIR, 'Tools')

UTILS_DIR                   = os.path.join(ROOT_DIR, 'utils')


# -------------------------------------------------------------------------------------------------------------
# Created by panda on 3/06/2018 - 10:45 PM
# Pipeline manager - DAMGteam
