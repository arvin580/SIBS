inFile = open('tandem.peptides.stopgain.candidates')
D = {}
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    gene = fields[4].split(':')[1]
    #D.setdefault(gene,[])
    #D[gene].append(line)
    D.setdefault(gene,{})
    pep = fields[2]+':'+fields[4].split(':')[-2]+':'+fields[4].split(':')[-1]
    D[gene].setdefault(pep,{})
    ###k = fields[0].split('output_')[1].split('.')[0]
    k = fields[0].split('output_')[1].split('.')[0].split('_')[1].split('-')[0]
    D[gene][pep].setdefault(k,0)
    D[gene][pep][k]+=1

inFile.close()

#for k in D:
#    if len(D[k])>1:
#        print(k)
#        print(D[k])
ouFile = open('tandem.peptides.stopgain.candidates.gene2', 'w')

d = D.items()
d.sort(cmp=lambda x,y:cmp(len(x[1]),len(y[1])),reverse=True)

for item in d : 
    for pep in item[1]:
        ouFile.write(item[0]+'\t'+pep+'\t')
        for cl in item[1][pep]:
            ouFile.write(cl +'\t' + str(item[1][pep][cl])+ '\t')
        ouFile.write('\n')


#for k1 in D:
#    ouFile.write(k1+'\t')
#    for  k2 in D[k1]:
#        ouFile.write(k2 +'\t'+str(D[k1][k2])+'\t')
#    ouFile.write('\n')
ouFile.close()
