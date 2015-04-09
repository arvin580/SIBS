D=dict()

inFile=open('sum_snp.genome_summary.012')
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    t='\t'.join(fields[21:26])
    D.setdefault(t,[0,0])
    D[t][0]=float(fields[31])

inFile.close()


inFile=open('sum_snp2.genome_summary.012')
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    t='\t'.join(fields[21:26])
    D.setdefault(t,[0,0])
    D[t][1]=float(fields[31])
inFile.close()

def qual(inF) :
    inFile=open(inF)
    ouFile=open(inF+'.qual','w')

    for line in inFile :
        line=line.strip()
        fields=line.split('\t')
        k='\t'.join(fields[1:6])

        ouFile.write(str(D[k][0])+'\t'+str(D[k][1])+'\t'+line+'\n')

    inFile.close()
    ouFile.close()

qual('SNV.exome.somatic.nonsynonymous')
qual('SNV.exome.somatic.nonsynonymous_nondbsnp')
