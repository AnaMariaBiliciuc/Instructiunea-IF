a=int(input("Introduceti primul nr: "))
b=int(input("Introduceti a doilea nr: "))
c=int(input("Introduceti a treilea nr: "))
if (a>0) and (b>0) and (c>0) :
    if b>c:
        print(b)
    else:
        print(c)
else:
    print(a+b)