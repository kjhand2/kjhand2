import sys,io,math,os
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Util.number import bytes_to_long, inverse
import struct
import re
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5
# Our "MPI" format consists of 4-byte integer length l followed by l bytes of binary key
def int_to_mpi(z):
    s = int_to_binary(z)
    return struct.pack('I',len(s))+s

# Horrible hack to get binary representation of arbitrary-length long int
def int_to_binary(z):
    s = ("%x"%z); s = (('0'*(len(s)%2))+s).decode('hex')
    return s

def bits_to_mpi(s):
    return struct.pack('I',len(s))+s

def parse_mpi(s,index):
    length = struct.unpack('<I',s[index:index+4])[0]
    z = long(s[index+4:index+4+length].encode('hex'),16)
    return z, index+4+length

def parse_bits(s,index):
    length = struct.unpack('<I',s[index:index+4])[0]
    return s[index+4:index+4+length],index+4+length

encrypt_header = '-----BEGIN PRETTY BAD ENCRYPTED MESSAGE-----\n'
encrypt_footer = '-----END PRETTY BAD ENCRYPTED MESSAGE-----\n'

# PKCS 7 pad message.
def pad(s,blocksize=AES.block_size):
    n = blocksize-(len(s)%blocksize)
    return s+chr(n)*n

def unpad(msg):
    n = ord(msg[-1])
    return msg[:-n]

# Encrypt string s using RSA encryption with AES in CBC mode.
# Generate a 256-bit symmetric key, encrypt it using RSA with PKCS1v1.5 padding, and prepend the MPI-encoded RSA ciphertext to the AES-encrypted ciphertext of the message.
def encrypt(rsakey,s):
    aeskey = Random.new().read(32)

    pkcs = PKCS1_v1_5.new(rsakey)
    output = bits_to_mpi(pkcs.encrypt(aeskey))
    
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(aeskey, AES.MODE_CBC, iv)

    output += iv + cipher.encrypt(pad(s))
    return encrypt_header + output.encode('base64') + encrypt_footer


def decrypt(rsakey,c):
    data = re.search(encrypt_header+"(.*)"+encrypt_footer,c,flags=re.DOTALL).groups()[0].decode('base64')
    rsam,index = parse_bits(data,0)

    cipher = PKCS1_v1_5.new(rsakey)
    sentinel = 'error'
    aeskey = cipher.decrypt(rsam,sentinel)
    if aeskey == sentinel:
        raise ValueError

    iv = data[index:index+AES.block_size]
    cipher = AES.new(aeskey,AES.MODE_CBC,iv)
    plain = unpad(cipher.decrypt(data[index+AES.block_size:]))

    return plain
#do multiplication
def gcd(x,y):
	return abs(x) if y ==0 else gcd(y,x%y)

ans = open("sol_1.2.4.txt","w")
RSAmod = open("mp1/moduli.hex","rb")
sol = open("sol_1.2.4.txt","w")
inCiph = open("1.2.4_ciphertext.enc.asc","r")
textCiph = inCiph.read()
#do mult
p = 1
e = 65537
line_tot = 0
file_lines = RSAmod.readlines()
linesList = list(file_lines)
#line= RSAmod.readline()
line = 0
while line < len(linesList):
	intLine = int(linesList[line],16)
	p = p*intLine
	line_tot = line_tot +1
	line= line+1
#print "past initial read in"
z = []
gcdList = []
curr = 0
p_enc = 0
numTimes = 0
text = "start"
while curr < line_tot-1:
	w = p % ((int(linesList[curr],16))**2)
	z.append(w)
	out = gcd(int(linesList[curr],16),z[curr]/int(linesList[curr],16))
	gcdList.append(out)
	p_enc = int(linesList[curr],16)/gcdList[curr]
	q = gcdList[curr]
	d = inverse(e,(p_enc-1)*(q-1))
	if p_enc != 1 and q != 1:
		val = (e*d)%((p_enc-1)*(q-1))
	else:
		val = 0
	if val == 1:
#		numTimes = numTimes+1
		tupleForKey = (int(linesList[curr],16),long(e),d,p_enc,q)
		currentKey = RSA.construct(tupleForKey)
		try:
			text = decrypt(currentKey,textCiph)
			curr = line_tot
		except:
			pass
	curr = curr+1
#print numTimes
#print text
ans.write(text)


