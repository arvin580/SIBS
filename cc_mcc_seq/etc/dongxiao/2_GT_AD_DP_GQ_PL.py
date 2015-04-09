import csv
inFile=open('sum_snp.genome_summary.csv')
ouFile=open('raw.snp.recalibrated.vcf.GT_AD_DP_GQ_PL_gene','w')

csvFile=csv.reader(inFile)

head=csvFile.next()

for fields in csvFile :

    if fields[32]=='PASS' :
        ouFile.write('\t'.join(fields[0:3]+fields[21:23]+fields[24:26]+fields[31:32]+fields[-10:])+'\n')

inFile.close()
ouFile.close()

