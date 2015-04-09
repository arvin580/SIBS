inFile=open('sum_snp.genome_combined.sorted.pass012')
n=0
dbsnp135=0
dbsnp132=0
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    if int(fields[-2])!=0 :
        n+=1
        if fields[8].find('rs')==0 :
            dbsnp135+=1
        if fields[28].find('rs')==0 :
            dbsnp132+=1
inFile.close()

print(n)
print(dbsnp132)
print(dbsnp135)
