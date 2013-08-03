import os
def classification(Dir,cleavage):
    ouFile1 = open('HeLa-peptide-reverse-contaminated','w')
    ouFile2 = open('HeLa-peptide-known','w')
    ouFile3 = open('HeLa-peptide-snv-indel-predict-sv-virus','w')

    Fs = os.listdir(Dir)
    for inF in Fs:
        if inF[] == '':
            inFile = open(inF)
            for line in inFile:
                line = line.strip()
                fields = line.split('\t')
                if fields[47] or fields[48]:
                    ouFile1.write(cleavage+'\t'+line+'\n')
                if fields[10].find('ENSP')!=-1:
                    ouFile2.write(cleavage+'\t'+line+'\n')
                elif fields[10].find('GENSCAN')!=-1:
                    if fields[10].find('PREDICT-SPLICING')!=-1:
                        ouFile3.write(cleavage+'\t'+'PREDICT-SPLICING'+'\t'+line+'\n')
                    else:
                        ouFile3.write(cleavage+'\t'+'PREDICT'+'\t'+line+'\n')
                elif fields[10].find('SNV')!=-1:
                    ouFile3.write(cleavage+'\t'+'SNV'+'\t'+line+'\n')
                elif fields[10].find('INDEL')!=-1:
                    ouFile3.write(cleavage+'\t'+'INDEL'+'\t'+line+'\n')
                elif fields[10].find('VIRUS')!=-1:
                    if fields[10].find('HUMAN-VIRUS')!=-1:
                        ouFile3.write(cleavage+'\t'+'HUMAN-VIRUS'+'\t'+line+'\n')
                    else:
                        ouFile3.write(cleavage+'\t'+'VIRUS'+'\t'+line+'\n')
                elif fields[10].find('SV')!=-1:
                    if fields[10].find('Deletion')!=-1:
                        ouFile3.write(cleavage+'\t'+'SV-DELETION'+'\t'+line+'\n')
                    elif fields[10].find('Duplication')!=-1:
                        ouFile3.write(cleavage+'\t'+'SV-DUPLICATION'+'\t'+line+'\n')
                    elif fields[10].find('Inversion')!=-1:
                        ouFile3.write(cleavage+'\t'+'SV-INVERSION'+'\t'+line+'\n')
                    elif fields[10].find('Translocation')!=-1:
                        ouFile3.write(cleavage+'\t'+'SV-TRANSLOCATION'+'\t'+line+'\n')
            
            inFile.close()
    ouFile1.close()
    ouFile2.close()
    ouFile3.close()

classification('../output','Trypsin')
#classification('HeLa-variant-LysC-evidence-unique','LysC')
#classification('HeLa-variant-GluC-evidence-unique','GluC')
