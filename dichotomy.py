import math

a = int(input("put a : "))
b = int(input("put b : "))
e = float(input("error (e) : "))

def f(x):
		return pow(x,3) + 4*x*x - 10

def dichotomy(a,b,e):
	n = 0
	condition = True
	while condition:
		c,n = round((a+b)/2, 5) , n+1
		if f(c) < 0: a = c
		else: b = c
		if abs(a-b) <= e: condition = False
		print(f'iteration-{n}- -- c = {c} -- f(c) = {round(f(c), 5)}')

if f(a)*f(b)<0:
	dichotomy(a,b,e)
else:
	print("Try another Function, another Domaine")

                                   
