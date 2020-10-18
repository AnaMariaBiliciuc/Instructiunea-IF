a=int(input("Introduceti primul numar:"))
b=int(input("Introduceti al doilea numar:"))

if (a>b and a%2==0) or (a%2==0 and b%2!=0):
    print(a)
if (a<b and b%2==0) or (b%2==0 and a%2!=0):
    print(b)