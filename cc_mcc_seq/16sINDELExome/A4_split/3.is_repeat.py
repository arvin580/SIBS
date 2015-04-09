import sys 
inFile = open('/netshare1/home1/people/hansun/GATK/bundle/ucsc.hg19.fasta')

dict1={}
for line in inFile :
    line=line.strip()
    if line.find('>')==0 :
        title=line.strip('>')
        dict1[title]=[]
    else :   
        dict1[title].append(line)
inFile.close()

for key in dict1 :
    dict1[key]=''.join(dict1[key])

def snv(inF):
    inFile = open(inF)
    ouFile1 = open(inF+'.is.repeat','w')
    ouFile2 = open(inF+'.not.repeat','w')
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        ch = fields[1]
        pos = int(fields[2])-1
        if dict1[ch][pos].islower():
            ouFile1.write(line+'\n')
        else:
            ouFile2.write(line+'\n')

    inFile.close()
    ouFile1.close()
    ouFile2.close()

snv('INDEL.exome.ICC4A')
snv('INDEL.exome.ICC5A')
snv('INDEL.exome.ICC9A')
snv('INDEL.exome.ICC10A')
snv('INDEL.exome.ICC4B')
snv('INDEL.exome.ICC5B')
snv('INDEL.exome.ICC9B')
snv('INDEL.exome.ICC10B')
snv('INDEL.exome.CHC5A')
snv('INDEL.exome.CHC6A')
snv('INDEL.exome.CHC7A')
snv('INDEL.exome.CHC10A')
snv('INDEL.exome.CHC5B')
snv('INDEL.exome.CHC6B')
snv('INDEL.exome.CHC7B')
snv('INDEL.exome.CHC10B')
snv('INDEL.exome.somatic.ICC4')
snv('INDEL.exome.somatic.ICC5')
snv('INDEL.exome.somatic.ICC9')
snv('INDEL.exome.somatic.ICC10')
snv('INDEL.exome.somatic.CHC5')
snv('INDEL.exome.somatic.CHC6')
snv('INDEL.exome.somatic.CHC7')
snv('INDEL.exome.somatic.CHC10')

snv('INDEL.genome.ICC4A')
snv('INDEL.genome.ICC5A')
snv('INDEL.genome.ICC9A')
snv('INDEL.genome.ICC10A')
snv('INDEL.genome.ICC4B')
snv('INDEL.genome.ICC5B')
snv('INDEL.genome.ICC9B')
snv('INDEL.genome.ICC10B')
snv('INDEL.genome.CHC5A')
snv('INDEL.genome.CHC6A')
snv('INDEL.genome.CHC7A')
snv('INDEL.genome.CHC10A')
snv('INDEL.genome.CHC5B')
snv('INDEL.genome.CHC6B')
snv('INDEL.genome.CHC7B')
snv('INDEL.genome.CHC10B')
snv('INDEL.genome.somatic.ICC4')
snv('INDEL.genome.somatic.ICC5')
snv('INDEL.genome.somatic.ICC9')
snv('INDEL.genome.somatic.ICC10')
snv('INDEL.genome.somatic.CHC5')
snv('INDEL.genome.somatic.CHC6')
snv('INDEL.genome.somatic.CHC7')
snv('INDEL.genome.somatic.CHC10')

