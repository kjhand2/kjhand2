.global your_asm_fn
.section .text

your_asm_fn:

push	%ebp
mov	%esp,%ebp

push %eax

lea first, %eax
push %eax
push second
push third

call practice

add $12, %esp
pop %eax

leave
ret

first:	.long 0xc001f00d
second:	.long 0x00c105ed
third:	.long 0xacce55ed
