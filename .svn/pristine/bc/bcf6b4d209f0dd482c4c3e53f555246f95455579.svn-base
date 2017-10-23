.global _main
.section .text

_main:

push	%ebp
mov	%esp,%ebp
pusha

xor %eax, %eax
add $11, %eax

xor %edx, %edx

push %edx
push $0x68732f6e
push $0x69622f2f	#push //bin/sh on backwards

mov %esp, %ebx		#point ebx to //bin/sh

push %edx		#push on another NULL

mov %esp, %edx

push %ebx		#addr of //bin/sh

mov %esp, %ecx

int $0x80

add $24, %esp

popa
leave
ret

