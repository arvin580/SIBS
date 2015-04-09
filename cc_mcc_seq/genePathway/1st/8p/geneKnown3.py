inFile1=open('/netshare1/home1/people/hansun/GATK/bundle/ucsc.hg19.fasta','r')
dict1={}
for line in inFile1 :
    line=line.strip()
    if line.find('>')==0 :
        title=line
        title=title.strip('>')
        dict1[title]=[]
    else :  
        dict1[title].append(line)
inFile1.close()

for key in dict1 : 
    dict1[key]=''.join(dict1[key])
 

def interval_seq(chr,pos,before,after,type,alt) :
    if type==0 :
        return(dict1[chr][pos-before-1:pos+after])
    if type==1 :
        s=dict1[chr][pos-before-1:pos-1]+alt+dict1[chr][pos:pos+after]
        return(s)

inFile2=open('geneKnown2','r')
ouFile1=open('geneKnown3','w')
ouFile1.write('GENE\tCHR\tPOS\tREF\tALT\t')
ouFile1.write('10A\t1A\t2A\t3A\t4A\t5A\t6A\t7A\t8A\t9A\t')
ouFile1.write('M10A\tM1A\tM2A\tM3A\tM4A\tM5A\tM6A\tM7A\tM8A\tM9A\t')
ouFile1.write('REFSEQ(+-500bp)\t')
ouFile1.write('ALTSEQ(+-500bp)\n')


for line in inFile2 :
    line=line.strip()
    fields=line.split()
    ouFile1.write(line+'\t'+interval_seq(fields[1],int(fields[2]),500,500,0,fields[4])+'\t'+interval_seq(fields[1],int(fields[2]),500,500,1,fields[4])+'\n')

ouFile1.close()
inFile2.close()
