import numpy as np
def chrom_pos() :
    chrom_dict=dict()
    inFile=open('/netshare1/home1/people/hansun/Data/hg19_refGene/hg19.chr.len')
    for line in inFile :
        line=line.strip()
        fields=line.split()
        chrom_dict[fields[0]]=int(fields[1])
    inFile.close()

    chrom_pos_dict=dict()
    for ch in chrom_dict:
        chrom_pos_dict[ch]=np.zeros(chrom_dict[ch])
    return chrom_pos_dict

chroms=['chr1','chr2','chr3','chr4','chr5','chr6','chr7','chr8','chr9','chr10','chr11','chr12','chr13','chr14','chr15','chr16','chr17','chr18','chr19','chr20','chr21','chr22','chrX','chrY']
#hs=['hs1','hs2','hs3','hs4','hs5','hs6','hs7','hs8','hs9','hs10','hs11','hs12','hs13','hs14','hs15','hs16','hs17','hs18','hs19','hs20','hs21','hs22','hsX','hsY']
hs = chroms
inter=1000000

def sample_scatter(inF) :
    ouFile=open(inF+'.sca','w')
    chrom_pos_dict=chrom_pos()
    
    inFile=open(inF)
    for line in inFile :
        line=line.strip()
        fields=line.split()
        chrom_pos_dict[fields[1]][int(fields[2])]=1
    inFile.close()

    for c,ch in enumerate(chroms) :
        pos=chrom_pos_dict[ch]
        for i in xrange(0,len(pos),inter) :
            n=pos[i:i+inter].sum()
            ouFile.write(hs[c]+'\t'+str(i)+'\t'+str(i+inter-1)+'\t'+str(n)+'\n')
    ouFile.close()

sample_scatter('SNV.genome.ICC4A.not.repeat')
sample_scatter('SNV.genome.ICC4B.not.repeat')
sample_scatter('SNV.genome.somatic.ICC4.not.repeat')

sample_scatter('SNV.genome.ICC5A.not.repeat')
sample_scatter('SNV.genome.ICC5B.not.repeat')
sample_scatter('SNV.genome.somatic.ICC5.not.repeat')


sample_scatter('SNV.genome.ICC9A.not.repeat')
sample_scatter('SNV.genome.ICC9B.not.repeat')
sample_scatter('SNV.genome.somatic.ICC9.not.repeat')

sample_scatter('SNV.genome.ICC10A.not.repeat')
sample_scatter('SNV.genome.ICC10B.not.repeat')
sample_scatter('SNV.genome.somatic.ICC10.not.repeat')



sample_scatter('SNV.genome.CHC5A.not.repeat')
sample_scatter('SNV.genome.CHC5B.not.repeat')
sample_scatter('SNV.genome.somatic.CHC5.not.repeat')

sample_scatter('SNV.genome.CHC6A.not.repeat')
sample_scatter('SNV.genome.CHC6B.not.repeat')
sample_scatter('SNV.genome.somatic.CHC6.not.repeat')

sample_scatter('SNV.genome.CHC7A.not.repeat')
sample_scatter('SNV.genome.CHC7B.not.repeat')
sample_scatter('SNV.genome.somatic.CHC7.not.repeat')

sample_scatter('SNV.genome.CHC10A.not.repeat')
sample_scatter('SNV.genome.CHC10B.not.repeat')
sample_scatter('SNV.genome.somatic.CHC10.not.repeat')








