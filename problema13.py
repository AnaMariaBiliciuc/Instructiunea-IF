x=int(input("Introduceti locul pe care l-a luat participantul: "))
if x<=100:
    if x%4==0:
        print("neagra")
    elif x%3==0:
        print("albastra")
    elif x%2==0:
        print("rosie")
else:
        print("alba")