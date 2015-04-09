from PyPlot.PyPlotClass import *
from PyStats.PyStatsClass import *

def gene_significant_mutated(iFile,samplePositionList,filename) :
    total_length=0
    total_num=0
    dict1=dict()
    inFile=open('hg19_max_coding_length')
    for line in inFile :
        line=line.rstrip()
        fields=line.split('\t')
        dict1[fields[0]]=int(fields[1])
    inFile.close()


    inFile=open(iFile)
    for line in inFile :
        line=line.rstrip()
        fields=line.split('\t')
        gn=sum([int(fields[x]) for x in samplePositionList]) 
        gl=dict1[fields[0]]
        if gn >0 :
            total_length+=gl
            total_num+=gn
    inFile.close()
    #print(total_length)
    #print(total_num)

    ps=PyStats()
    inFile=open(iFile)
    ouFile=open(iFile+'.'+filename+'.fisher_test','w')
    for line in inFile :
        line=line.rstrip()
        fields=line.split('\t')
        gs=sum([int(fields[x]) for x in samplePositionList]) 
        gl=dict1[fields[0]]
        if gs >0 :
            f=ps.fisher_test([gs,gl,total_num,total_length])
            ouFile.write(str(f)+'\t'+line+'\n')
            #print(str(f)+'\t'+line)
    inFile.close()
    ouFile.close()
    ps.fdr_adjust_file(iFile+'.'+filename+'.fisher_test')


gene_significant_mutated('SNV.exome.somatic.nonsynonymous.geneLevel',[-8,-7,-6,-5],'ICC')
gene_significant_mutated('SNV.exome.somatic.nonsynonymous.geneLevel',[-4,-3,-2,-1],'CHC')
gene_significant_mutated('SNV.exome.somatic.nonsynonymous.geneLevel',[-8,-7,-6,-5,-4,-3,-2,-1],'ICC_CHC')
