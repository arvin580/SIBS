inFile=open('/netshare1/home1/people/hansun/GeneFusionsFinal/8_AnnotatedProtein/ensemble_protein')
ensembl=inFile.read()
inFile.close()

inFile=open('/netshare1/home1/people/hansun/GeneFusionsFinal/8_AnnotatedProtein/uniprot_human')
uniprot=inFile.read()
inFile.close()

inFile=open('/netshare1/home1/people/hansun/GeneFusionsFinal/7_ContaminatedProtein/contaminanted_comb_reverse')
contaminated=inFile.read()
inFile.close()


dict1=dict()
inFile=open('FDR.pep.annotated')
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    dict1[fields[0]]=int(fields[1])
inFile.close()

dict2=dict()
inFile=open('FDR.pep.contaminated')
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    dict2[fields[0]]=int(fields[1])
inFile.close()

dict3=dict()
inFile=open('FDR.pep.splicing')
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    dict3[fields[0]]=int(fields[1])
inFile.close()



inFile=open('FDR.pep.splicing')
ouFile=open('FDR.pep.splicing.final','w')
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    pep=fields[0]
    num=int(fields[1])
    if ensembl.find(pep)!=-1 or  uniprot.find(pep)!=-1 :
        dict1.setdefault(pep,0)
        dict1[pep]+=num
    elif contaminated.find(pep)!=-1 :
        dict2.setdefault(pep,0)
        dict2[pep]+=num
    else :
        ouFile.write(line+'\n')
inFile.close()
ouFile.close()


inFile=open('FDR.pep.genefusions')
ouFile=open('FDR.pep.genefusions.final','w')
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    pep=fields[0]
    num=int(fields[1])
    if ensembl.find(pep)!=-1 or  uniprot.find(pep)!=-1 :
        dict1.setdefault(pep,0)
        dict1[pep]+=num
    elif contaminated.find(pep)!=-1 :
        dict2.setdefault(pep,0)
        dict2[pep]+=num
    elif pep in dict3:
        print(pep)
    else :
        ouFile.write(line+'\n')
inFile.close()
ouFile.close()

ouFile=open('FDR.pep.contaminated.final','w')
for key in dict2 :
    pep=key
    num=int(dict2[key])
    if ensembl.find(pep)!=-1 or  uniprot.find(pep)!=-1 :
        dict1.setdefault(pep,0)
        dict1[pep]+=num
        #print(pep)
    else :
        ouFile.write(key+'\t'+str(num)+'\n')
ouFile.close()


ouFile=open('FDR.pep.annotated.final','w')

for key in dict1 :
    ouFile.write(key+'\t'+str(dict1[key])+'\n')

ouFile.close()
