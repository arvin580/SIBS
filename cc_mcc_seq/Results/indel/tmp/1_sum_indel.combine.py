import csv

dict1=dict()
inFile=open('sum_indel.exome_summary.csv')
csvFile=csv.reader(inFile)
head=csvFile.next()
for fields in csvFile :
    key=fields[0:31]
    key='\t'.join(key)
    dict1.setdefault(key,[0]*28)
    dict1[key][0:14]=fields[31:]

inFile.close()


inFile=open('sum_indel2.exome_summary.csv')
csvFile=csv.reader(inFile)
head=csvFile.next()
for fields in csvFile :
    key=fields[0:31]
    key='\t'.join(key)
    dict1.setdefault(key,[0]*28)
    dict1[key][14:]=fields[31:]

inFile.close()

ouFile=open('sum_indel.exome_combined','w')

ouFile.write('\t'.join(head)+'\n')
for key in dict1 :
    ouFile.write(key+'\t'+'\t'.join([str(i) for i in dict1[key]])+'\n')

ouFile.close()


dict1=dict()
inFile=open('sum_indel.genome_summary.csv')
csvFile=csv.reader(inFile)
head=csvFile.next()
for fields in csvFile :
    key=fields[0:31]
    key='\t'.join(key)
    dict1.setdefault(key,[0]*28)
    dict1[key][0:14]=fields[31:]

inFile.close()


inFile=open('sum_indel2.genome_summary.csv')
csvFile=csv.reader(inFile)
head=csvFile.next()
for fields in csvFile :
    key=fields[0:31]
    key='\t'.join(key)
    dict1.setdefault(key,[0]*28)
    dict1[key][14:]=fields[31:]

inFile.close()

ouFile=open('sum_indel.genome_combined','w')

ouFile.write('\t'.join(head)+'\n')
for key in dict1 :
    ouFile.write(key+'\t'+'\t'.join([str(i) for i in dict1[key]])+'\n')

ouFile.close()

