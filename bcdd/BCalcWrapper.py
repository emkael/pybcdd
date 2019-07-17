'''
Wrapper class for libbcalcDDS.dll
'''

from ctypes import cdll, c_void_p

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
            function = getattr(self.libbcalcdds, 'bcalcDDS_' + attrname)
            if attrname == 'new':
                function.restype = c_void_p
            else:
                function.argtypes = [c_void_p]
            return function(*args)
        return _dynamic_method

    def declarerToLeader(self, player):
        return (player + 1) % 4
