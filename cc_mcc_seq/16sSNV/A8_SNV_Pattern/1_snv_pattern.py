from PyPlot.PyPlotClass import *
import numpy as np

def snv_pattern(iFileList,xLabel) :
    N=len(iFileList)
    dict1=dict()
    for i,item in enumerate(iFileList) :
        inFile=open(item)
        for line in inFile :
            line=line.strip()
            fields=line.split('\t')
            type=fields[4]+fields[5]
            dict1.setdefault(type,[0]*N)
            dict1[type][i]+=1
        inFile.close()

    dict1['T>G/A>C']=list(np.array(dict1['TG'])+np.array(dict1['AC']))
    dict1['T>C/A>G']=list(np.array(dict1['TC'])+np.array(dict1['AG']))
    dict1['T>A/A>T']=list(np.array(dict1['TA'])+np.array(dict1['AT']))
    dict1['C>A/G>T']=list(np.array(dict1['CA'])+np.array(dict1['GT']))
    dict1['C>G/G>C']=list(np.array(dict1['CG'])+np.array(dict1['GC']))
    dict1['C>T/G>A']=list(np.array(dict1['CT'])+np.array(dict1['GA']))


    dict1['SNV']=list(np.array(dict1['T>G/A>C'])+np.array(dict1['T>C/A>G'])+np.array(dict1['T>A/A>T'])+np.array(dict1['C>A/G>T'])+np.array(dict1['C>G/G>C'])+np.array(dict1['C>T/G>A']))

    pp=PyPlot('SNV_Pattern.pdf')
    pp.single_bar_multi_bar_vertical_proportion(dict1['SNV'],[dict1['T>G/A>C'],dict1['T>C/A>G'],dict1['T>A/A>T'],dict1['C>A/G>T'],dict1['C>G/G>C'],dict1['C>T/G>A']],xLabel)


snv_pattern(['SNV.genome.somatic.ICC4','SNV.genome.somatic.ICC5','SNV.genome.somatic.ICC9','SNV.genome.somatic.ICC10','SNV.genome.somatic.CHC5','SNV.genome.somatic.CHC6','SNV.genome.somatic.CHC7','SNV.genome.somatic.CHC10'],['ICC4','ICC5','ICC9','ICC10','CHC5','CHC6','CHC7','CHC10'])
