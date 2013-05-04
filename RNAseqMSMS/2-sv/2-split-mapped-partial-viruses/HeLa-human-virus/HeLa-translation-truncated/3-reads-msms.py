inFile = open('ERR0498-04-05.unmapped.unique.human-viruse-checked-random-10000')
ouFile = open('ERR0498-04-05.unmapped.unique.human-viruse-checked-random-10000-msms','w')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    D = fields

    D2 = {}
    inFile = open('HeLa-Known-Protein')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        for item in fields:
            its = item.split(':')
            for it in its:
                if it in D:
                    D2.setdefault(it,[])
                    D2[it].append(line)
    inFile.close()
    
    inFile = open('HeLa-Human-Viruses')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        for item in fields:
            its = item.split(':')
            for it in its:
                if it in D:
                    D2.setdefault(it,[])
                    D2[it].append(line)
    inFile.close()
    
    inFile = open('HeLa-Viruses')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        for item in fields:
            its = item.split(':')
            for it in its:
                if it in D:
                    D2.setdefault(it,[])
                    D2[it].append(line)
    inFile.close()
    
    
    
    for k in D2:
        ouFile.write(str(len(D2))+'\n')

