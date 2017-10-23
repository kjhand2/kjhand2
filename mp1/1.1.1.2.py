# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 19:39:32 2017

@author: ubuntu
"""

file_name = "1.1.1.2_value.hex"
write_integer = "sol_1.1.1.2_decimal.txt"
write_binary = "sol_1.1.1.2_binary.txt"


with open(file_name) as f:
    file_content = f.read().strip()

integer_parsed = int(file_content,16)

with open(write_integer, "w") as i:
    i.write(str(integer_parsed))

with open(write_binary, "w") as b:
    b.write(bin(integer_parsed)[2:])
