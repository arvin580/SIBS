
def pep2dna(pep,ouFile) :

    inFile=open('Tandem.Omssa.FDR.pep.genefusions.final.pos.3.3.curate.complete.curate.dna')
    while True :
        line1=inFile.readline()
        line2=inFile.readline()
        line3=inFile.readline()
        line4=inFile.readline()
        line5=inFile.readline()

        if not line1 :
            break
        
        p=line1.strip('#\r\n')
        line5=line5.strip()
        if p == pep :
            fields=line2.split(':')
            ouFile.write(pep+'\t')
            ouFile.write(fields[1]+'\t')
            ouFile.write(fields[3]+'\t')
            ouFile.write(fields[2]+'\t')
            ouFile.write(fields[4]+'\t')
            ouFile.write(line5+'\n')
        
    inFile.close()

    inFile=open('Tandem.Omssa.FDR.pep.splicing.final.pos.3.3.curate.complete.curate.dna')
    while True :
        line1=inFile.readline()
        line2=inFile.readline()
        line3=inFile.readline()
        line4=inFile.readline()
        line5=inFile.readline()

        if not line1 :
            break
        
        p=line1.strip('#\r\n')
        line5=line5.strip()
        if p == pep :
            fields=line2.split(':')
            ouFile.write(pep+'\t')
            ouFile.write(fields[1]+'\t')
            ouFile.write(fields[3]+'\t')
            ouFile.write(fields[2]+'\t')
            ouFile.write(fields[4]+'\t')
            ouFile.write(line5+'\n')
        
    inFile.close()





inFile=open('Tandem.Omssa.FDR.pep.genefusions.splicing.final.pos.3.3.spec2.num.both')
ouFile=open('pep.dna.table','w')

for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    pep=fields[0]
    pep2dna(pep,ouFile)

inFile.close()
ouFile.close()
