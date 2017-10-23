from sys import argv
#import numpy as np

input_file = argv[1]
output_file = argv[2]

with open(input_file) as f:
    message = f.read().strip()
    message = bytearray(message)
    
mask = 0x3FFFFFFF
write_out = 0

for byte in message:
    intermediate = ((byte ^ 0xCC) << 24) | ((byte ^ 0x33) << 16) | ((byte ^ 0xAA) << 8) | (byte ^ 0x55)
#    print("intermediate: " + format(intermediate, 'x'))    
    write_out = (write_out & mask) + (intermediate & mask)
#    inter_array.append(intermediate)
#    print("write_out: " + format(write_out, 'x'))
    
#for letter1 in inter_array:
#    for letter2 in inter_array:
#         print(np.where(np.array(inter_array) == letter1 + letter2)) 
    
with open(output_file, "w") as f:
    f.write(format(write_out, 'x'))
#print(format(write_out, 'x'))