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


multi_calling_split('sum_snv16sExome.exome_summary.indel.overall.filter',range(-16,0),['INDEL.exome.ICC4A','INDEL.exome.ICC5A','INDEL.exome.ICC9A','INDEL.exome.ICC10A','INDEL.exome.CHC5A','INDEL.exome.CHC6A','INDEL.exome.CHC7A','INDEL.exome.CHC10A','INDEL.exome.ICC4B','INDEL.exome.ICC5B','INDEL.exome.ICC9B','INDEL.exome.ICC10B','INDEL.exome.CHC5B','INDEL.exome.CHC6B','INDEL.exome.CHC7B','INDEL.exome.CHC10B'])

multi_calling_split('sum_snv16sExome.genome_summary.indel.overall.filter',range(-16,0),['INDEL.genome.ICC4A','INDEL.genome.ICC5A','INDEL.genome.ICC9A','INDEL.genome.ICC10A','INDEL.genome.CHC5A','INDEL.genome.CHC6A','INDEL.genome.CHC7A','INDEL.genome.CHC10A','INDEL.genome.ICC4B','INDEL.genome.ICC5B','INDEL.genome.ICC9B','INDEL.genome.ICC10B','INDEL.genome.CHC5B','INDEL.genome.CHC6B','INDEL.genome.CHC7B','INDEL.genome.CHC10B'])
