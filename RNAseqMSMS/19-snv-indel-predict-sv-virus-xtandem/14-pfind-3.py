D = {}
inFile = open('12-pfind/gluc-0.2013_08_09_11_29_02_qry.peptides-pep.pep3')
for line in inFile:
    line = line.strip()
    D[line] = 1
inFile.close()
inFile = open('12-pfind/trypsin-0.2013_08_09_11_29_00_qry.peptides-pep.pep3')
for line in inFile:
    line = line.strip()
    D[line] = 1
inFile.close()
inFile = open('12-pfind/lysc-0.2013_08_09_11_29_01_qry.peptides-pep.pep3')
for line in inFile:
    line = line.strip()
    D[line] = 1
inFile.close()

def pep(inF):
    inFile = open(inF+'-pFind2')
    ouFile = open(inF+'-pFind3','w')
    for line in inFile:
        fields = line.split('\t')
        if fields[8] in D:
            ouFile.write('pFind'+'\t'+line)
        else:
            ouFile.write(''+'\t'+line)
    inFile.close()
    ouFile.close()

pep('HeLa-variant-Trypsin-LysC-GluC-peptide-snv-indel-predict-sv-virus-gene-miss_cleavage-known_new-normal_check-spec-to_validation_not_predict')

