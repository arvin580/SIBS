def mk_fasta(inF):
    inFile = open(inF)
    ouFile = open(inF+'.fasta','w')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        for item in fields[1:]:
            if item.find('S:')==0:
                ouFile.write('>'+fields[0]+'|'+item+'\n')
                ouFile.write(item.split(':')[1]+'\n')
    inFile.close()

mk_fasta('3-stopgain-protein-unique2-filtered')
