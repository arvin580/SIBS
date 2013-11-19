import re
D = {}
inFile = open('Peptides-Identified-Second-unSpec')
ouFile = open('Peptides-Identified-Second-unSpec-single_SNV', 'w')

while True:
    line1 = inFile.readline().strip()
    line2 = inFile.readline().strip()
    if line1:
        s = re.search(r'\s(\w+)\sVARIATION', line1)
        if s:
            pep=s.group(1)
            D.setdefault(pep, [])
            D[pep].append(line1+'\n'+line2)
    else:
        break
inFile.close()

for k in D:
    if len(D[k]) == 1:
        ouFile.write(D[k][0] + '\n')
ouFile.close()
