import numpy as np
from math import sqrt

def is_in(A,b,center) :
    for i in range(len(A)) :
        sum = 0
        for j in range(len(A[0])) :
            sum+= A[i][j] * center[j][0]
        if(sum > b[0][i]) :
            return False, np.array([A[i]])
    return True, np.array([[]])

def ellipsoid(C, d, Ak, center, N) :
    inn, c   = is_in(C,d,center)
    n        = len(C[0])
    nbe_iter = 0

    while(not(inn) and nbe_iter < N) :
        tmp        = Ak.dot(c.transpose())
        b          = (1/sqrt( c.dot(tmp) )) * tmp
        center     = center-b/(n+1)
        Ak         = (n**2 / ((n**2)-1)) * (Ak - 2/(n+1) * b.dot(b.transpose()))
        inn, c     = is_in(C,d,center)
        nbe_iter  += 1
    if(nbe_iter >= N) :
        return "EMPTY"
    return (Ak, center)#the center is the point on the convex


A = np.array([[-1,-1],[1,0],[-1,2]])
b = np.array([[5,-2.05,2.1]])
#the convex set is {x in Rn st Ax < b}

print(ellipsoid(A,b, 36*np.array([[1,0],[0,1]]), np.array([[0,0]]).transpose(), 5))
#the initial ellipsoid is of radius 6 centered at 0
#we do 5 iterations of the ellipsoid before stop
