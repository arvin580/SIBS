import sys
import re
import subprocess


hits = 2
chrs = ['chr1','chr2','chr3','chr4','chr5','chr6','chr7','chr8','chr9','chr10',
        'chr11','chr12','chr13','chr14','chr15','chr16','chr17',
        'chr18','chr19','chr20','chr21','chr22','chrX','chrY','chrM']
 
def seq(inF):
    sv = {}
    inFile = open(inF)
    while True:
        head = inFile.readline().strip('>\n')
        seq = inFile.readline().strip()
        if head:
            sv[head]=seq
        else:
            break
    inFile.close()
    return sv

def grep(s,ouFile):
    rs=re.search(r'>(.*)<',s)
    if rs:
        subprocess.Popen(['grep',rs.group(1),sys.argv[1]], stdout=ouFile)

def unique(item):
    flag = [0, 0]
    for x in item[1][1:]:
        if (int(x[6]) + int(x[7]))/2 <=35:
            flag[0]+=1
        else:
            flag[1]+=1
    return flag
        
   

def count(inF):
    D = dict()
    inFile = open(inF)
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        #if float(fields[2]) > 90 and float(fields[3]) > 30:
        #if (float(fields[2]) > 95 and float(fields[3]) > 30) or (float(fields[2]) > 85  and float(fields[3]) > 60):
        if (float(fields[2]) > 90 and float(fields[3]) > 30):
            D.setdefault(fields[0],[0])
            D[fields[0]][0]+=1
            D[fields[0]].append(fields)
    inFile.close()

    d = D.items()
    d.sort(cmp=lambda x,y:cmp(x[1][0],y[1][0]))

    sv = seq(sys.argv[1].split('.blated')[0])
    ouFile1 = open(sys.argv[1]+'.filtered.head1','w')
    ouFile2 = open(sys.argv[1]+'.filtered.head2','w')
    ouFile3 = open(sys.argv[1]+'.filtered.seq1','w')
    ouFile4 = open(sys.argv[1]+'.filtered.seq2','w')
    ##ouFile5 = open(sys.argv[1]+'.filtered.grep','w')
    for item in d:
        t = []
        for x in item[1][1:]:
            t.append('\t'.join(x))


        if item[1][0] == hits  and max([int(x[3]) for x in item[1][1:]])<60:
            #flag = [0,0]
            flag = unique(item)
            if flag[0]<=1 and flag[1]<=1:
                t = []
                for x in item[1][1:]:
                    t.append('\t'.join(x))

                ouFile3.write('>'+item[0]+'\t'+str(item[1][0])+'\t'+'\t'.join(t)+'\n')
                ouFile3.write(sv[item[0]]+'\n')
                ouFile1.write(item[0]+'\t'+str(item[1][0])+'\n')
                ##ouFile3.write(item[0]+'\n')
                ##grep(item[0],ouFile5)
        
        ouFile2.write(item[0]+'\t'+str(item[1][0])+'\n')
        ##for x in sv[item[0]]:
        ##    ouFile4.write(x+'\n')
        ##ouFile4.write(item[0]+'\n')
        ouFile4.write('>'+item[0]+'\t'+str(item[1][0])+'\t'+'\t'.join(t)+'\n')
        ouFile4.write(sv[item[0]]+'\n')
         
    ouFile1.close()
    ouFile2.close()
    ouFile3.close()
    ##ouFile4.close()
    ##ouFile5.close()
        
count(sys.argv[1])
    
    
