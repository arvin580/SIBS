import os
def classification(Dir,cleavage):
    ouFile1 = open('HeLa-peptide-Reverse','w')
    ouFile2 = open('HeLa-peptide-Annotated','w')
    ouFile3 = open('HeLa-peptide-LNCRNA','w')
    Fs = os.listdir(Dir)
    for inF in Fs:
        if inF[-8:] == '.txt.fdr':
            inFile = open(Dir+'/'+inF)
            for line in inFile:
                line = line.strip()
                if line.find('REVERSE:') != -1:
                    ouFile1.write(line+'\n')
                elif line.find('ENSP000')!=-1:
                    ouFile2.write('ANNOTATED'+'\t'+line+'\n')
                elif line.find('LNCRNA')!=-1:
                    ouFile3.write('LNCRNA'+'\t'+line+'\n')
            inFile.close()
    ouFile1.close()
    ouFile2.close()
    ouFile3.close()

classification('output','Trypsin')
