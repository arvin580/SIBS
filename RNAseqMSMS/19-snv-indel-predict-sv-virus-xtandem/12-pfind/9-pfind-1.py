D = {}
inFile = open('/netshare1/home1/people/hansun/RNAseqMSMS/12-SNV-INDEL-VIRUS-SV/HeLa-SNV-INDEL-VIRUS-SV-MGF.mgf_out/0.KR-2013_06_01_09_57_53-K8R10_qry.peptides-pep.pep')
for line in inFile:
    line = line.strip()
    D.setdefault(line,0)
    D[line] += 1
inFile.close()

inFile = open('/netshare1/home1/people/hansun/RNAseqMSMS/12-SNV-INDEL-VIRUS-SV/HeLa-SNV-INDEL-VIRUS-SV-MGF.mgf_out/0.K-2013_06_01_09_57_53-K8R10_qry.peptides-pep.pep')
for line in inFile:
    line = line.strip()
    D.setdefault(line,0)
    D[line] += 1
inFile.close()

inFile = open('/netshare1/home1/people/hansun/RNAseqMSMS/12-SNV-INDEL-VIRUS-SV/HeLa-SNV-INDEL-VIRUS-SV-MGF.mgf_out/0.ED-2013_06_01_09_57_53-K8R10_qry.peptides-pep.pep')
for line in inFile:
    line = line.strip()
    D.setdefault(line,0)
    D[line] += 1
inFile.close()

def pep(inF):
    inFile = open(inF)
    ouFile = open(inF+'-pFind1','w')
    for line in inFile:
        fields = line.split('\t')
        if fields[3] in D:
            ouFile.write('pFind-ALL-UNIQUE'+'\t'+line)
        else:
            ouFile.write(''+'\t'+line)
    inFile.close()
    ouFile.close()

pep('HeLa-SNV-INDEL-VIRUS-SV-pep-new')
