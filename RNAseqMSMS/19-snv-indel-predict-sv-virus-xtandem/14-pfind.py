inFile = open('12-pfind/gluc-0.2013_08_09_11_29_02_qry.peptides-pep.pep2')
for line in inFile:
    line = line.strip()
    D[line] = 1
inFile.close()
