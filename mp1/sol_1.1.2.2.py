from Crypto.Cipher import AES
from sys import argv


cipher_file = argv[1]
key_file = argv[2]
iv_file = argv[3]
output_file = argv[4]

with open(cipher_file) as f:
    cipher = f.read().strip()
    cipher1 = cipher.decode('hex')
with open(key_file) as f:
    key = f.read().strip()
    key = key.decode('hex')
with open(iv_file) as f:
    iv = f.read().strip()
    iv = iv.decode('hex')

AES_cipher = AES.new(key, 2, iv)

write_out = AES_cipher.decrypt(cipher1)

with open(output_file, "w") as f:
    f.write(write_out)
    
print(write_out)