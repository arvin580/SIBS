D = {}

inFile = open('sum_snp.genome_summary.012')

for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    k = '\t'.join(fields[0:3]+fields[8:9]+fields[21:26])
    D.setdefault(k, ['0']*28)
    D[k][0]=fields[-9]
    D[k][1]=fields[-8]
    D[k][2]=fields[-7]
    D[k][3]=fields[-6]
    D[k][4]=fields[-5]
    D[k][5]=fields[-4]
    D[k][6]=fields[-3]
    D[k][7]=fields[-2]
    D[k][8]=fields[-1]
    D[k][9]=fields[-10]
inFile.close()

inFile = open('sum_snp2.genome_summary.012')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    k = '\t'.join(fields[0:3]+fields[8:9]+fields[21:26])
    D.setdefault(k, ['0']*28)
    D[k][10]=fields[-9]
    D[k][11]=fields[-8]
    D[k][12]=fields[-7]
    D[k][13]=fields[-6]
    D[k][14]=fields[-5]
    D[k][15]=fields[-4]
    D[k][16]=fields[-3]
    D[k][17]=fields[-2]
    D[k][18]=fields[-1]
    D[k][19]=fields[-10]
inFile.close()

inFile = open('sum_snp34.genome_summary.012')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    k = '\t'.join(fields[0:3]+fields[8:9]+fields[21:26])
    D.setdefault(k, ['0']*28)
    D[k][20]=fields[-8]
    D[k][21]=fields[-7]
    D[k][22]=fields[-6]
    D[k][23]=fields[-5]
    D[k][24]=fields[-4]
    D[k][25]=fields[-3]
    D[k][26]=fields[-2]
    D[k][27]=fields[-1]
inFile.close()
ouFile = open('sum_snp1234.genome_summary','w')

for k in D:
    ouFile.write(k+'\t'+'\t'.join(D[k])+'\n')
ouFile.close()



