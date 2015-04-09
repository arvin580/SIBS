def uniqueList(inlist):
    oulist=list()
    for item in inlist :
        if item not in oulist :
            oulist.append(item)
    return oulist


list1=list()

inFile=open('sum_snp.exome_combined.sorted.pass012.new.nonsyn.genesorted.tpvalue.fd3type')
ouFile=open('sum_snp.exome_combined.sorted.pass012.new.nonsyn.genesorted.tpvalue.fd3type_fd3type','w')

for line in inFile :
    line=line.strip('\r\n')
    fields=line.split('\t')
    if fields[0] :
        ouFile.write(fields[0]+'\t'+fields[6]+'\t'+fields[26]+':'+fields[27]+'\t'+'\t'.join(fields[-20:])+'\n')
        list1.append(fields[0]+'\t'+fields[6])

inFile.close()
ouFile.close()

inFile=open('sum_snp.exome_combined.sorted.pass012.new.nonsyn.genesorted.tpvalue.fd3type_fd3type')
ouFile=open('sum_snp.exome_combined.sorted.pass012.new.nonsyn.genesorted.tpvalue.fd3type_fd3type.2','w')
dict1=dict()
for line in inFile :
    line=line.strip('\r\n')
    fields=line.split('\t')
    dict1.setdefault(fields[0]+'\t'+fields[1],[0]*20)
    for i,item in enumerate(fields[3:]) :
        dict1[fields[0]+'\t'+fields[1]][i]+=int(item)

inFile.close()

for key in uniqueList(list1) :
    ouFile.write(key+'\t'+'\t'.join([str(i) for i in dict1[key]])+'\n')
ouFile.close()
