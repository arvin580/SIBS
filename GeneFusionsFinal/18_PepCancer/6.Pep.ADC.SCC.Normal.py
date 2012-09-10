P=['GDVEEDETIPDSPSVLETIR','GGSGYGDLGGPIITTQVTIPK']

def sym(pep) :
    inFile=open('Tandem.Omssa.FDR.pep.splicing.final.pos.3.3.curate.complete.curate')
    while True :
        line1=inFile.readline()
        line2=inFile.readline()
        line3=inFile.readline()
    
        if not line1 :
            break
        p=line1.strip('#\r\n')
        if p == pep :
            fields=line2.split(':')
            f=fields[1]
            return f

    inFile.close()


def deal(pep,D1) :
    inFile=open('Tandem.Omssa.FDR.pep.splicing.final.pos.3.3.spec')
    for line in inFile :
        line=line.strip()
        fields=line.split()
        n1=int(fields[1])
        n2=int(fields[2])
        if fields[0] == pep :
            for t in fields[-n2:] :
                tp=t.split('_')[0]
                D1[pep][tp]+=1

    inFile.close()




inFile=open('Tandem.Omssa.FDR.pep.splicing.final.pos.3.3.spec2')
ouFile=open('Tandem.Omssa.FDR.pep.splicing.final.pos.3.3.spec2.num.omssa','w')

D1=dict()
for line in inFile :
    line=line.strip()
    fields=line.split()
    pep=fields[0]
    D1.setdefault(pep,{})
    D1[pep].setdefault('ADC',0)
    D1[pep].setdefault('SCC',0)
    D1[pep].setdefault('Normal',0)
    deal(pep,D1)
inFile.close()

for pep in P :
    ouFile.write(pep+'\t'+sym(pep)+'\t')
    for tp in ['ADC','SCC','Normal'] :
        ouFile.write(str(D1[pep][tp])+'\t')
    ouFile.write('\n')

ouFile.close()
        
