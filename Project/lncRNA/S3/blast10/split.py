inFile1=open('lncrna_lncdb_human_genomic.fa','r')
lines=inFile1.readlines()
inFile1.close()
j=0
for i in range(0,len(lines),2):
    j+=1
    ouFile1=open('lncrna_lncdb_human_genomic.'+str(j),'w')
    ouFile1.write(lines[i])
    ouFile1.write(lines[i+1])
    ouFile1.close()


