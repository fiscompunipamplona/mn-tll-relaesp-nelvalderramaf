import math as mt

o=float(input("Digite el valor de x en años luz "))
h=float(input("Digite el valor de la velocidad (como fraccion de c)"))
x=o*9.461e15 #m
c=3e8#m/s
v=h*c#m/s
t=x/v#s
print("El tiempo desde la tierra es => ",t)
ga=(mt.sqrt(1-((v**2)/(c**2))))
T=((t-((v*x)/c**2))/ga)#s
print("el tiempo desde el observador es => ",T)
