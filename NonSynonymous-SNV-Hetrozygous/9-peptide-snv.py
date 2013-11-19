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
            D.setdefault(pep, 0)
            D[pep] += 1
    else:
        break
inFile.close()
for k in D:
    if D[k] == 1:
        print(k)
ouFile.close()
