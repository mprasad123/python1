def Factorial (n):
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
    print(Factorial(45))
except Exception as obj:
    print(obj)
            
