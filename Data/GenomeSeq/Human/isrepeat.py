import sys
inFile=open('ucsc.hg19.fasta.fa')
fa=inFile.readlines()
inFile.close()

for i,item in enumerate(fa) :
    cur=0
    num=0
    while item.find('sys.argv[1]')!=-1 :
        num+=1
        if num==1:
            cur=cur+item.find(sys.argv[1])
        else :
            cur=cur+item.find(sys.argv[1])+1
        item=item[item.find(sys.argv[1])+1:]
        print(str(cur))


