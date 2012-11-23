inFile = open('tandem.peptides.stopgain.candidates')
D = {}
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    gene = fields[4].split(':')[1]
    #D.setdefault(gene,[])
    #D[gene].append(line)
    D.setdefault(gene,{})
    k = fields[1].split('output_')[1].split('.')[0]
    D[gene].setdefault(k,0)
    D[gene][k]+=1

inFile.close()

#for k in D:
#    if len(D[k])>1:
#        print(k)
#        print(D[k])

ouFile = open('tandem.peptides.stopgain.candidates.gene', 'w')

for k1 in D:
    ouFile.write(k1+'\t')
    for  k2 in D[k1]:
        ouFile.write(k2 +'\t'+str(D[k1][k2])+'\t')
    ouFile.write('\n')

ouFile.close()
