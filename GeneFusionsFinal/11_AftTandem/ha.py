dict1=dict()
inFile=open('FDR.pep.annotated.annotated')
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    dict1[fields[0]]=0
inFile.close()


inFile=open('FDR.pep.genefusions.annotated')
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    if fields[0] in dict1 :
        print(line)
inFile.close()
