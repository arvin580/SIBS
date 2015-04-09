samples = ['ICC4A','ICC4B','ICC5A','ICC5B','ICC9A','ICC9B','ICC10A','ICC10B',
           'CHC5A','CHC5B','CHC6A','CHC6B','CHC7A','CHC7B','CHC10A','CHC10B']
def seq():
    D = {}
    for sp in samples:
        inFile = open(sp+'.inv.br.fasta.blasted.filtered.seq1')
        s = []
        for line in inFile:
            line = line.rstrip()
            fields = line.split('\t')
            if fields[0].find(':')!=0:
                s.append('\t'.join(fields[0:-1]))
            else:
                k =sp+':'+':'.join(fields[0].split(':')[1:4])
                D[k] = s
                s= []
    
        inFile.close()
    return D

#d = seq()
#for x in d['CHC10A:chr1:187464828:187466727']:
#    print(x)

def symbol(inF):
    D = {}
    inFile = open(inF)
    ouFile = open(inF+'.reads','w')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        for fd in fields[1:]:
            fds = fd.split(':')
            if len(fds)==4:
                val = fields[0]+':'+':'.join(fds[0:3])
                D.setdefault(fds[3],[])
                D[fds[3]].append(val)
    inFile.close()

    d = D.items()
    d.sort(cmp=lambda x,y:cmp(len(x[1]),len(y[1])), reverse = True)
    
    sq = seq()
    for item in d :
        for it in item[1]:
            ouFile.write('>'+item[0]+':'+it+'\n')
            s = sq[it]
            for x in s :
                ouFile.write(x+'\n')
    
    ouFile.close()

symbol('1.sv.stat.exon')
symbol('1.sv.stat.gene')

