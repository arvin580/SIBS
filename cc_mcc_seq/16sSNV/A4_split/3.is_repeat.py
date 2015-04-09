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

snv('SNV.exome.ICC4A')
snv('SNV.exome.ICC5A')
snv('SNV.exome.ICC9A')
snv('SNV.exome.ICC10A')
snv('SNV.exome.ICC4B')
snv('SNV.exome.ICC5B')
snv('SNV.exome.ICC9B')
snv('SNV.exome.ICC10B')
snv('SNV.exome.CHC5A')
snv('SNV.exome.CHC6A')
snv('SNV.exome.CHC7A')
snv('SNV.exome.CHC10A')
snv('SNV.exome.CHC5B')
snv('SNV.exome.CHC6B')
snv('SNV.exome.CHC7B')
snv('SNV.exome.CHC10B')
snv('SNV.exome.somatic.ICC4')
snv('SNV.exome.somatic.ICC5')
snv('SNV.exome.somatic.ICC9')
snv('SNV.exome.somatic.ICC10')
snv('SNV.exome.somatic.CHC5')
snv('SNV.exome.somatic.CHC6')
snv('SNV.exome.somatic.CHC7')
snv('SNV.exome.somatic.CHC10')

snv('SNV.genome.ICC4A')
snv('SNV.genome.ICC5A')
snv('SNV.genome.ICC9A')
snv('SNV.genome.ICC10A')
snv('SNV.genome.ICC4B')
snv('SNV.genome.ICC5B')
snv('SNV.genome.ICC9B')
snv('SNV.genome.ICC10B')
snv('SNV.genome.CHC5A')
snv('SNV.genome.CHC6A')
snv('SNV.genome.CHC7A')
snv('SNV.genome.CHC10A')
snv('SNV.genome.CHC5B')
snv('SNV.genome.CHC6B')
snv('SNV.genome.CHC7B')
snv('SNV.genome.CHC10B')
snv('SNV.genome.somatic.ICC4')
snv('SNV.genome.somatic.ICC5')
snv('SNV.genome.somatic.ICC9')
snv('SNV.genome.somatic.ICC10')
snv('SNV.genome.somatic.CHC5')
snv('SNV.genome.somatic.CHC6')
snv('SNV.genome.somatic.CHC7')
snv('SNV.genome.somatic.CHC10')

