inFile=open('hg19.refGene.stat')
ouFile=open('hg19.refGene.stat2','w')

line=inFile.readline()
ouFile.write(line)

chr_sum=[0]*7
chr_sum[0]='total'
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    for i in range(len(fields[1:])) :
        chr_sum[i+1]+=float(fields[i+1])
    ouFile.write(line+'\n')
inFile.close()

ouFile.write('\t'.join([str(i) for i in chr_sum]))
