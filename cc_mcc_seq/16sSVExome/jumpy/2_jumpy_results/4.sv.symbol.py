def uniqueList(inlist):
    oulist=list()
    for item in inlist :
        if item not in oulist :
            oulist.append(item)
    return oulist

def symbol(inF):
    inFile = open(inF)
    ouFile = open(inF+'.symbol','w')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        ouFile.write(fields[0]+'\t')
        gene = []
        for item in fields[1:]:
            its =item.split(':')
            if len(its) == 6 :
                gene.append(its[-2]+':'+its[-1])
            
        ouFile.write('\t'.join(uniqueList(gene)))
        ouFile.write('\n')
    inFile.close()
    ouFile.close()

symbol('1.sv.stat.gene')
symbol('1.sv.stat.exon')
