D = {}
inFile = open('/netshare1/home1/people/hansun/Project/snpMSMS/Tandem/output-filter/Liver-SNV-INDEL-new-pep-spec.mgf_out/0.2013_06_08_13_32_23_qry.peptides-pep.pep')
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
        if fields[1] in D:
            ouFile.write('pFind-ALL-UNIQUE'+'\t'+line)
        else:
            ouFile.write(''+'\t'+line)
    inFile.close()
    ouFile.close()

pep('Liver-SNV-INDEL-new-pep-gene-new')
