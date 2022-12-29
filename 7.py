n1=input("enter a number:")
n2=input("enter a number:")

try:
    res=int(n1)/int(n2)
except (ZeroDivisionError,ValueError):
    print("Exception handaled by prabha")
except ValueError:
    print("Exception handaled by prasad")
except Exception as ob:
    print (ob)
else:
    print (n1,'/' ,n2, '=', res)
finally:
    print("thanks")
    
print("visit again at python class at MTICA")
