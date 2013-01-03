inFile = open('D6EAE8E9016-Alignment.txt')
D = {}
for line in inFile:
    line = line.strip()
    if line.find('Query  1  ')==0:
        fields = line.split()
        D[fields[2]]=1
inFile.close()

D2= {}
inFile = open('Tandem.Ossma.genefusion.splicing.fa')
for line in inFile:
    line = line.strip()
    if line.find('>')!=0:
        D2[line]=1
inFile.close()


for k in D:
    if k in D2:
        print(k)
