def isPalindromic(s) :
    s=str(s)
    ns=len(s)
    for i in range(ns/2) :
        if s[i]!=s[ns-i-1] :
            return False 
    return True

p=[]
q1=[]
q2=[]
for x in range(999,99,-1) :
    for y in range(999,99,-1) :
        m= x * y
        t=isPalindromic(m) 
        if t :
            p.append(m)
            q1.append(x)
            q2.append(y)

print(max(p))
print(q1[p.index(max(p))])
print(q2[p.index(max(p))])

