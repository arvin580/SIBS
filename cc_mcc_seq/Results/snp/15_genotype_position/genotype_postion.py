import csv

dict1=dict()
inFile=open('sum_snp.genome_summary.csv')
csvFile=csv.reader(inFile)
head=csvFile.next()
for fields in csvFile :
    key='\t'.join(fields[0:23])
    val='\t'.join(fields[24:26])
    dict1[key]=val
inFile.close()

dict2=dict()
inFile=open('sum_snp2.genome_summary.csv')
csvFile=csv.reader(inFile)
head=csvFile.next()
for fields in csvFile :
    key='\t'.join(fields[0:23])
    val='\t'.join(fields[24:26])
    dict2[key]=val
inFile.close()

for key in dict1 :
    if key in dict2 :
        if dict1[key]!=dict2[key] :
            print(key+'\t'+dict1[key]+'\t'+dict2[key])







