L1=list()
inFile=open('FDR.pep.annotated.annotated')
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    L1.append(fields[0])
inFile.close()
SL1=set(L1)


L2=list()
inFile=open('FDR.pep.genefusions.annotated')
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    L2.append(fields[0])
inFile.close()
SL2=set(L2)

L3=list()
inFile=open('FDR.pep.splicing.annotated')
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    L3.append(fields[0])
inFile.close()
SL3=set(L3)

L=(SL1 | SL2 | SL3)

for item in L :
    print(item)
