from PyPlot.PyPlotClass import *

def snv_region_based_annotation(iFile) :
    inFile=open(iFile)
    dict1=dict()
    head=inFile.readline()
    for line in inFile :
        line=line.strip()
        fields=line.split('\t')
        dict1[fields[0]]=[int(x) for x in fields[1:]]
    inFile.close()
    pp=PyPlot()
    pp.multi_bar([dict1['Coding'][0:4],dict1['Intronic'][0:4],dict1['NonCoding'][0:4],dict1['Intergenic'][0:4],dict1['Genomic'][0:4]])

snv_region_based_annotation('sum_snp.somatic.distribution')


