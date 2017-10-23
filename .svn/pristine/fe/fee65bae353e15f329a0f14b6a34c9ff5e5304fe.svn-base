from sys import argv

cipher_file = argv[1]
key_file = argv[2]
modulo_file = argv[3]
output_file = argv[4]

with open(cipher_file) as f:
    encrypted = f.read().strip()
    encrypted = int(encrypted,16)
with open(key_file) as f:
    key = f.read().strip()
    key = int(key,16)
with open(modulo_file) as f:
    modulo = f.read().strip()
    modulo = int(modulo,16)
    
#e_prime = 0
#message = 1
#while(e_prime < key):
#    e_prime = e_prime+1
#    message = (encrypted * message) % modulo

message = pow(encrypted, key, modulo)

with open(output_file, "w") as f:
    f.write(format(message, 'x'))