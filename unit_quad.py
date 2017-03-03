import quad_func as qf
import math

tol=1E-15
a=1.0
b=1.0
c=-1.0
roots=qf.quad_form(a,b,c)
sqr5=math.sqrt(5)
r1=.5*(-1.0+sqr5)
r2=.5*(-1.0-sqr5)
err1=math.fabs(roots[0]-r1)
err2=math.fabs(roots[1]-r2)
if err1 < tol and err2 < tol:
    print('Pass Unit Test 1')
else:
    print('Fail Unit Test 1'),err1,err2

