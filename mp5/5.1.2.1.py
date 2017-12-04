import pickle

test = {1:"1",2:"2",3:"3"}

pickleOut = open("5.1.2.1.pickle","wb")
pickle.dump(test, pickleOut)
pickleOut.close()