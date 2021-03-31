a=int(input("enter the value from 1 to 100"))
if (a%2==1):
    print("Weird")
else:
    if(a>0 and a<11):
        print("Not weird")
    elif(a>10 and a<21):
        print("weird")
    elif(a>20):
        print("not weird")