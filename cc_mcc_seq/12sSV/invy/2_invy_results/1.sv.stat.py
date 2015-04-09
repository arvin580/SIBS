from operator import itemgetter, attrgetter
samples=['ICC1A','ICC2A','ICC3A','ICC6A','ICC7A','ICC8A',
         'CHC1A','CHC2A','CHC3A','CHC4A','CHC8A','CHC9A']

chrs=['chr1','chr2','chr3','chr4','chr5','chr6','chr7','chr8','chr9','chr10','chr11','chr12','chr13','chr14','chr15','chr16','chr17','chr18','chr19','chr20','chr21','chr22','chrX','chrY','chrM']

suffix = '.inv.br.fasta.blasted.filtered.head1'
svs = []
ouFile = open('1.sv.stat','w')

def cmp_func(x,y):
    if chrs.index(x[0]) < chrs.index(y[0]):
        return -1
    elif chrs.index(x[0]) > chrs.index(y[0]):
        return 1
    else:
        if x[1] < y[1]:
            return -1
        elif x[1] > y[1]:
            return 1
        else:
            if x[2] < y[2]:
                return -1
            elif x[2] > y[2]:
                return 1
            else:
                return 0

def sv_sort(svs):
    svs_sorted=sorted(svs, cmp=lambda x,y : cmp_func(x,y))
    return svs_sorted

for sp in samples:
    inFile = open(sp + suffix)
    for line in inFile:
        line = line.strip()
        fields = line.split(':')
        sv = [fields[1],int(fields[2]),int(fields[3])]
        svs.append(sv)
    svs_sorted = sv_sort(svs)
    ouFile.write(sp+'\t')
    for item in svs_sorted:
        ouFile.write(':'.join([str(x) for x in item])+'\t')
    ouFile.write('\n')
    svs = []
    inFile.close()
