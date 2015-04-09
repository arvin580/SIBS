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

def fn(gene) :
    inFile=open('/netshare1/home1/people/hansun/Data/GeneID/new/gene_info_9606')
    ff=''
    for line in inFile :
        line=line.strip()
        fields=line.split('\t')
        alias=fields[4].split('|')
        if fields[2] == gene  or gene in alias:
            ff=fields[8]
            break
    inFile.close()
    return ff
inFile=open('SNV.exome.somatic.nonsynonymous.qual')
ouFile=open('SNV.exome.somatic.nonsynonymous.qual_seq','w')
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    chrom=fields[3]
    pos1=int(fields[4])
    pos2=int(fields[5])
    ref=fields[6]
    alt=fields[7]
    seq=get_seq(chrom,pos1,pos2,ref,alt)
    ff=fn(fields[2])
    ouFile.write(line+'\t'+seq+'\t'+ff+'\n')

inFile.close()
ouFile.close()


inFile=open('SNV.exome.somatic.nonsynonymous_nondbsnp.qual')
ouFile=open('SNV.exome.somatic.nonsynonymous_nondbsnp.qual_seq','w')
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    chrom=fields[3]
    pos1=int(fields[4])
    pos2=int(fields[5])
    ref=fields[6]
    alt=fields[7]
    seq=get_seq(chrom,pos1,pos2,ref,alt)
    ff=fn(fields[2])
    ouFile.write(line+'\t'+seq+'\t'+ff+'\n')

inFile.close()
ouFile.close()



