import re

Q = 20
D = 30

def multi_calling_split(iFile,samplePosList,sampleNameList) :
    for i,item in enumerate(samplePosList) :
        inFile=open(iFile)
        ouFile=open(sampleNameList[i],'w')
        for line in inFile :
            line=line.rstrip()
            fields=line.split('\t')
            if int(fields[item].split(':')[-1])>=Q and int(fields[item].split(':')[-2])>=D:
                gene=fields[1]
                gene=re.split(r'[,;(]',gene)[0]
                if fields[item].find('0/1')==0:
                    ouFile.write('\t'.join([gene]+fields[21:26]+['1'])+'\n')
                if fields[item].find('1/1')==0:
                    ouFile.write('\t'.join([gene]+fields[21:26]+['2'])+'\n')
        ouFile.close()
        inFile.close()


multi_calling_split('sum_snv16sExome.exome_summary.overall.filter',range(-16,0),['SNV.exome.ICC4A','SNV.exome.ICC5A','SNV.exome.ICC9A','SNV.exome.ICC10A','SNV.exome.CHC5A','SNV.exome.CHC6A','SNV.exome.CHC7A','SNV.exome.CHC10A','SNV.exome.ICC4B','SNV.exome.ICC5B','SNV.exome.ICC9B','SNV.exome.ICC10B','SNV.exome.CHC5B','SNV.exome.CHC6B','SNV.exome.CHC7B','SNV.exome.CHC10B'])

multi_calling_split('sum_snv16sExome.genome_summary.overall.filter',range(-16,0),['SNV.genome.ICC4A','SNV.genome.ICC5A','SNV.genome.ICC9A','SNV.genome.ICC10A','SNV.genome.CHC5A','SNV.genome.CHC6A','SNV.genome.CHC7A','SNV.genome.CHC10A','SNV.genome.ICC4B','SNV.genome.ICC5B','SNV.genome.ICC9B','SNV.genome.ICC10B','SNV.genome.CHC5B','SNV.genome.CHC6B','SNV.genome.CHC7B','SNV.genome.CHC10B'])
