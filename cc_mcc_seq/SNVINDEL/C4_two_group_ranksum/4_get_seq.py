inFile=open('/netshare1/home1/people/hansun/Data/GenomeSeq/Human/ucsc.hg19.fasta.fa')
fa=dict()
while True :
   head=inFile.readline().strip()
   seq=inFile.readline().strip()
   fa[head]=seq
   if not head :
       break
inFile.close()

def get_seq(chrom,pos1,pos2,ref,alt,inter=500) :
        if pos1-inter-1<0 :
            inter=pos1-1
        seq=fa['>'+chrom]
        if ref==seq[pos1-1:pos2].upper() :
            #s1=seq[pos-inter-1:pos-1]+ref+seq[pos:pos+inter]
            #s2=seq[pos-inter-1:pos-1]+alt+seq[pos:pos+inter]
            s1=seq[pos1-inter-1:pos1-1]+seq[pos1-1:pos2]+seq[pos2:pos2+inter]
            s2=seq[pos1-inter-1:pos1-1]+alt+seq[pos2:pos2+inter]
            return(s1+'\t'+s2)
        else :
            print('warning:\t'+chrom+'\t'+str(pos1)+'\t'+str(pos2)+'\t'+ref+'\t'+alt)
            return None

inFile=open('SNV.exome.somatic.nonsynonymous.geneLevel.ranksum_test.mutation')
ouFile=open('SNV.exome.somatic.nonsynonymous.geneLevel.ranksum_test.mutation_seq','w')
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    chrom=fields[1]
    pos1=int(fields[2])
    pos2=int(fields[3])
    ref=fields[4]
    alt=fields[5]
    seq=get_seq(chrom,pos1,pos2,ref,alt)
    ouFile.write(line+'\t'+seq+'\n')

inFile.close()
ouFile.close()



