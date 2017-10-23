# -*- coding: utf-8 -*-
import os,sys
fkey = open(sys.argv[2],"r") 
fkey_cont = fkey.read().strip()
fciph = open(sys.argv[1],"r")
fciph_cont = fciph.read().strip()
s = len(fciph_cont)
s_key = len(fkey_cont)
run = ['']*s
fout =  open(sys.argv[3],"w+")
x=0
y=0
key = fkey_cont[x]
ascii_uppercase = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
while True:
	if fkey_cont[x] == fciph_cont[y]:
		test = ascii_uppercase[x]
		run[y] = test
	if fciph_cont[y] == '0' or fciph_cont[y] == '1' or fciph_cont[y] == '2' or fciph_cont[y] == '3' or fciph_cont[y] == '4' or fciph_cont[y] == '5' or fciph_cont[y] == '6' or fciph_cont[y] == '7' or fciph_cont[y] == '8' or fciph_cont[y] == '9':
		run[y] = fciph_cont[y]
	if s == y+1 and s_key == x+1:
		break
	if s==y+1:
		x =x+1
		y=0
	else:
		y =y+1
fout.write(" ".join(map(lambda x: str(x),run)))
fout.close()
fciph.close()
fkey.close()



