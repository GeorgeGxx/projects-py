# Serie Fibonacci

from math import sqrt
def F(n):
    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))

def Fibonacci(startNumber, endNumber):
    n = 0
    cur = F(n)
    while cur <= endNumber:
        if startNumber <= cur:
            print(cur)
        n += 1
        cur = F(n)
Fibonacci(1,100)