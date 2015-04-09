import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
def get_color(i,N) :
    cm=plt.get_cmap('gist_rainbow')
    return(cm(i/float(N)))

def read_data(inFlist):
    y=[[],[],[],[],[],[],[],[]]
    for i,f in enumerate(inFlist) :
        inFile=open(f)
        for line in inFile :
            line=line.strip()
            fields=line.split()
            y[i].append(float(fields[-1]))
        inFile.close()
    return y

def plot_gene(inF,ax) :
    inFile=open(inF)
    n=-1
    gene=[]
    for line in inFile :
        n+=1
        line=line.strip()
        fields=line.split('\t')
        name=fields[1]
        chrom=fields[2]
        strand=fields[3]
        txStart=int(fields[4])
        txEnd=int(fields[5])
        cdsStart=int(fields[6])
        cdsEnd=int(fields[7])
        exonCount=int(fields[8])
        exonStarts=[int(i) for i in fields[9].split(',')[0:-1]]
        exonEnds=[int(i) for i in fields[10].split(',')[0:-1]]
        score=fields[11]
        name2=fields[12]
        cdsStartStat=fields[13]
        cdsEndStat=fields[14]
        exonFrames=[int(i) for i in fields[15].split(',')[0:-1]]
        gene.append(name2)
        L.append(ax.plot([(txStart-57000000)/10000,(txEnd-57000000)/10000],[105+n*2,105+n*2],linewidth=3,color=get_color(n+8,14)))
    inFile.close()
    return gene


y=read_data(['SNV.genome.somatic.ICC4.sca','SNV.genome.somatic.ICC5.sca','SNV.genome.somatic.ICC9.sca','SNV.genome.somatic.ICC10.sca','SNV.genome.somatic.CHC5.sca','SNV.genome.somatic.CHC6.sca','SNV.genome.somatic.CHC7.sca','SNV.genome.somatic.CHC10.sca'])

fig = plt.figure()
ax=fig.add_subplot(111)
L=[]
for i,item in enumerate(y) :
    L.append(plt.plot(item,color=get_color(i,14)))
ax.set_xlim(1,100)
ax.set_ylim(0,120)
ax.set_xticks([1,20,40,60,80,100])
ax.set_yticks([20,40,60,80,100])
ax.set_xticklabels(['57000000','57200000','57400000','57600000','58000000','57999999'])
ax.set_xlabel('chr6')
ax.set_ylabel('Number of Somatic SNV')
gene=plot_gene('gene_in_chr6_57M_58M',ax)


legTitle=['ICC4','ICC5','ICC9','ICC10','CHC5','CHC6','CHC7','CHC10']+gene
legL=[item[0] for item in L]
ax.legend(legL,legTitle,loc='upper right',bbox_to_anchor=[0.95,0.95])

plt.savefig('SNV_number_Scatter_chr6_57M_58M.pdf')

