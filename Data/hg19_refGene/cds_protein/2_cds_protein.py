import sys
inFile=open(sys.argv[1]+'.out1')
ouFile=open(sys.argv[1]+'.out2','w')
ouFile1=open(sys.argv[1]+'.out3','w')
ouFile2=open(sys.argv[1]+'.out4','w')
exons=[]
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    exonStart=int(fields[8])
    exonEnd=int(fields[9])
    cdsStart=int(fields[5])
    cdsEnd=int(fields[6])
    strand=fields[2]
    seq=fields[11]

    if strand=='-' :
        if cdsStart<=exonStart<=cdsEnd and exonEnd>cdsEnd :
            exon_len=cdsEnd-exonStart
            exon=seq[-exon_len:] 
            #ouFile.write(exon+'\n')
            exons.append([exon,exonStart,cdsEnd])
        if cdsStart<=exonStart<=cdsEnd and cdsStart<=exonEnd<=cdsEnd :
            exon=seq
            #ouFile.write(exon+'\n')
            exons.append([exon,exonStart,exonEnd])
        
        if cdsStart<=exonEnd<=cdsEnd and exonStart<=cdsStart :
            exon_len=exonEnd-cdsStart
            exon=seq[0:exon_len]
            #ouFile.write(exon+'\n')
            exons.append([exon,cdsStart,exonEnd])
        if exonEnd>=cdsEnd and exonStart<=cdsStart :
            exon=seq[exonEnd-cdsEnd:exonEnd-cdsStart]
            #ouFile.write(exon+'\n')
            exons.append([exon,cdsStart,cdsEnd])
    if strand=='+' :
        pass
            


for item in exons :
    ouFile1.write(item[0]+'\t'+str(item[1])+'\t'+str(item[2])+'\n')
    ouFile.write(item[0])



inFile.close()
ouFile.close()
ouFile1.close()

inFile3=open('mutation.file2')
ouFile3=open('mutation.file2.out','w')
for line in inFile3 :
    line=line.rstrip()
    fields=line.split('\t')
    point=int(fields[22])
    strand=sys.argv[2]

    protein=[]
    lh=0
    if strand=='-' :
        for item in exons :
            if point<item[1] :
                protein.append(item)
            if item[1]<=point<=item[2] :
                part_len=item[2]-point
                part=item[0][0:part_len]
                protein.append([part,point,item[2]])
                break

    for item in protein :
        ouFile2.write(item[0]+'\t'+str(item[1])+'\t'+str(item[2])+'\n')
        lh+=len(item[0])

    ouFile3.write(str(lh/3)+'\t'+line+'\n')

inFile3.close()
ouFile3.close()
ouFile2.close()




