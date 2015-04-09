import re
Q = 10
D = 5
def multi_calling_split(iFile,samplePosList,sampleNameList) :
    for i,item in enumerate(samplePosList) :
        inFile=open(iFile)
        ouFile=open(sampleNameList[i],'w')
        for line in inFile :
            line=line.rstrip()
            fields=line.split('\t')
            if int(fields[item].split(':')[-1])>=Q and int(fields[item+8].split(':')[-1])>=Q \
                    and int(fields[item].split(':')[-2])>=D and int(fields[item+8].split(':')[-2])>=D:
                gene=fields[1]
                gene=re.split(r'[,;(]',gene)[0]
                if fields[item].find('0/1')==0 and fields[item+8].find('0/0')==0:
                    ouFile.write('\t'.join([gene]+fields[21:26]+['1'])+'\n')
                if fields[item].find('1/1')==0 and fields[item+8].find('0/0')==0:
                    ouFile.write('\t'.join([gene]+fields[21:26]+['2'])+'\n')
        ouFile.close()
        inFile.close()


multi_calling_split('sum_snv16s.exome_summary.overall.filter',range(-16,-8),['SNV.exome.somatic.ICC4','SNV.exome.somatic.ICC5','SNV.exome.somatic.ICC9','SNV.exome.somatic.ICC10','SNV.exome.somatic.CHC5','SNV.exome.somatic.CHC6','SNV.exome.somatic.CHC7','SNV.exome.somatic.CHC10'])

multi_calling_split('sum_snv16s.genome_summary.overall.filter',range(-16,-8),['SNV.genome.somatic.ICC4','SNV.genome.somatic.ICC5','SNV.genome.somatic.ICC9','SNV.genome.somatic.ICC10','SNV.genome.somatic.CHC5','SNV.genome.somatic.CHC6','SNV.genome.somatic.CHC7','SNV.genome.somatic.CHC10'])
