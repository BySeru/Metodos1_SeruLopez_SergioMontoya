# ___________________________________________________
#  Librerías
# ___________________________________________________

import numpy as np

# ___________________________________________________
#  Derivada
# ___________________________________________________

def dx(f,x,h=1e-6):
    return (f(x+h)-f(x-h))/(2*h)

# ___________________________________________________
#  Método Newton-Raphson
# ___________________________________________________

def Newt_Raph(f,df,xn,h=1e-6,iter_max=1000,preci=1e-6):
    error=1
    itera=0
    while (error > preci) and (itera < iter_max):
        
        try:
            xn1 = xn - f(xn)/df(f,xn)
            error=np.abs((xn1-xn)/xn)
            
        except ZeroDivisionError:
            print("Imagínate que tienes cero galletas y la repartes entre cero amigos. ¿Cuántas galletas le tocan a cada amigo? No tiene sentido, ¿lo ves? Así que el Monstruo de las galletas está triste porque no tiene galletas y tu estás triste porque no tienes amigos. Intenta otro valor.")
            #Tomado de Siri

        xn = xn1
        itera += 1
    
    if itera == iter_max:
        return False
    else:
        return xn

# ___________________________________________________
#  Raíces
# ___________________________________________________

def GetAllRoots(x,f):
    Roots = np.array([])
    
    if f(0) < 1e-10:
        Roots=np.append(Roots,f(0))
    
    for i in x:
        root = Newt_Raph(f,dx,i)
        
        if root != False:
            root = np.round(root,6)
            
            if root not in Roots:
                Roots = np.append(Roots,root)
                
    Roots.sort()
    
    return Roots