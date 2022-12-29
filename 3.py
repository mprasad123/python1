def Factorial (n):
    assert(isinstance(n,int)),"factorial not defined for non integer"
    assert(n>=0)," Factorial of negative number is not defined!"
    if n==0:
        return 1
    else:
        return n*Factorial(n-1)
try:
    print(Factorial(-45))
except Exception as obj:
    print(obj)
try:
    print(Factorial(4.9))
except Exception as obj:
    print(obj)
try:
    print(Factorial('prabha'))
except Exception as obj:
    print(obj)
            
            
