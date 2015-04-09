inFile1=open('3A.bam.predSV.txt','r')

dict1=dict()
for line in inFile1 :
    fields=line.split()
    dict1.setdefault(fields[8],0)
    dict1[fields[8]]+=1

inFile1.close()
