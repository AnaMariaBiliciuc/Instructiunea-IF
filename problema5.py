zc=int(input("Introduceti ziua curenta: "))
lc=int(input("Introduceti luna curenta: "))
ac=int(input("Introduceti anul curent: "))
zn=int(input("Introduceti ziua nasterii: "))
ln=int(input("Introduceti luna nasterii: "))
an=int(input("Introduceti anul nasterii: "))
if (lc>ln) :
     print("Varsta persoanei este ",(ac-an)+1)
else :
    print("Varsta persoanei este ",ac-an)