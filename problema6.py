n1=int(input("Introduceti prima nota: "))
n2=int(input("Introduceti a2a nota: "))
n3=int(input("Introduceti a3a nota "))
if n1<=10 and n1>0 and n2<=10 and n2>0 and n3<=10 and n3>0:
    if n3>=8:
        print(n1 ,n2 ,n3 ,)
    else:
        if n3<8:
            print(n2)
        elif n1>n2:
            print(n2)
        else:
            print(n1)