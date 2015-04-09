import sys
inFile = open('/netshare1/home1/people/hansun/GATK/bundle/ucsc.hg19.fasta')

dict1={}
for line in inFile :
    line=line.strip()
    if line.find('>')==0 :
        title=line
        title=title.strip('>')
        dict1[title]=[]
    else :   
        dict1[title].append(line)
inFile.close()

for key in dict1 :
    dict1[key]=''.join(dict1[key])
    subject = dict1[key]
    inx = subject.find(sys.argv[1])
    while inx != -1:
        print(inx)
        inx = subject[inx+1:].find(sys.argv[1])




