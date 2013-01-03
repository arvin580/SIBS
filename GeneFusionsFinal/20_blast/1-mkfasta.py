ouFile = open('Tandem.Ossma.genefusion.splicing.fa', 'w')
def mkfa(inF):
    inFile = open(inF)
    n = 0
    for line in inFile:
        n+=1
        line = line.strip()
        fields = line.split('\t')
        ouFile.write('>'+inF+'\t'+line+'\n')
        ouFile.write(fields[0]+'\n')
    inFile.close()
mkfa('Tandem.FDR.pep.genefusions.final.pos.3.3')
mkfa('Tandem.FDR.pep.splicing.final.pos.3.3')
mkfa('Omssa.FDR.pep.genefusions.final.pos.3.3')
mkfa('Omssa.FDR.pep.splicing.final.pos.3.3')
