'''
dict1=dict()
inFile=open('/netshare1/home1/people/hansun/Data/GenomeSeq/Human/ucsc.hg19.fasta.fa')
ouFile=open('chr.len','w')

for line in inFile :
    line=line.strip()
    if line.find('>')==0 :
        head=line.strip('>')
    else :
        dict1[head]=len(line)
inFile.close()

for key in dict1 :
    ouFile.write(key+'\t'+str(dict1[key])+'\n')
ouFile.close()
'''
import numpy as np
dict1=dict()
inFile1=open('hg19.chr.len')
for line in inFile1 :
    line=line.strip()
    fields=line.split('\t')
    chr=fields[0]
    length=int(fields[1])
    dict1[chr]=length

inFile1.close()

ouFile=open('hg19.refGene.stat','w')
ouFile.write('chr'+'\t'+'total_len'+'\t'+'exon_len'+'\t'+'intron_len'+'\t'+'utr_len'+'\t'+'nr_len'+'\t'+'inter_len'+'\n')

chrs=['chr1','chr2','chr3','chr4','chr5','chr6','chr7','chr8','chr9','chr10','chr11','chr12','chr13','chr14'
,'chr15','chr16','chr17','chr18','chr19','chr20','chr21','chr22','chrX','chrY','chrM']




for ch in chrs :
    chr=np.zeros((5,dict1[ch]))
    
    inFile=open('hg19_refGene.txt')
    
    for line in inFile :
        line=line.strip('\r\n')
        fields=line.split('\t')
        c=fields[2]
        if c==ch :
            if fields[1].find('NM')==0 :
                exonStart=[int(i) for i in fields[9].split(',')[0:-1]]
                exonEnd=[int(i) for i in fields[10].split(',')[0:-1]]
                for i in range(len(exonStart)) :
                    for j in range(exonStart[i],exonEnd[i]) :
                        chr[0][j]=1
    
                cdsStart=[int(fields[6])]
                cdsEnd=[int(fields[7])]
                for i in range(len(cdsStart)) :
                    for j in range(cdsStart[i],cdsEnd[i]) :
                        chr[1][j]=1
    
                txStart=[int(fields[4])]
                txEnd=[int(fields[5])]
                for i in range(len(txStart)) :
                    for j in range(txStart[i],txEnd[i]) :
                        chr[2][j]=1
                        chr[4][j]=1
    
            if fields[1].find('NR')==0 :
                nrStart=[int(fields[4])]
                nrEnd=[int(fields[5])]
                for i in range(len(nrStart)) :
                    for j in range(nrStart[i],nrEnd[i]) :
                        chr[3][j]=1
                        chr[4][j]=1
    
    inFile.close()
    
    
    total_len=dict1[ch]
    exon_len=chr[0].sum()
    intron_len=chr[1].sum()-chr[0].sum()
    utr_len=chr[2].sum()-chr[1].sum()
    nr_len=chr[3].sum()
    inter_len=total_len-chr[4].sum()
    
    ouFile.write(ch+'\t'+str(total_len)+'\t'+str(exon_len)+'\t'+str(intron_len)+'\t'+str(utr_len)+'\t'+str(nr_len)+'\t'+str(inter_len)+'\n')

ouFile.close()





























'''

inFile=open('hg19_refGene.txt')
dict1=dict()

for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    type=fields[1].split('_')[0]
    dict1.setdefault(type,0)
    dict1[type]+=1

inFile.close()

for key in dict1 :
    print(key+'\t'+str(dict1[key]))
'''
