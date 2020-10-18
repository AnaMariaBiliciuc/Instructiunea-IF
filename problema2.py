a=int(input("Introduceti lungimea laturii 1= "))
b=int(input("Introduceti lungimea laturii 2=  "))
c=int(input("Introduceti lungimea laturii 3= "))
if (a<32000) and (b<32000) and (c<32000) : 
    print(" Numerele au valori mai mici de 32000")
if (a<b+c) and (b<a+c) and (c<a+b) :
    print ("DA")
else :
    print ("NU")