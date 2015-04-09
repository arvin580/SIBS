inFile=open('sum_snp.genome_combined.sorted.pass012.new.UTR.genesorted_mcc_num_len2')

gene=[0]*75
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    gene[int(fields[1])]+=1

inFile.close()


import matplotlib
matplotlib.use('Agg')


import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

gene1=[]
gene2=[]

fig = plt.figure()
ax = fig.add_subplot(111)

for i in range(len(gene)) :
    if gene[i] >0 :
        gene1.append(i)
        gene2.append(gene[i])
        
ax.plot(gene1,gene2,'s-')

ax.set_xlabel('number of UTR SNV in a gene')
ax.set_ylabel('number of genes')
ax.set_xlim(0,max(gene1)+1)




plt.savefig('sum_snp.genome_combined.sorted.pass012.new.UTR.genesorted_mcc_num_len2.pdf')
