import re
D = {}
inFile = open('Peptides-Identified-Second-unSpec')
ouFile = open('Peptides-Identified-Second-unSpec-single_SNV', 'w')

while True:
    line1 = inFile.readline().strip()
    line2 = inFile.readline().strip()
    if line1:
        s = re.search(r'\s(.*?)\sVARIATION', line1)
        if s:
            print(s.group(1))
    else:
        break


inFile.close()
ouFile.close()
