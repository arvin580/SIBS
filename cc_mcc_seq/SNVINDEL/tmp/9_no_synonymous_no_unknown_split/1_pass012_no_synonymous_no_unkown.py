import re
def multi_calling_split(file,samplePosList,sampleNameList) :
    for i,item in enumerate(samplePosList) :
        inFile=open(file)
        ouFile=open(file+'.'+sampleNameList[i],'w')
        for line in inFile :
            line=line.rstrip()
            fields=line.split('\t')
            if int(fields[item])>0 :
                gene=fields[1]
                gene=re.split(r'[,;(]',gene)[0]
                ouFile.write('\t'.join([gene]+fields[21:26]+[fields[item]])+'\n')
        ouFile.close()
        inFile.close()



multi_calling_split('sum_snp.exome_summary.pass012.nonsynonymous',[-10,-9,-8,-7,-6,-5,-4,-3,-2,-1],['ICC10A','ICC1A','ICC2A','ICC3A','ICC4A','ICC5A','ICC6A','ICC7A','ICC8A','ICC9A'])
multi_calling_split('sum_snp2.exome_summary.pass012.nonsynonymous',[-10,-9,-8,-7,-6,-5,-4,-3,-2,-1],['CHC10A','CHC1A','CHC2A','CHC3A','CHC4A','CHC5A','CHC6A','CHC7A','CHC8A','CHC9A'])
multi_calling_split('sum_snp34.exome_summary.pass012.nonsynonymous',[-8,-7,-6,-5,-4,-3,-2,-1],['ICC10B','ICC4B','ICC5B','ICC9B','CHC10B','CHC5B','CHC6B','CHC7B'])





