# A Python array is as lean as a C array
from array import array
from random import random

floats = array('d', (random() for i in range(10**7))) #d means double-precision floats 
floats[-1]
fp = open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()
floats2 = open('floats.bin', 'rb')
floats2.fromfile(fp, 10**7)
fp.close()
floats2[-1]
if floats == floats:
    print("True --")