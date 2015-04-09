inFile=open('sum_snp.genome_combined.sorted.pass012.new')
ouFile=open('sum_snp.genome_combined.sorted.pass012.new.dis','w')

dis=[0]*21
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    num=0
    for item in fields[-20:] :
        if item!='0' :
            num+=1
    dis[num]+=1
    if num==20:
        print(line)

inFile.close()

for item in dis :
    ouFile.write(str(item)+'\n')
ouFile.close()



inFile=open('sum_snp.exome_combined.sorted.pass012.new')
ouFile=open('sum_snp.exome_combined.sorted.pass012.new.dis','w')

dis=[0]*21
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    num=0
    for item in fields[-20:] :
        if item!='0' :
            num+=1
    dis[num]+=1
    if num==20:
        print(line)


inFile.close()

for item in dis :
    ouFile.write(str(item)+'\n')


ouFile.close()

