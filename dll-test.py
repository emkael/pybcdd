from bcdd.BCalcWrapper import BCalcWrapper
from ctypes import *

bc = BCalcWrapper()
solver = bc.new(b"PBN", b"N:.63.AKQ987.A9732 A8654.KQ5.T.QJT6 J973.J98742.3.K4 KQT2.AT.J6542.85", 0, 0)
print(solver)
print(c_char_p(bc.getLastError(solver)))
print(bc.getTricksToTake(solver))
