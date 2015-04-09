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


multi_calling_split('sum_snp.exome_summary.012',[-10,-9,-8,-7,-6,-5,-4,-3,-2,-1],['SNV.exome.nopass.ICC10A','SNV.exome.nopass.ICC1A','SNV.exome.nopass.ICC2A','SNV.exome.nopass.ICC3A','SNV.exome.nopass.ICC4A','SNV.exome.nopass.ICC5A','SNV.exome.nopass.ICC6A','SNV.exome.nopass.ICC7A','SNV.exome.nopass.ICC8A','SNV.exome.nopass.ICC9A'])
multi_calling_split('sum_snp2.exome_summary.012',[-10,-9,-8,-7,-6,-5,-4,-3,-2,-1],['SNV.exome.nopass.CHC10A','SNV.exome.nopass.CHC1A','SNV.exome.nopass.CHC2A','SNV.exome.nopass.CHC3A','SNV.exome.nopass.CHC4A','SNV.exome.nopass.CHC5A','SNV.exome.nopass.CHC6A','SNV.exome.nopass.CHC7A','SNV.exome.nopass.CHC8A','SNV.exome.nopass.CHC9A'])
multi_calling_split('sum_snp34.exome_summary.012',[-8,-7,-6,-5,-4,-3,-2,-1],['SNV.exome.nopass.ICC10B','SNV.exome.nopass.ICC4B','SNV.exome.nopass.ICC5B','SNV.exome.nopass.ICC9B','SNV.exome.nopass.CHC10B','SNV.exome.nopass.CHC5B','SNV.exome.nopass.CHC6B','SNV.exome.nopass.CHC7B'])

multi_calling_split('sum_snp.genome_summary.012',[-10,-9,-8,-7,-6,-5,-4,-3,-2,-1],['SNV.genome.nopass.ICC10A','SNV.genome.nopass.ICC1A','SNV.genome.nopass.ICC2A','SNV.genome.nopass.ICC3A','SNV.genome.nopass.ICC4A','SNV.genome.nopass.ICC5A','SNV.genome.nopass.ICC6A','SNV.genome.nopass.ICC7A','SNV.genome.nopass.ICC8A','SNV.genome.nopass.ICC9A'])
multi_calling_split('sum_snp2.genome_summary.012',[-10,-9,-8,-7,-6,-5,-4,-3,-2,-1],['SNV.genome.nopass.CHC10A','SNV.genome.nopass.CHC1A','SNV.genome.nopass.CHC2A','SNV.genome.nopass.CHC3A','SNV.genome.nopass.CHC4A','SNV.genome.nopass.CHC5A','SNV.genome.nopass.CHC6A','SNV.genome.nopass.CHC7A','SNV.genome.nopass.CHC8A','SNV.genome.nopass.CHC9A'])
multi_calling_split('sum_snp34.genome_summary.012',[-8,-7,-6,-5,-4,-3,-2,-1],['SNV.genome.nopass.ICC10B','SNV.genome.nopass.ICC4B','SNV.genome.nopass.ICC5B','SNV.genome.nopass.ICC9B','SNV.genome.nopass.CHC10B','SNV.genome.nopass.CHC5B','SNV.genome.nopass.CHC6B','SNV.genome.nopass.CHC7B'])

