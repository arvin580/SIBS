#inFile=open('/netshare1/home1/people/hansun/GeneFusionsFinal/5_Translate/exon_fusion')
#inFile.close()

def pep2dna(inF,inF2) :
    inFile=open(inF)
    ouFile=open(inF+'.dna','w')
    while True :
        line1=inFile.readline()
        line2=inFile.readline()
        line3=inFile.readline()

        line1=line1.strip()
        line2=line2.strip()
        line3=line3.strip()

        if not line1 :
            break

        inFile2=open(inF2)

        while True :
            L1=inFile2.readline()
            L2=inFile2.readline()
            
            L1=L1.strip()
            L2=L2.strip()

            if not L1 :
                break

            if line2.find(L1) !=-1 :
                ouFile.write(line1+'\n')
                ouFile.write(line2+'\n')
                ouFile.write(line3+'\n')
                ouFile.write(L1+'\n')
                ouFile.write(L2+'\n')

        inFile2.close()
    
    inFile.close()

#pep2dna('Tandem.Omssa.FDR.pep.genefusions.final.pos.3.3.curate.complete.curate','/netshare1/home1/people/hansun/GeneFusionsFinal/5_Translate/exon_fusion')
pep2dna('Tandem.Omssa.FDR.pep.splicing.final.pos.3.3.curate.complete.curate','/netshare1/home1/people/hansun/GeneFusionsFinal/5_Translate/splicing_exon')
