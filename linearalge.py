import numpy as p
import numpy.matlib
a=p.matrix("1,2,3;4,5,6;5,8,6")
b=p.matrix("1,2,3;4,6,5;6,7,8")
from scipy import linalg
print "addition two matrices \n",p.add(a,b)
print"subraction of two matrices\n",p.subtract(a,b)
print"multiplication of matrices\n",p.dot(a,b)
print"division of matrices\n",p.divide(b,a)
print "eigen values of a: \n",linalg.eig(a)
print"square root of matrix\n",p.sqrt(a)
print"square of matrix\n",p.square(a)
print "inverse of matrix a\n",linalg.inv(a)
print "det of matrix ---",linalg.det(a)
print" trace ---",p.trace(a)
print"rank ---",p.linalg.matrix_rank(a)
print "inverse \n",p.linalg.inv(a)
print"transpose \n",p.transpose(a)    

