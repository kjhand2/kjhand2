import hashlib,binascii,io,sys
def hamDist(bin_1,bin_2):
	return sum(x1 != x2 for x1, x2 in zip(bin_1,bin_2))
#in and out
s1 = open(sys.argv[1],"r")
s2 = open(sys.argv[2],"r")
out = io.FileIO(sys.argv[3],"w")
#convert to hash input string
s1cont = s1.read().strip()
bin_1 = bin(int(hashlib.sha256(s1cont).hexdigest(),16))[2:]
#convert to hash perturbed string
s2cont = s2.read().strip()
bin_2 = bin(int(hashlib.sha256(s2cont).hexdigest(),16))[2:]
#compute hamming distance
res = hamDist(bin_1=bin_1,bin_2=bin_2)
out.write(str(hex(res-1)[2:]))
out.close()
s2.close()
s1.close()



