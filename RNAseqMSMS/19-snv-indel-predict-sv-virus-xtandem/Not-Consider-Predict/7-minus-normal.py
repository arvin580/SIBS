D = {}
import os
def normal(Dir):
    fs = os.listdir(Dir)
    for inF in fs:
        if inF[-8:] == '.txt.fdr':
            inFile = open(Dir + os.sep+ inF)
            for line in inFile:
                fields = line.split('\t')
                spc = fields[0]
                D[spc]=1
            inFile.close()

normal('/netshare1/home1/people/hansun/RNAseqMSMS/15-snv-indel-sv-virus-KR/output-second')
normal('/netshare1/home1/people/hansun/RNAseqMSMS/16-snv-indel-sv-virus-K/output-second')
normal('/netshare1/home1/people/hansun/RNAseqMSMS/17-snv-indel-sv-virus-ED/output-second')

ouFile = open('HeLa-known-Trypsin-LysC-GluC-spec','w')
for k in D:
    ouFile.write(k+'\n')
ouFile.close()

inFile = open('HeLa-variant-Trypsin-LysC-GluC-peptide-snv-indel-predict-sv-virus-gene-miss_cleavage-known_new')
ouFile = open('HeLa-variant-Trypsin-LysC-GluC-peptide-snv-indel-predict-sv-virus-gene-miss_cleavage-known_new-normal_check','w')

for line in inFile:
    line = line.rstrip()
    fields = line.split('\t')
    if fields[8].find('PREDICT')==-1:
        flag = 0
        for i in range(len(fields)):
            if fields[i].find('Velos1_NaNa')!=-1:
                if fields[i] not in D:
                    flag = 1
                    break
        if flag:
            ouFile.write('Normal-Not-Matched'+'\t'+line+'\n')
        else:
            ouFile.write('Normal-Matched'+'\t'+line+'\n')
    else:
        ouFile.write('Normal-Not-Check'+'\t'+line+'\n')
        

inFile.close()
    
