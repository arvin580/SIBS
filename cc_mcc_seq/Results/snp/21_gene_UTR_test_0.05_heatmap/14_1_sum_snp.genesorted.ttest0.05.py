def uniqueList(inlist):
    oulist=list()
    for item in inlist :
        if item not in oulist :
            oulist.append(item)
    return oulist

list1=list()

inFile=open('sum_snp.genome_combined.sorted.pass012.new.UTR.genesorted.tpvalue')
ouFile=open('sum_snp.genome_combined.sorted.pass012.new.UTR.genesorted.tpvalue.0.05','w')

for line in inFile :
    line=line.strip('\r\n')
    fields=line.split('\t')
    if float(fields[2])<=0.05 :
        ouFile.write(fields[5]+'\t'+fields[25]+':'+fields[26]+'\t'+'\t'.join(fields[-20:])+'\n')
        list1.append(fields[5])

inFile.close()
ouFile.close()


inFile=open('sum_snp.genome_combined.sorted.pass012.new.UTR.genesorted.tpvalue.0.05')
ouFile=open('sum_snp.genome_combined.sorted.pass012.new.UTR.genesorted.tpvalue.0.05.2','w')

dict1=dict()
for line in inFile :
    line=line.strip('\r\n')
    fields=line.split('\t')
    dict1.setdefault(fields[0],[0]*20)
    for i,item in enumerate(fields[2:]) :
        dict1[fields[0]][i]+=int(item)

inFile.close()

for key in uniqueList(list1) :
    ouFile.write(key+'\t'+'\t'.join([str(i) for i in dict1[key]])+'\n')
ouFile.close()
