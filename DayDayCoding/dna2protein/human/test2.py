inFile=open('dna_protein_out1')
D=dict()
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    if  len(fields) ==6 :
        print(line)
inFile.close()
