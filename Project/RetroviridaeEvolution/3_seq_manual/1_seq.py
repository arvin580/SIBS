import sys
inFile=open('RetroviridaeGenome.fasta.fa')

dict1={}
for line in inFile :
    line=line.strip()
    if line.find('>')==0 :
        title=line
        title=title.strip('>')
        title=title.split('.')[0]
        dict1[title]=[]
    else :   
        dict1[title].append(line)
inFile.close()

nc=sys.argv[1]
start=int(sys.argv[2])
end=int(sys.argv[3])
seq=dict1[nc][0]

ouFile=open(nc+'_'+str(start)+'_'+str(end)+'.fasta','w')
ouFile.write('>'+nc+'_'+str(start)+'_'+str(end)+'\n')
ouFile.write(seq[start-1:end]+'\n')
ouFile.close()




