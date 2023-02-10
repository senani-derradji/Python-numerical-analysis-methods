import math

def f(x):
    f = pow(x,3) + 4*pow(x,2) - 10
    return round(f, 6)

def g(x):
    '''    f(x) =  x³ + 4x² - 10  / g(x) = f'(x)  '''
    g = 3*x**2 + 8*x
    return round(g, 6)

a = int(input("a : "))
b = int(input("b : "))
e = float(input("e : "))

def Newton(a,b,e=0.0001):
    x0 = (a+b)/2
    i , condition = 1 , True
    
    while condition:
        x1 = round(x0 - (f(x0)/g(x0)), 6)
        print(f'iterations-{i}- ,X1 = {x1} ')
    
        if abs(x1-x0) <= e: condition = False
        x0 = x1
        i = i+1
        
    print(f'solution is : {x1}')
Newton(a,b,e)