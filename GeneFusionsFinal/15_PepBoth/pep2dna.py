def pep2dna(inF,inF2) :
    inFile=open(inF)
    ouFile=open(inF+'.complete','w')
    for line in inFile :
        line=line.strip()
        if len(line) >0 :
            fields=line.split('\t')
            pep=fields[0]
            ouFile.write('#'+pep+'\n')
            inFile2=open(inF2)
            while True :
                line1=inFile2.readline()
                line2=inFile2.readline()
    
                if line2.find(pep)!=-1 :
                    ouFile.write(line1)
                    ouFile.write(line2)
                if not line1 :
                    break
            inFile2.close()
    inFile.close()
    ouFile.close()

#pep2dna('Tandem.Omssa.FDR.pep.genefusions.final.pos.3.3.curate','/netshare1/home1/people/hansun/GeneFusionsFinal/9_FinalDataBase/fusion_splicing_uniprot_ensembl_contaminated_final')
pep2dna('Tandem.Omssa.FDR.pep.splicing.final.pos.3.3.curate','/netshare1/home1/people/hansun/GeneFusionsFinal/9_FinalDataBase/fusion_splicing_uniprot_ensembl_contaminated_final')
