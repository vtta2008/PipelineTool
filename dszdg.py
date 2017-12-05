try:
    from __version__ import __version__
except ImportError:
    # Version file has not been autogenerated from build process:
    __version__ = None

from PySide.QtCore import qInstallMsgHandler


def _message_handler(type, message):
    """Handle qt warnings etc with an exception, so they don't pass
    unnoticed"""
    print '%s: %s' % (type, message)
    # raise Exception('%s: %s'%(type,message))


qInstallMsgHandler(_message_handler)
del qInstallMsgHandler

from locking import qtlock

qtlock.enforce()

from qsettings_wrapper import QSettingsWrapper
from UiLoader import UiLoader