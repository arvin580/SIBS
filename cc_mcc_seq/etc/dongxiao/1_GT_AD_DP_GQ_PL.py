inFile=open('raw.snp.recalibrated.vcf')
ouFile=open('raw.snp.recalibrated.vcf.GT_AD_DP_GQ_PL','w')

for i in range(125) :
    head=inFile.readline()

for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    if fields[6]=='PASS' :
        ouFile.write('\t'.join(fields[0:2])+'\t'+'\t'.join(fields[3:6])+'\t'+'\t'.join(fields[9:])+'\n')

inFile.close()
ouFile.close()

