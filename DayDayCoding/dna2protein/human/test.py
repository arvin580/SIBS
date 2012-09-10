inFile=open('dna_protein_out1.anno')
D=dict()
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    if  len(fields) >5 :
        #print(line)
        D.setdefault(len(fields),0)
        D[len(fields)]+=1
inFile.close()

for key in D :
    print(str(key)+'\t'+str(D[key]))
