inFile=open('/netshare1/home1/people/hansun/GeneFusionsFinal/8_AnnotatedProtein/ensemble_protein')
ensembl=inFile.read()
inFile.close()

inFile=open('/netshare1/home1/people/hansun/GeneFusionsFinal/8_AnnotatedProtein/uniprot_human')
uniprot=inFile.read()
inFile.close()

inFile=open('/netshare1/home1/people/hansun/GeneFusionsFinal/7_ContaminatedProtein/contaminanted_comb_reverse')
contaminated=inFile.read()
inFile.close()


def pep(inF) :
    inFile=open(inF)
    ouFile=open(inF+'.not.annotated','w')
    ouFile2=open(inF+'.annotated','w')
    for line in inFile :
        line=line.strip()
        fields=line.split('\t')
        pep=fields[0]
        if ensembl.find(pep)==-1  and uniprot.find(pep)==-1  and contaminated.find(pep)==-1 :
            ouFile.write(line+'\n')
        else :
            ouFile2.write(line+'\n')
    inFile.close()
    ouFile.close()
    ouFile2.close()

def pep2(inF) :
    inFile=open(inF)
    ouFile=open(inF+'.not.annotated','w')
    ouFile2=open(inF+'.annotated','w')
    for line in inFile :
        line=line.strip()
        fields=line.split('\t')
        pep=fields[0]
        if ensembl.find(pep)==-1  and uniprot.find(pep)==-1  :
            ouFile.write(line+'\n')
        else :
            ouFile2.write(line+'\n')
    inFile.close()
    ouFile.close()
    ouFile2.close()


pep('FDR.pep.genefusions')
pep('FDR.pep.splicing')
pep('FDR.pep.annotated')
pep2('FDR.pep.contaminated')



