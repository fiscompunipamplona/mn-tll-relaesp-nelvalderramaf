print(" serie de fibonacci para numeros menores que 1000")
m1=1
m2=1
print(m1)
print(m2)
m3=m1+m2
print(m3)
while m3<1000:
	m1=m2
	m2=m3
	m3=m1+m2
	if m3>1000:
		break
	print(m3)
