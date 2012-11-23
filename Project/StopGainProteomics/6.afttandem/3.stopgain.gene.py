inFile = open('tandem.peptides.stopgain.candidates')
D = {}
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    gene = fields[4].split(':')[1]
    #D.setdefault(gene,[])
    #D[gene].append(line)
    D.setdefault(gene,{})
    k = fields[0].split('output_')[1].split('.')[0]
    D[gene].setdefault(k,0)
    D[gene][k]+=1

inFile.close()

#for k in D:
#    if len(D[k])>1:
#        print(k)
#        print(D[k])

ouFile = open('tandem.peptides.stopgain.candidates.gene', 'w')

d = D.items()
d.sort(cmp=lambda x,y:cmp(len(x[1]),len(y[1])),reverse=True)

for item in d : 
    ouFile.write(item[0]+'\t')
    for it in item[1]:
        ouFile.write(it +'\t'+str(item[1][it])+'\t')
    ouFile.write('\n')


#for k1 in D:
#    ouFile.write(k1+'\t')
#    for  k2 in D[k1]:
#        ouFile.write(k2 +'\t'+str(D[k1][k2])+'\t')
#    ouFile.write('\n')
ouFile.close()
