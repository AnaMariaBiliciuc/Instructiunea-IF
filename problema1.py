e1=int(input("Introduceti nr elevului "))
e2=int(input("Introduceti nr elevului "))
e3=int(input("Introduceti nr elevului "))
p1=int(input("Introduceti punctajul elevului 1= "))
p2=int(input("Introduceti punctajul elevului2= "))
p3=int(input("Inroduceti punctajul elevului 3= "))
if ((p1>p2) and (p1>p3)) :
    print(e1)
if ((p2>p1) and (p2>p3)) :
     print(e2)
if ((p3>p1) and (p3>p2)) :
     print(e3)