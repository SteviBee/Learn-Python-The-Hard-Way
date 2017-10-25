#trying to use pickle to store profiles and get them back
#i am trying to use cpickle because it is faster
try:
    import cPickle as pickle
except:
    import pickle

x = 'this is cool'

#storing the variable to the new file!
f = open('profiledict.pkl', 'wb')
#-1 specifies highest binary proticol
pickle.dump(x, f, -1)
f.close()

#getting it back!
f = open('profiledict.pkl', 'rb')
y = pickle.load(f)
f.close()
print "Y = ", y
