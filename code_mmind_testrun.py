p=1
q=2
r=3
s=4

for a in range(5):
    print(a+1," Try")
    b=input("What's on your mind? ")
    lis=[p,q,r,s]
    listy=[p,q,r,s]
    count=0
    k=0
    countw=0
    for i in lis:
        if int(b[k])==i:
            count=count+1
            listy.remove(i)
        else:
            pass
        k=k+1
    if count==4:
        print("Success")
        break
    else:
        print("The number of red pegs are ",count)
    for m in range(4):                              #error from this line till the end of the loop to be fixed 
        for n in listy:                             # fix whatever is wrong 
            if int(b[m])==n:
                countw=countw+1
            else:
                pass
    print("The number of white pegs are ",countw)
else:
    print("Oh! Better luck next time!")
