import urllib2
from sys import argv
import binascii

def pad(msg):
    n = len(msg) % 16
    return msg + "".join(chr(i) for i in range(16, n, -1))

def get_status(u):
    req = urllib2.Request(u)
    try:
        f = urllib2.urlopen(req)
        return f.code
    except urllib2.HTTPError, e:
        return e.code

ciphertext = argv[1]
output = argv[2]

with open(ciphertext) as f:
    cipher = f.read().strip()
    cipher = cipher.decode('hex')
    
cipher = bytearray(cipher)
#maybe just use cipher and then do all the math with % or something
#do we need to keep track of the message block? we are just changing 
#cipher -15 bytes
original_message = bytearray(len(cipher)) #place to store the guesses when they are right

for byte_index in range(len(cipher)-1, 15, -1):
    cipher_copy = bytearray(cipher)
    block_number = int(byte_index / 16)
    byte_number = byte_index % 16
    for g in range(0, 256):
        cipher_copy[byte_index - 16] = cipher[byte_index-16] ^ g
        for i in range(byte_index +1, (block_number+1) * 16):
            cipher_copy[i-16] = cipher[i-16] ^ original_message[i]
        padding = pad(bytearray(byte_number))
        for i in range((block_number-1)*16, block_number*16):
            cipher_copy[i] = cipher_copy[i] ^ padding[i%16]
        
        url = "http://192.17.90.133:9998/mp1/kjhand2/?" + binascii.hexlify(cipher_copy[(block_number-1)*16:(block_number+1) * 16])
        status = get_status(url)
        if(status == 404):
            #print(g)
            original_message[byte_index] = g
            break
    if(g == 255 & status != 404):
        print("ERROR")
        break
    
with open(output, 'w') as f:
    f.write(original_message[16:103])