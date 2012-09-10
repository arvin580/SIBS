def pro(n1,n2,n3) :
    s=0
    for i in range(1,n1) :
        if i%n2==0 or i%n3 ==0 :
            s+=i
    return s

s=pro(1000,3,5)
print(s)
