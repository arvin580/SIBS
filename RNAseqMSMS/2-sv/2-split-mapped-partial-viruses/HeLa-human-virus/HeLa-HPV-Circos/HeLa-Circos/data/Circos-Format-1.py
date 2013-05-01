def Circos_Format(inF):
    D = {}
    inFile = open(inF)
    ouFile = open(inF+'.circos','w')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        p = fields[0]+'\t'+fields[1]
        D.setdefault(p,1)
        ouFile.write(fields[0]+'\t'+fields[1]+'\t'+str(int(fields[1])+1)+'\t'+str(D[p])+'\n')
        D[p]-=0.02
    inFile.close()
    ouFile.close()

Circos_Format('ERR0498-04-05.unmapped.unique.human-viruse-checked-human-chr-site')
Circos_Format('ERR0498-04-05.unmapped.unique.human-viruse-checked-virus-site')
