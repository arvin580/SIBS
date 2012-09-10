###  python gbk.py human_ABL1 NC_001499_ABL1
import sys
inFile=open(sys.argv[1])
ouFile=open(sys.argv[1]+'_'+sys.argv[2]+'.gbk','w')
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    name=fields[1]
    chrom=fields[2]
    strand=fields[3]
    txStart=int(fields[4])
    txEnd=int(fields[5])
    cdsStart=int(fields[6])
    cdsEnd=int(fields[7])
    exonCount=int(fields[8])
    exonStarts=fields[9].split(',')[0:-1]
    exonEnds=fields[10].split(',')[0:-1]
    name2=fields[12]
    exonFrames=fields[15].split(',')[0:-1]
    
    #print('%s..%s'%(txStart,txEnd))
    #print('%s..%s'%(cdsStart,cdsEnd))
    ouFile.write('     cdsStart        %s..%s'%(cdsStart-txStart+1,cdsStart-txStart+1)+'\n')
    ouFile.write('                     /genome_pos="%s"'%(cdsStart)+'\n')
    ouFile.write('     cdsEnd          %s..%s'%(cdsEnd-txStart+1,cdsEnd-txStart+1)+'\n')
    ouFile.write('                     /genome_pos="%s"'%(cdsEnd)+'\n')
    for i in range(exonCount) :
        ouFile.write('     exon            %s..%s'%(int(exonStarts[i])-txStart+1,int(exonEnds[i])-txStart+1)+'\n')
        ouFile.write('                     /locus_tag="%s,%s"'%(int(exonStarts[i]),int(exonEnds[i]))+'\n')
    

inFile.close()

inFile=open(sys.argv[2])

for line in inFile :
    line=line.strip()
    #fields=line.split('\t')
    fields=line.split()
    subjectStart=fields[9]
    subjectEnd=fields[10]
    queryStart=fields[7]
    queryEnd=fields[8]
    ouFile.write('     blast           complement(%s..%s)'%(int(subjectStart)-txStart+1,int(subjectEnd)-txStart+1)+'\n')
    ouFile.write('                     /locus_tag="%s,%s"'%(int(subjectStart),int(subjectEnd))+'\n')
    ouFile.write('                     /genome_pos="%s,%s"'%(int(queryStart),int(queryEnd))+'\n')
    

inFile.close()




ouFile.write('ORIGIN\n')
for i in range(txEnd-txStart+1) :
    ouFile.write('N')












ouFile.close()
