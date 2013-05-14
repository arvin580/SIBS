def peptide(inL):
    acids = ['A','R','D','C','Q','E','H','I','G','N','L','K','M','F','P','S','T','W','Y','V']
    L = []
    for item in inL :
        if item.isupper():
            flag1 = 0
            flag2 = 0
            for x in item:
                if x in acids:
                    flag1 += 1
                if x  not in 'ATCG':
                    flag2 += 1
            if flag1 == len(item) and flag2:
                L.append(item)
    return L

inFile = open('/netshare1/home1/people/hansun/Data/Uniprot/human_uniprot_sprot.fa')
D = {}
while True:
    line1 = inFile.readline().strip()
    line2 = inFile.readline().strip()
    if line1:
        D[line1] = line2
    else:
        break
inFile.close()

inFile = open('HeLa-predict-rnaseq-msms')
ouFile1 = open('HeLa-predict-rnaseq-msms-uniprot','w')
ouFile2 = open('HeLa-predict-rnaseq-msms-not-uniprot','w')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    flag = 0
    for item in peptide(fields):
        print(item)
        for k in D:
            if item in D[k]:
                flag += 1
    if flag:
        ouFile1.write(line+'\n')
    else:
        ouFile2.write(line+'\n')

inFile.close()
ouFile1.close()
ouFile2.close()
