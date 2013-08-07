import os
def classification(Dir,cleavage):
    ouFile1 = open('HeLa-peptide-reverse-contaminated','w')
    ouFile2 = open('HeLa-peptide-known','w')
    ouFile3 = open('HeLa-peptide-snv-indel-predict-sv-virus','w')
    Fs = os.listdir(Dir)
    for inF in Fs:
        if inF[-8:] == '.txt.fdr':
            inFile = open(Dir+'/'+inF)
            for line in inFile:
                line = line.strip()
                if line.find('REVERSE:') != -1:
                    ouFile1.write(cleavage+'\t'+line+'\n')
                elif line.find('ENSP000')!=-1:
                    ouFile2.write(cleavage+'\t'+line+'\n')
                elif line.find('GENSCAN000')!=-1:
                    if line.find('PREDICT-SPLICING')!=-1:
                        ouFile3.write(cleavage+'\t'+'PREDICT-SPLICING'+'\t'+line+'\n')
                    else:
                        ouFile3.write(cleavage+'\t'+'PREDICT'+'\t'+line+'\n')
                elif line.find('SNV:')!=-1:
                    ouFile3.write(cleavage+'\t'+'SNV'+'\t'+line+'\n')
                elif line.find('INDEL:')!=-1:
                    ouFile3.write(cleavage+'\t'+'INDEL'+'\t'+line+'\n')
                elif line.find('VIRUS:')!=-1:
                    if line.find('HUMAN-VIRUS:')!=-1:
                        ouFile3.write(cleavage+'\t'+'HUMAN-VIRUS'+'\t'+line+'\n')
                    else:
                        ouFile3.write(cleavage+'\t'+'VIRUS'+'\t'+line+'\n')
                elif line.find('SV:')!=-1:
                    if line.find('Deletion')!=-1:
                        ouFile3.write(cleavage+'\t'+'SV-DELETION'+'\t'+line+'\n')
                    elif line.find('Duplication')!=-1:
                        ouFile3.write(cleavage+'\t'+'SV-DUPLICATION'+'\t'+line+'\n')
                    elif line.find('Inversion')!=-1:
                        ouFile3.write(cleavage+'\t'+'SV-INVERSION'+'\t'+line+'\n')
                    elif line.find('Translocation')!=-1:
                        ouFile3.write(cleavage+'\t'+'SV-TRANSLOCATION'+'\t'+line+'\n')
            
            inFile.close()
    ouFile1.close()
    ouFile2.close()
    ouFile3.close()

classification('../output','Trypsin')
#classification('HeLa-variant-LysC-evidence-unique','LysC')
#classification('HeLa-variant-GluC-evidence-unique','GluC')
