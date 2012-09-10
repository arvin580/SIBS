def groupid() :
    inFile=open('Tandem.groupid.specid')
    D=dict()
    for line in inFile :
        line=line.strip()
        fields=line.split('\t')
        groupid=fields[0]
        spec=fields[1]
        k=spec.split('.')[0]+'.'+groupid
        D[k]=spec
    inFile.close()
    return D
'''
gi=groupid()
for k in gi :
    print(k)

'''
import os
import re

def keyname(name) :
    fields=re.split(r'[_.]',name)
    k=fields[1]+'/'+fields[2]+'/'+fields[3]+'_'+fields[4]+'_'+fields[5]+'_'+fields[6]+'_'+fields[7]+'.'+fields[-1]
    return k



def pepid(pep,D,tandem) :
    DIR='/netshare1/home1/people/hansun/GeneFusionsFinal/11_AftTandem/FDR'
    tandem.setdefault(pep,[])
    files=os.listdir(DIR)
    for f in files :
        inFile=open(DIR+os.sep+f)
        for line in inFile :
            line=line.strip()
            fields=line.split('\t')
            if len(fields)>3 and line.find(pep)!=-1 :
                k=keyname(fields[0])
                #print(k)
                if k in D :
                    tandem[pep].append(D[k])
                
        inFile.close()

def pepid2(pep,D,omssa) :
    DIR='/netshare1/home1/people/hansun/GeneFusionsFinal/13_AftOmssa/FDR'
    omssa.setdefault(pep,[])
    files=os.listdir(DIR)
    for f in files :
        inFile=open(DIR+os.sep+f)
        for line in inFile :
            line=line.strip()
            fields=line.split('\t')
            if len(fields)>3 and line.find(pep)!=-1 :
                omssa[pep].append(fields[1])
        inFile.close()


def deal(P,ouFile,tandem,omssa) :
    for k in P :
        ouFile.write(k+'\t')
        for v in tandem[k] :
            ouFile.write(v+'\t')
        ouFile.write('\n')
        ouFile.write(k+'\t')
        for v in omssa[k] :
            ouFile.write(v+'\t')
        ouFile.write('\n')

def deal2(P,ouFile,tandem,omssa) :
    for k in P :
        set1=set(tandem[k])
        set2=set(omssa[k])
        s=set1 & set2

        if len(s) >0 :
            ouFile.write(k+'\t')
            for x in s :
                ouFile.write(x+'\t')
            ouFile.write('\n')

        








def main() :
    tandem=dict()
    omssa=dict()
    inFile=open('Tandem.Omssa.FDR.pep.genefusions.final.pos.3.3')
    D=groupid()
    P=list()
    for line in inFile :
        line=line.strip()
        fields=line.split('\t')
        P.append(fields[0])
        pepid(fields[0],D,tandem)
        pepid2(fields[0],D,omssa)
    inFile.close()

    ouFile=open('Tandem.Omssa.FDR.pep.genefusions.final.pos.3.3.spec12','w')

    deal(P,ouFile,tandem,omssa)
    ouFile.write('\n\n')
    deal2(P,ouFile,tandem,omssa)
    ouFile.close()

main()


