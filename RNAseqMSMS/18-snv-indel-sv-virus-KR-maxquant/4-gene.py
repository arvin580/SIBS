L = []
inFile  = open('/netshare1/home1/people/hansun/RNAseqMSMS/1-snv/A1_csv2tsv/sum_snv.exome_summary')
for line in inFile:
    line = line.strip()
    L.append(line)
inFile.close()

inFile  = open('/netshare1/home1/people/hansun/RNAseqMSMS/1-snv/A1_csv2tsv/sum_snv.exome_summary.indel')
for line in inFile:
    line = line.strip()
    L.append(line)
inFile.close()

def snv_indel(line):
    fields = line.split('\t')
    fds = fields[10].split(':')
    for i in range(len(fds)):
        if fds[i].find('SNV')!=-1 or fds[i].find('INDEL')!=-1:
            ch = fields[10].split(':')[i+1]
            pos = fields[10].split(':')[i+2]
            genes = []
            dbsnps = []
            for item in L:
                if item.find(ch) != -1 and item.find(pos) != -1: 
                    gene = item.split('\t')[1].split('(')[0]
                    dbsnp = item.split('\t')[8]
                    genes.append(gene)
                    dbsnps.append(dbsnp)
            if dbsnps:        
                ouFile.write('|'.join(genes)+'\t'+'|'.join(dbsnps)+'\t'+line+'\n')
            else:
                ouFile.write('|'.join(genes)+'\t'+'new'+'\t'+line+'\n')
            break


inFile = open('HeLa-peptide-snv-indel-predict-virus-sv')
ouFile = open('HeLa-peptide-snv-indel-predict-virus-sv-gene','w')
for line in inFile:
    line = line.rstrip()
    fields = line.split('\t')
    if fields[1]=='SNV' or fields[1]=='INDEL':
        snv_indel(line)
inFile.close()
ouFile.close()
