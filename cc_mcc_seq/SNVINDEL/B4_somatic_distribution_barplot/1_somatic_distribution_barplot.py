from PyPlot.PyPlotClass import *
ml=1000000
coding_len = 33319174.0/ml
intron_len = 949184922.0/ml
noncoding_len = 305330955.0/ml
inter_len = 1889047975.0/ml
total_len = 3095693983.0/ml

import numpy as np

def snv_region_based_annotation(iFile) :
    inFile=open(iFile)
    dict1=dict()
    head=inFile.readline()
    for line in inFile :
        line=line.strip()
        fields=line.split('\t')
        dict1[fields[0]]=np.array([int(x) for x in fields[1:]])
    inFile.close()
    pp=PyPlot()
    pp.multi_bar([dict1['Coding'][0:8]/coding_len,dict1['Intronic'][0:8]/intron_len,dict1['NonCoding'][0:8]/noncoding_len,dict1['Intergenic'][0:8]/inter_len,dict1['Genomic'][0:8]/total_len],xLabel=['ICC4','ICC5','ICC9','ICC10','CHC5','CHC6','CHC7','CHC10'],legTitle=['Coding','Intronic','NonCoding','Intergenic','Genomic'])

snv_region_based_annotation('SNV.genome.somatic.distribution')


