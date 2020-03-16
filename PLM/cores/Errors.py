# -*- coding: utf-8 -*-
"""

Script Name: Errors.py
Author: Do Trinh/Jimmy - 3D artist.

Description:

"""
# -------------------------------------------------------------------------------------------------------------
""" Import """

# PLM
from PLM.commons import DAMGERROR


class NodePropertyError(DAMGERROR): pass


class NodeWidgetError(DAMGERROR): pass


class NodeRegistrationError(DAMGERROR): pass


class PortRegistrationError(DAMGERROR): pass


class NodeMenuError(DAMGERROR): pass


class IconNotFound(DAMGERROR): pass


class ActionKeyConfigError(DAMGERROR): pass


class ActionRegisterError(DAMGERROR): pass


class ButtonRegisterError(DAMGERROR): pass


class ToolbarNameError(DAMGERROR): pass


# -------------------------------------------------------------------------------------------------------------
# Created by panda on 4/12/2019 - 1:22 AM
# © 2017 - 2018 DAMGteam. All rights reserved