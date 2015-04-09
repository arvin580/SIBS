inFile1=open('geneKnown','r')
ouFile1=open('geneKnown2','w')


gene=list()
for line in inFile1 :
    fields=line.split()
    flag=0
    for it,item in enumerate(gene) :
        n=0
        for i in range(5) :
            if item[i]==fields[i] :
                n+=1
        if n==5 :
            for j in range(5,25,1):
                gene[it][j]=int(gene[it][j])+int(fields[j])
                flag=1
    if flag==0 :
        gene.append(fields)

inFile1.close()



for item in gene :
    ouFile1.write('\t'.join([str(i) for i in item])+'\n')
ouFile1.close()
