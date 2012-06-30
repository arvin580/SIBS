inFile=open('ucsc.hg19.fasta')
ouFile=open('ucsc.hg19.fasta.fa','w')
row=0
for line in inFile :
    row+=1
    line=line.strip()
    if line.find('>')==0 :
        if row==1 :
            ouFile.write(line+'\n')
        else :
            ouFile.write('\n')
            ouFile.write(line+'\n')
    else :
        ouFile.write(line)

inFile.close()
ouFile.close()
