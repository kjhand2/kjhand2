.global your_asm_fn
.section .text

your_asm_fn:

push	%ebp
mov	%esp,%ebp

push %eax

push $0x80c5b68
lea closed, %eax
push %eax
push $0xacce55ed


call practice

add $12, %esp

pop %eax
leave
ret

closed: .long 0x00c105ed
