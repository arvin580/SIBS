def filter(inF):
    inFile = open(inF)
    ouFile = open(inF+'-filtered','w')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        f1 = 0
        f2 = 0
        for item in fields[1:]:
            if item.find('S:')==0:
                f1 =1
            if item.find('T:')==0 or item.find('K:')==0:
                f2 =1
        if f1 and f2 :
            ouFile.write(line+'\n')
    
    inFile.close()
    ouFile.close()

filter('3-stopgain-protein-unique')
filter('3-stopgain-protein-unique2')
