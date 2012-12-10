import sys 
interval = 100
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
        if line1:
            fields1 = line1.split('\t')
            fields2 = line2.split('\t')
            ch1 = fields1[2]
            ch2 = fields2[2]
            pos1 = int(fields1[3])
            pos2 = int(fields2[3])
            flag1 = 0
            flag2 = 0
            pos1_start = pos1-interval
            pos1_end = pos1+interval
            pos2_start = pos2-interval
            pos2_end = pos2+interval
            if pos1_start < 0:
                pos1_start = 0
            if pos2_start < 0:
                pos2_start = 0
            if pos1_end > len(dict1[ch1]):
                pos1_end = len(dict1[ch1])
            if pos2_end > len(dict1[ch2]):
                pos2_end = len(dict1[ch2])



            for i in range(pos1_start,pos1_end):
                if dict1[ch1][i].islower():
                    flag1 = 1
                    break
            for i in range(pos2_start,pos2_end):
                if dict1[ch2][i].islower():
                    flag2 = 1
                    break
            if flag1 == 0  and flag2 == 0:
                ouFile2.write(line1)
                ouFile2.write(line2)
            else:
                ouFile1.write(line1)
                ouFile1.write(line2)

        else:
            break

    inFile.close()
    ouFile1.close()
    ouFile2.close()

isRepeat(sys.argv[1])

