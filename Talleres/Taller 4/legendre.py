# ___________________________________________________
#  Librerías
# ___________________________________________________

import numpy as np
import sympy as sp

# ___________________________________________________
#  Derivada
# ___________________________________________________

def dx(f,x,h=1e-6):
    return (f(x+h)-f(x-h))/(2*h)

# ___________________________________________________
#  Método Newton-Raphson
# ___________________________________________________

def Newt_Raph(f,df,xn,itmax = 100,preci=1e-9):
    error = 1
    it = 0
    
    while error > preci and it < itmax:
        try:
            xn1 = xn - f(xn)/df(xn)
            error  = abs(xn1-xn)
        
        except ZeroDivisionError:
            print("zero division")
        
        xn = xn1
        it += 1
        
    if it == itmax:
        return False
    else:
        return xn
# ___________________________________________________
#  Raíces
# ___________________________________________________

def GetAllRoots(f,df,x):
    
    Roots = np.array([])
    
    for i in x:
        root = Newt_Raph(f,df,i)
        
        if root != False:
            croot = np.round( root,8)
            
            if croot not in Roots:
                Roots = np.append(Roots,croot)
                
    Roots.sort()
    
    return Roots

def GetRootsPoly(n,xi,poly,d_poly,f):
    
    x = sp.Symbol('x',Real=True)
    
    poly = sp.lambdify([x],poly[n],'numpy')
    d_poly = sp.lambdify([x],d_poly[n],'numpy')
    Roots = GetAllRoots(poly,d_poly,xi)
    if n%2 != 0:
        Roots = np.insert(Roots,len(Roots),0)
    return Roots

# ___________________________________________________
#  Legendre
# ___________________________________________________
def Legendre(n):
    legendre=[]
    d_legendre=[]
    x = sp.Symbol("x",Real=True)
    y = sp.Symbol("y",Real=True)
    
    y = (x**2 - 1)**n
    for i in range(n+1):
        poly = sp.diff(y,x,i)/(2**n * np.math.factorial(i))

        legendre.append(poly)
        d_legendre.append(sp.diff(poly,x,1))
    return legendre,d_legendre


def GetWeights(Roots,d_poly,n):
    Weights = []
    x = sp.Symbol('x',Real=True)
    d_poly = sp.lambdify([x],d_poly[n],'numpy')
    
    for r in Roots:
        Weights.append(2/((1- r**2)*d_poly(r)**2))
        
    return Weights