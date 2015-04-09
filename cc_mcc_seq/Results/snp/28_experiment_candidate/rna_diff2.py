def getChr(chr='chrX'):
    inFile=open('/netshare1/home1/people/hansun/Data/GenomeSeq/Human/ucsc.hg19.fasta.fa')
    flag=0
    while True :
        line=inFile.readline().strip()
        if flag==1 :
            return line
        if line.find(chr)==1 :
            flag=1
        if not line :
            break
    inFile.close()

def getSeq(chr,pos,ref,alt) :
    chrSeq=getChr(chr)
    left=chrSeq[pos-101:pos-1]
    point=chrSeq[pos-1:pos]
    right=chrSeq[pos:pos+100]
    print(left)
    print(point)
    print(right)

