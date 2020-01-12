# -*- coding: utf-8 -*-
"""

Script Name: urls.py
Author: Do Trinh/Jimmy - 3D artist.

Description:
    

"""
# -------------------------------------------------------------------------------------------------------------
from __future__ import absolute_import, unicode_literals
from __buildtins__ import globalSetting
""" Import """

# Python
import pprint

# PLM
from bin                            import DAMGDICT
from .metadatas                     import __plmWiki__

PYTHON_TAG                          = 'https://docs.anaconda.com/anaconda/reference/release-notes/'
LICENCE_TAG                         = 'https://github.com/vtta2008/damgteam/blob/master/LICENCE'
VERSION_TAG                         = 'https://github.com/vtta2008/damgteam/blob/master/bin/docs/rst/version.rst'

class ConfigUrl(DAMGDICT):

    key                             = 'ConfigUrl'

    def __init__(self):
        super(ConfigUrl, self).__init__()

        self.add('pythonTag', PYTHON_TAG)
        self.add('licenceTag', LICENCE_TAG)
        self.add('versionTag', VERSION_TAG)
        self.add('PLM wiki', __plmWiki__)

        if globalSetting.tracks.configInfo:
            if globalSetting.tracks.urlInfo:
                pprint.pprint(self)

# -------------------------------------------------------------------------------------------------------------
# Created by panda on 1/12/2020 - 3:44 PM
# © 2017 - 2019 DAMGteam. All rights reserved