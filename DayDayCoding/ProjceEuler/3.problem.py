def primer(n) :
    fac=2
    while n>1 :
        if n % fac==0 :
            print(fac)
            while n % fac ==0 :
                n=n/fac
        fac+=1
primer(600851475143)

