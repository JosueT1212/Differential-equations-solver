import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

rel=1e-6 #Relative error 
def string_to_function(func):
    f=sp.sympify(func)
    f=sp.lambdify(("x","y"),func)
    return f




V0=(float(input("Introduce el valor inicial de la variable de estado: ")))
func=string_to_function(input("Introduce la funcion dy/dx: "))
h=(float(input("Introduce el paso del metodo RK4: ")))
t=float(input("Introduce el punto inicial que desas analizar: "))
tf=(float(input("Introduce el punto final que deseas analizar: ")))


V=V0

tarr=[]
Varr=[]
#RK4 method
while(t<=tf+rel):
    tarr=tarr+[t]
    Varr=Varr+[V]
    k1=h*func(t,V)
    k2=h*func(t+h/2,V+k1/2)
    k3=h*func(t+h/2,V+k2/2)
    k4=h*func(t+h,V+k3)
    V=V+(1/6)*(k1+2*k2+2*k3+k4)
    t=t+h
    
    

print(Varr)
plt.plot(tarr,Varr)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Runge Kutta 4')
plt.show()


     














