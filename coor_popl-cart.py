import math as mt

r=float(input("digite el valor de r => "))
t=float(input("digite el valoor del angulo => "))
h=((t*mt.pi)/180)
x=(r*(mt.cos(h)))
y=(r*(mt.sin(h)))
print("X es => ", x)
print("Y s => ", y)

