import numpy as np
a=input("Enter the array a:")
b=input("Enter the array b:")
c=np.append(a,b)
print "append of two arrays",c
for i in range(0,len(b)):
	if (b[i]>=0):
		a.append(b[i])
print"append b to a",a                                                                                                                                                                                                                                     
