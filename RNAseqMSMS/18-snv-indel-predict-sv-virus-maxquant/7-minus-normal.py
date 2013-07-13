D = {}
def normal(inF):
    inFile = open(inF)
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        for i in range(len(fields)):
            if fields[i].find('Velos1_NaNa')!=-1:
                f = fields[i]
                no = fields[i+27]
                fno = f + ':' + no
                D.setdefault(fno,0)
                D[fno] += 1
    inFile.close()

normal('HeLa-known-Trypsin-evidence-unique')
normal('HeLa-known-LysC-evidence-unique')
normal('HeLa-known-GluC-evidence-unique')

ouFile = open('HeLa-known-Trypsin-LysC-GluC-spec','w')
for k in D:
    ouFile.write(k+'\t'+str(D[k])+'\n')
ouFile.close()

inFile = open('HeLa-variant-Trypsin-LysC-GluC-evidence-unique-peptide-snv-indel-predict-sv-virus-gene-miss_cleavage-known_new')
ouFile = open('HeLa-variant-Trypsin-LysC-GluC-evidence-unique-peptide-snv-indel-predict-sv-virus-gene-miss_cleavage-known_new-normal_check','w')

for line in inFile:
    line = line.rstrip()
    fields = line.split('\t')
    if fields[8].find('PREDICT')==-1:
        flag = 0
        for i in range(len(fields)):
            if fields[i].find('Velos1_NaNa')!=-1:
                f = fields[i]
                no = fields[i+27]
                fno = f + ':' + no
                if fno not in D:
                    flag = 1
                    break
        if flag:
            ouFile.write('Normal-Not-Matched'+'\t'+line+'\n')
        else:
            ouFile.write('Normal-Matched'+'\t'+line+'\n')
    else:
        ouFile.write('Normal-Not-Check'+'\t'+line+'\n')
        

inFile.close()
    
