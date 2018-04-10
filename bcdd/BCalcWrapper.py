'''
Wrapper class for libbcalcDDS.dll
'''

from ctypes import cdll

from .Exceptions import DllNotFoundException


class BCalcWrapper(object):

    DENOMINATIONS = [ 'C', 'D', 'H', 'S', 'N' ]
    PLAYERS = [ 'N', 'E', 'S', 'W' ]

    def __init__(self):
        try:
            self.libbcalcdds = cdll.LoadLibrary('./libbcalcdds.dll')
        except OSError:
            try:
                self.libbcalcdds = cdll.LoadLibrary('./libbcalcdds.so')
            except OSError:
                self.libbcalcdds = None
        if self.libbcalcdds is None:
            raise DllNotFoundException()

    def __getattr__(self, attrname):
        def _dynamic_method(*args):
            return getattr(self.libbcalcdds, 'bcalcDDS_' + attrname)(*args)
        return _dynamic_method

    def declarerToLeader(self, player):
        return (player + 1) % 4
