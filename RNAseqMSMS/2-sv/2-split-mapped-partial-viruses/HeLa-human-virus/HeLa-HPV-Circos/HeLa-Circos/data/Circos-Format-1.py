def Circos_Format(inF):
    inFile = open(inF)
    ouFile = open(inF+'.circos','w')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        ouFile.write(fields[0]+'\t'+fields[1]+'\t'+str(int(fields[1])+1)+'\t'+str(0.2)+'\n')
    inFile.close()
    ouFile.close()

Circos_Format('ERR0498-04-05.unmapped.unique.human-viruse-checked-human-chr-site')
