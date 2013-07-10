SNVINDEL = []
inFile  = open('/netshare1/home1/people/hansun/RNAseqMSMS/1-snv/A1_csv2tsv/sum_snv.exome_summary')
for line in inFile:
    line = line.strip()
    SNVINDEL.append(line)
inFile.close()

inFile  = open('/netshare1/home1/people/hansun/RNAseqMSMS/1-snv/A1_csv2tsv/sum_snv.exome_summary.indel')
for line in inFile:
    line = line.strip()
    SNVINDEL.append(line)
inFile.close()

L = []
inFile = open('/netshare1/home1/people/hansun/Data/hg19_refGene/refGene-2013-04-22.txt')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    L.append(fields)
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
            for item in SNVINDEL:
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

def predict(line): 
    fields = line.split('\t')
    for item in fields:
        if item.find('genscan')!=-1:
            ch ='chr'+item.split(':')[3]
            pos1 =item.split(':')[4]
            pos2 =item.split(':')[5]
            genes = []
            for item in L:
                if (item[2]==ch and (int(item[4])<=int(pos1)<=int(item[5]) or int(item[4])<=int(pos2)<=int(item[5]))) :
                    gene = item[12]
                    genes.append(gene)
            ouFile.write('|'.join(set(genes))+'\t'+''+'\t'+line+'\n')
            break

inFile = open('HeLa-peptide-snv-indel-predict-virus-sv')
ouFile = open('HeLa-peptide-snv-indel-predict-virus-sv-gene','w')
for line in inFile:
    line = line.rstrip()
    fields = line.split('\t')
    if fields[1]=='SNV' or fields[1]=='INDEL':
        snv_indel(line)
    elif fields[1] == 'PREDICT':
        predict(line)

inFile.close()
ouFile.close()
