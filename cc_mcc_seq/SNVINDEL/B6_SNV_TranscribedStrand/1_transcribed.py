import string
import sys
t=string.maketrans('ATCGatcg','TAGCtagc')
def read_hg19() :
    hg=[]
    inFile=open('hg19_refGene.txt')
    for line in inFile :
        line=line.strip()
        fields=line.split()
        txStart=int(fields[4])
        txEnd=int(fields[5])
        chrom=fields[2]
        strand=fields[3]
        hg.append([chrom,txStart+1,txEnd,strand])
    inFile.close()
    return hg

def transcription(inF) :
    hg=read_hg19()
    tran=dict()
    untran=dict()
    inFile=open(inF)
    ouFile=open(inF+'.trans','w')
    for line in inFile :
        line=line.strip()
        fields=line.split()
        chrom=fields[1]
        point=int(fields[2])
        ref=fields[4]
        alt=fields[5]
        k1=ref+alt
        k2=k1.translate(t)
        for item in hg :
            if chrom==item[0] and item[1]<=point<=item[2] and item[3]=='+':
                tran.setdefault(k1,0)
                untran.setdefault(k2,0)
                tran[k1]+=1
                untran[k2]+=1
            if chrom==item[0] and item[1]<=point<=item[2] and item[3]=='-':
                tran.setdefault(k2,0)
                untran.setdefault(k1,0)
                tran[k2]+=1
                untran[k1]+=1
    for key in tran :
        ouFile.write(key+'\t'+str(tran[key])+'\t'+str(untran[key])+'\n')

    inFile.close()
    ouFile.close()

transcription(sys.argv[1])




