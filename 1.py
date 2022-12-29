def kelvinTofahrenheit(Temperature):
    assert (Temperature >= 0),"colder than absolute zero at MTICA!"
    res=((Temperature-273)*1.8)+32
    return res
try:
    print (kelvinTofahrenheit(-50))
except Exception as ob:
        print(ob)
try:
    print (kelvinTofahrenheit(273))
except Exception as ob:
        print(ob)
try:
    print (kelvinTofahrenheit(505.78))
except Exception as ob:
        print(ob)
try:
    print (kelvinTofahrenheit(-5))
except Exception as ob:
        print(ob)
        
print("Thank you")
        
        
