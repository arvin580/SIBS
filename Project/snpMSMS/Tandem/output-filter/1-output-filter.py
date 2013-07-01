import os

DIR = '../output'
files = os.listdir(DIR)

ouFile1 = open('Liver-SNV-INDEL-new','w')
ouFile3 = open('Liver-Known-Protein','w')
ouFile4 = open('Liver-SNV-INDEL-REVERSE','w')
for f in files:
    if f[-8:] == '.txt.fdr':
        inFile = open(DIR + '/' + f)
        fn = f.split('.')[0]
        for line in inFile:
            if line.find('REVERSE')!=-1:
                ouFile4.write(fn+'.'+line)
            elif line.find('chromosome') != -1:
                ouFile3.write(fn+'.'+line)
            #elif line.find('ALT')!=-1 and line.find('REF') == -1:
            #    ouFile2.write(line)
            #if line.find('REF')!=-1:
            #    ouFile1.write(line)
            else:
                ouFile1.write(fn+'.'+line)
        inFile.close()

ouFile1.close()
#ouFile2.close()
ouFile3.close()
ouFile4.close()


