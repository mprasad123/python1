def checkEvenodd(num1):
    assert(num1>0),"Negative numbers"
    if num1%2==0:
        return "Even"
    else:
        return "odd"


for i in range(3): 
    num=int(input("Enter a no:"))
    try:
        print(num,"is",checkEvenodd(num))
    except AssertionError as ob:
         print(ob)
