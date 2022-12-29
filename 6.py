n1=int(input("enter a number:"))
n2=int(input("enter a number:"))

try:
    res=n1/n2
except ZeroDivisionError:
    print("divison by zero not allowed")
else:
    print (n1,'/' ,n2, '=', res)
print('thanks')
