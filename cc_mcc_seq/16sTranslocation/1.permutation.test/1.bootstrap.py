### py 1.fisher.test.py *.paired 
import sys
import random
#from PyStats.PyStatsClass import * 


interval = 100 

def readRef():
    dict1={}
    inFile = open('/netshare1/home1/people/hansun/GATK/bundle/ucsc.hg19.fasta')
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
    return dict1

dict1 = readRef()


def isRepeat(inF):
    inFile = open(inF)
    data_is_repeat = 0
    data_not_repeat = 0
    random_is_repeat = 0
    random_not_repeat = 0

    while True:
        line1 = inFile.readline()
        if line1:
            fields1 = line1.split('\t')
            ch1 = fields1[0]
            ch2 = fields1[1]
            pos1 = int(fields1[2])
            pos2 = int(fields1[3])
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
                data_not_repeat += 1
               
            else:
                data_is_repeat += 1

        else:
            break

    inFile.close()

    #ps=PyStats()
    ouFile.write(str(data_is_repeat)+'\t'+str(data_not_repeat)+'\n')
    #a=ps.fisher_test([data_is_repeat,data_not_repeat,random_is_repeat,random_not_repeat])
    #print(a)

def randomRepeat(inF):
    inFile = open(inF)
    data_is_repeat = 0
    data_not_repeat = 0
    random_is_repeat = 0
    random_not_repeat = 0

    while True:
        line1 = inFile.readline()
        if line1:
            fields1 = line1.split('\t')
            ch1 = fields1[0]
            ch2 = fields1[1]
            pos1 = int(fields1[2])
            pos2 = int(fields1[3])
            flag1 = 0
            flag2 = 0

            pos1_random = random.randint(0,len(dict1[ch1]))
            pos2_random = random.randint(0,len(dict1[ch2]))
            flag1 = 0
            flag2 = 0
            pos1_random_start = pos1_random-interval
            pos1_random_end = pos1_random+interval
            pos2_random_start = pos2_random - interval
            pos2_random_end = pos2_random + interval
            if pos1_random_start < 0:
                pos1_random_start = 0
            if pos2_random_start < 0:
                pos2_random_start = 0
            if pos1_random_end > len(dict1[ch1]):
                pos1_random_end = len(dict1[ch1])
            if pos2_random_end > len(dict1[ch2]):
                pos2_random_end = len(dict1[ch2])

            for i in range(pos1_random_start,pos1_random_end):
                if dict1[ch1][i].islower():
                    flag1 = 1
                    break
            for i in range(pos2_random_start,pos2_random_end):
                if dict1[ch2][i].islower():
                    flag2 = 1
                    break
            if flag1 == 0  and flag2 == 0:
                random_not_repeat += 1
            else:
                random_is_repeat += 1

        else:
            break
    ouFile.write(str(random_is_repeat)+'\t'+str(random_not_repeat)+'\n')
    ouFile.flush()

    inFile.close()

ouFile = open(sys.argv[1]+'.bootstrap', 'w')
isRepeat(sys.argv[1])
for i in range(1000):
    randomRepeat(sys.argv[1])

ouFile.close()

