import string
def seq(file):
    ouFile1=open(file.split('.')[0]+'.seq','w')
    inFile1=open(file)
    inFile1.readline()
    for line in inFile1 :
        fields=line.split()
        #inFile2=open('/netshare1/home1/people/hansun/Project/lncRNA/GenomeSeq/%s/ucsc.%s.fasta'%fields[0].capitalize(),%fields[0])
        if fields[0]=='human' :
            inFile2=open('/netshare1/home1/people/hansun/Project/lncRNA/GenomeSeq/%s/ucsc.hg19.fasta'%(fields[0].capitalize()))
        else :
            inFile2=open('/netshare1/home1/people/hansun/Project/lncRNA/GenomeSeq/%s/ucsc.%s.fasta'%(fields[0].capitalize(),fields[0]))
        dict1=dict()
    #    flag=0
    #    for line in inFile2 :
    #        line=line.strip()
    #        if flag==1 :
    #            dict1[key]=line
    #            break
    #        if line.find(fields[2])!=-1 :
    #            key=fields[2]
    #            flag=1
    #    inFile2.close()
    #
        for line in inFile2 :
            line=line.strip()
            if line.find('>')==0 :
                key=line[1:]
                dict1.setdefault(key,[])
            else :
                dict1[key].append(line)
        for key in dict1 :
            dict1[key]=''.join(dict1[key])
    
        if int(fields[3])<=int(fields[4]) :
            seq=dict1[fields[2]][int(fields[3])-1:int(fields[4])]
        else :
            seq=dict1[fields[2]][int(fields[3])-1:int(fields[4])-2:-1]
            mt=string.maketrans('ATCGNatcgn','TAGCNtagcn')
            seq=seq.translate(mt)
        ouFile1.write('>'+fields[1]+':'+fields[0]+':'+fields[2]+':'+fields[3]+':'+fields[4]+':'+fields[5]+'\n')
        ouFile1.write(seq+'\n')
    inFile1.close()


seq('Pldi_mouse.txt')
seq('Zfhx2as_mouse.txt')
