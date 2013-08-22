import random
D = {}
inFile = open('/netshare1/home1/people/hansun/Data/HeLa/Illumina/ERR0498-04-05.sam')
for line in range(95):
    inFile.readline()
for line in inFile:
    fields = line.split('\t')
    D[fields[0]] = 1
inFile.close()

def read_random(x):
    ouFile = open('ERR0498-04-05.unmapped.unique.human-viruse-checked-random-'+str(x),'w')
    for n in range(x):
        R = random.sample(D,1175)
        for x in R:
            ouFile.write(x+'\t')
        ouFile.write('\n')
    ouFile.close()

read_random(10000)


