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


multi_calling_split('sum_indel.exome_summary.012',[-10,-9,-8,-7,-6,-5,-4,-3,-2,-1],['INDEL.exome.nopass.ICC10A','INDEL.exome.nopass.ICC1A','INDEL.exome.nopass.ICC2A','INDEL.exome.nopass.ICC3A','INDEL.exome.nopass.ICC4A','INDEL.exome.nopass.ICC5A','INDEL.exome.nopass.ICC6A','INDEL.exome.nopass.ICC7A','INDEL.exome.nopass.ICC8A','INDEL.exome.nopass.ICC9A'])
multi_calling_split('sum_indel2.exome_summary.012',[-10,-9,-8,-7,-6,-5,-4,-3,-2,-1],['INDEL.exome.nopass.CHC10A','INDEL.exome.nopass.CHC1A','INDEL.exome.nopass.CHC2A','INDEL.exome.nopass.CHC3A','INDEL.exome.nopass.CHC4A','INDEL.exome.nopass.CHC5A','INDEL.exome.nopass.CHC6A','INDEL.exome.nopass.CHC7A','INDEL.exome.nopass.CHC8A','INDEL.exome.nopass.CHC9A'])
multi_calling_split('sum_indel34.exome_summary.012',[-8,-7,-6,-5,-4,-3,-2,-1],['INDEL.exome.nopass.ICC10B','INDEL.exome.nopass.ICC4B','INDEL.exome.nopass.ICC5B','INDEL.exome.nopass.ICC9B','INDEL.exome.nopass.CHC10B','INDEL.exome.nopass.CHC5B','INDEL.exome.nopass.CHC6B','INDEL.exome.nopass.CHC7B'])

multi_calling_split('sum_indel.genome_summary.012',[-10,-9,-8,-7,-6,-5,-4,-3,-2,-1],['INDEL.genome.nopass.ICC10A','INDEL.genome.nopass.ICC1A','INDEL.genome.nopass.ICC2A','INDEL.genome.nopass.ICC3A','INDEL.genome.nopass.ICC4A','INDEL.genome.nopass.ICC5A','INDEL.genome.nopass.ICC6A','INDEL.genome.nopass.ICC7A','INDEL.genome.nopass.ICC8A','INDEL.genome.nopass.ICC9A'])
multi_calling_split('sum_indel2.genome_summary.012',[-10,-9,-8,-7,-6,-5,-4,-3,-2,-1],['INDEL.genome.nopass.CHC10A','INDEL.genome.nopass.CHC1A','INDEL.genome.nopass.CHC2A','INDEL.genome.nopass.CHC3A','INDEL.genome.nopass.CHC4A','INDEL.genome.nopass.CHC5A','INDEL.genome.nopass.CHC6A','INDEL.genome.nopass.CHC7A','INDEL.genome.nopass.CHC8A','INDEL.genome.nopass.CHC9A'])
multi_calling_split('sum_indel34.genome_summary.012',[-8,-7,-6,-5,-4,-3,-2,-1],['INDEL.genome.nopass.ICC10B','INDEL.genome.nopass.ICC4B','INDEL.genome.nopass.ICC5B','INDEL.genome.nopass.ICC9B','INDEL.genome.nopass.CHC10B','INDEL.genome.nopass.CHC5B','INDEL.genome.nopass.CHC6B','INDEL.genome.nopass.CHC7B'])

