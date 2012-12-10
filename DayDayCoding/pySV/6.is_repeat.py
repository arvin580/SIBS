import sys 
inFile = open('/netshare1/home1/people/hansun/GATK/bundle/ucsc.hg19.fasta')

dict1={}
for line in inFile :
    line=line.strip()
    if line.find('>')==0 :
        title=line.strip('>')
        dict1[title]=[]
    else :   
        dict1[title].append(line)
inFile.close()

for key in dict1 :
    dict1[key]=''.join(dict1[key])

def isRepeat(inF):
    inFile = open(inF)
    ouFile1 = open(inF+'.is.repeat','w')
    ouFile2 = open(inF+'.not.repeat','w')

    while True:
        line1 = inFile.readline()
        line2 = inFile.readline()
        if not line1:
            fields1 = line1.split('\t')
            fields2 = line2.split('\t')
            ch1 = fields1[]
            ch2 = fields2[]
            pos1 = int(fields1[])
            pos2 = int(fields2[])

        else:
            break


    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        ch = fields[1]
        pos = int(fields[2])-1
        if dict1[ch][pos].islower():
            ouFile1.write(line+'\n')
        else:
            ouFile2.write(line+'\n')

    inFile.close()
    ouFile1.close()
    ouFile2.close()

snv('SNV.exome.ICC4A')

