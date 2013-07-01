import os

DIR = '../output2'
files = os.listdir(DIR)

ouFile1_1 = open('HeLa-SV-Duplication','w')
ouFile1_2 = open('HeLa-SV-Deletion','w')
ouFile1_3 = open('HeLa-SV-Inversion','w')
ouFile1_4 = open('HeLa-SV-Translocation','w')
ouFile2 = open('HeLa-Predict-Splicing','w')
ouFile3 = open('HeLa-Predict','w')
ouFile4 = open('HeLa-Known-Protein','w')
ouFile5 = open('HeLa-Predict-Splicing-SV-REVERSE','w')
for f in files:
    if f[-8:] == '.txt.fdr':
        inFile = open(DIR + '/' + f)
        for line in inFile:
            if line.find('REVERSE')!=-1:
                ouFile5.write(line)
            elif line.find('ENSP00')!=-1 :
                ouFile4.write(line)
            elif line.find('genscan') != -1:
                ouFile3.write(line)
            elif line.find('Deletion')!=-1:
                ouFile1_2.write(line)
            elif line.find('Duplication')!=-1:
                ouFile1_1.write(line)
            elif line.find('Inversion')!=-1:
                ouFile1_3.write(line)
            elif line.find('Translocation')!=-1:
                ouFile1_4.write(line)
            if line.find('REVERSE')==-1 and line.find('ENSP')==-1 and line.find('PREDICT-SPLICING')!=-1:
                ouFile2.write(line)
        inFile.close()

ouFile1_1.close()
ouFile1_2.close()
ouFile1_3.close()
ouFile1_4.close()
ouFile2.close()
ouFile3.close()
ouFile4.close()


