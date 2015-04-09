def get_seq(chrom,pos,ref,alt,inter=500) :
    inFile=open('/netshare1/home1/people/hansun/Data/GenomeSeq/Human/ucsc.hg19.fasta.fa')
    while True :
        head=inFile.readline()
        seq=inFile.readline()
        if head.find(chrom)!=-1 :
            seq=seq.strip()
            if ref==seq[pos-1] :
                s1=seq[pos-inter-1:pos-1]+ref+seq[pos:pos+inter]
                s2=seq[pos-inter-1:pos-1]+alt+seq[pos:pos+inter]
                return(s1+'\t'+s2)
            else :
                print('warning')
        if not head :
            break
    inFile.close()

##get_seq('chr3',10,'0','X',5)

inFile=open('repair_gene')
ouFile=open('repair_gene_seq','w')
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    chrom=fields[1]
    pos=int(fields[2])
    ref=fields[4]
    alt=fields[5]
    seq=get_seq(chrom,pos,ref,alt)
    ouFile.write(line+'\t'+seq+'\n')

inFile.close()
ouFile.close()



