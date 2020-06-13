p=1
q=2
r=2
s=4
lis=[p,q,r,s]
for a in range(5):
    print(a+1," Try")
    b=input("What's on your mind? ")
    ls=[]
    for obj in b:
        ls.append(int(obj))
    listy=[p,q,r,s]
    count=0
    k=0
    countw=0
    for i in lis:
        if int(b[k])==i:
            count=count+1
            listy.remove(i)
            ls.remove(i)
        else:
            pass
        k=k+1
    if count==4:
        print("Success")
        break
    else:
        print("The number of red pegs are ",count)
    for m in ls:                        
        for n in listy:                         
            if m==n:
                countw=countw+1
                listy.remove(n)
            else:
                pass
    print("The number of white pegs are ",countw)
else:
    print("Oh! Better luck next time!")
