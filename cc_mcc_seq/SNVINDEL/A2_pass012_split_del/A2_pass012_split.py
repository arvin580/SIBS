import re
def multi_calling_split(iFile,samplePosList,sampleNameList) :
    for i,item in enumerate(samplePosList) :
        inFile=open(iFile)
        ouFile=open(sampleNameList[i],'w')
        for line in inFile :
            line=line.rstrip()
            fields=line.split('\t')
            if int(fields[item])>0 :
                gene=fields[1]
                gene=re.split(r'[,;(]',gene)[0]
                ouFile.write('\t'.join([gene]+fields[21:26]+[fields[item]])+'\n')
        ouFile.close()
        inFile.close()


multi_calling_split('sum_snp.exome_summary.pass012',[-10,-9,-8,-7,-6,-5,-4,-3,-2,-1],['SNV.exome.ICC10A','SNV.exome.ICC1A','SNV.exome.ICC2A','SNV.exome.ICC3A','SNV.exome.ICC4A','SNV.exome.ICC5A','SNV.exome.ICC6A','SNV.exome.ICC7A','SNV.exome.ICC8A','SNV.exome.ICC9A'])
multi_calling_split('sum_snp2.exome_summary.pass012',[-10,-9,-8,-7,-6,-5,-4,-3,-2,-1],['SNV.exome.CHC10A','SNV.exome.CHC1A','SNV.exome.CHC2A','SNV.exome.CHC3A','SNV.exome.CHC4A','SNV.exome.CHC5A','SNV.exome.CHC6A','SNV.exome.CHC7A','SNV.exome.CHC8A','SNV.exome.CHC9A'])
multi_calling_split('sum_snp34.exome_summary.pass012',[-8,-7,-6,-5,-4,-3,-2,-1],['SNV.exome.ICC10B','SNV.exome.ICC4B','SNV.exome.ICC5B','SNV.exome.ICC9B','SNV.exome.CHC10B','SNV.exome.CHC5B','SNV.exome.CHC6B','SNV.exome.CHC7B'])

multi_calling_split('sum_snp.genome_summary.pass012',[-10,-9,-8,-7,-6,-5,-4,-3,-2,-1],['SNV.genome.ICC10A','SNV.genome.ICC1A','SNV.genome.ICC2A','SNV.genome.ICC3A','SNV.genome.ICC4A','SNV.genome.ICC5A','SNV.genome.ICC6A','SNV.genome.ICC7A','SNV.genome.ICC8A','SNV.genome.ICC9A'])
multi_calling_split('sum_snp2.genome_summary.pass012',[-10,-9,-8,-7,-6,-5,-4,-3,-2,-1],['SNV.genome.CHC10A','SNV.genome.CHC1A','SNV.genome.CHC2A','SNV.genome.CHC3A','SNV.genome.CHC4A','SNV.genome.CHC5A','SNV.genome.CHC6A','SNV.genome.CHC7A','SNV.genome.CHC8A','SNV.genome.CHC9A'])
multi_calling_split('sum_snp34.genome_summary.pass012',[-8,-7,-6,-5,-4,-3,-2,-1],['SNV.genome.ICC10B','SNV.genome.ICC4B','SNV.genome.ICC5B','SNV.genome.ICC9B','SNV.genome.CHC10B','SNV.genome.CHC5B','SNV.genome.CHC6B','SNV.genome.CHC7B'])

