def get_chr(chrom) :
    head=0
    inFile=open('/netshare1/home1/people/hansun/Data/GenomeSeq/Human/ucsc.hg19.fasta.fa')
    for line in inFile :
        line=line.strip()
        if head :
            return line
        if line.find(chrom)!=-1 :
            head=1
    inFile.close()


import sys
inFile=open(sys.argv[1])
ouFile=open(sys.argv[1]+'.out1','w')

import string
trans=string.maketrans('ATCGatcg','TAGCtagc')

for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    name=fields[1]
    chrom=fields[2]
    strand=fields[3]
    txStart=fields[4]
    txEnd=fields[5]
    cdsStart=fields[6]
    cdsEnd=fields[7]
    exonCount=fields[8]
    exonStarts=fields[9].split(',')[0:-1]
    exonEnds=fields[10].split(',')[0:-1]
    name2=fields[12]
    exonFrames=fields[15].split(',')[0:-1]

    seq=get_chr(chrom)

    if strand=='+' :
        for i in range(int(exonCount)) :
            seq_pos=seq[int(exonStarts[i]):int(exonEnds[i])]
            ouFile.write('\t'.join(fields[1:9]+fields[12:13])+'\t'+exonStarts[i]+'\t'+exonEnds[i]+'\t'+exonFrames[i]+'\t'+seq_pos+'\n')
    else :
        for i in range(int(exonCount)-1,-1,-1) :
            seq_pos=seq[int(exonStarts[i]):int(exonEnds[i])]
            seq_rev=seq_pos[::-1].translate(trans)
            ouFile.write('\t'.join(fields[1:8]+fields[12:13])+'\t'+exonStarts[i]+'\t'+exonEnds[i]+'\t'+exonFrames[i]+'\t'+seq_rev+'\n')


inFile.close()
ouFile.close()
