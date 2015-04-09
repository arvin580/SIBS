inFile=open('SNV.exome.somatic.nonsynonymous.qual')
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    if float(fields[0])>0 and float(fields[1])>0 :
        print(line)
inFile.close()
