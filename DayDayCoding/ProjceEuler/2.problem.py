def pro(upper) :
    s=[]
    n1=1
    n2=2
    n3=0
    s.append(n1)
    s.append(n2)
    while n3<=upper :
        n3=n1+n2
        s.append(n3)
        n1=n2
        n2=n3
    return s

s=pro(4000000)

m=0
for x in s :
    if x%2==0 :
        m+=x
print(m)


    
