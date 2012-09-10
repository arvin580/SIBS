import os

def spec(pep,Dir) :
    files=os.listdir(Dir)
    specs=[]
    for ff in files :
        inFile=open(Dir+os.sep+ff)

        for line in inFile :
            line=line.strip()
            fields=line.split('\t')
            if len(fields) >5 :
                if fields[9]==pep :
                    tp=fields[0].split('_')
                    specs.append(tp[1]+'_'+tp[2])
        inFile.close()
    return specs
    
def spec2(pep,Dir) :
    files=os.listdir(Dir)
    specs=[]
    for ff in files :
        inFile=open(Dir+os.sep+ff)
        for line in inFile :
            line=line.strip()
            fields=line.split('\t')
            if len(fields) >5 :
                if fields[2]==pep :
                    tp=fields[1].split('/')
                    specs.append(tp[0]+'_'+tp[1])
        inFile.close()
    return specs
    




def pepSpec(inF) :
    inFile=open(inF)
    ouFile=open(inF+'.spec','w')
    for line in inFile :
        line=line.strip()
        fields=line.split('\t')
        pep=fields[0]
        ouFile.write(line+'\t')

        specs=spec(pep,'/netshare1/home1/people/hansun/GeneFusionsFinal/11_AftTandem/FDR')
        for item in specs :
            ouFile.write(item+'\t')

        specs=spec2(pep,'/netshare1/home1/people/hansun/GeneFusionsFinal/13_AftOmssa/FDR')
        for item in specs :
            ouFile.write(item+'\t')

        ouFile.write('\n')

    inFile.close()
    ouFile.close()

pepSpec('Tandem.Omssa.FDR.pep.genefusions.final.pos.3.3')
