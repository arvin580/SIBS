def scatter_max(inFlist) :
    SNV=list()
    for item in inFlist :
        inFile=open(item)
        for line in inFile :
            line=line.strip()
            fields=line.split('\t')
            SNV.append(float(fields[-1]))
        inFile.close()
        return max(SNV)

def scatter_format(inFlist) :
    m=scatter_max(inFlist)
    print(m)
    m=100
    for item in inFlist :
        #m=not.repeat.scatter_max([item])
        inFile=open(item)
        ouFile=open(item+'tter','w')
        for line in inFile :
            line=line.strip()
            fields=line.split('\t')
            ouFile.write(' '.join(fields[0:-1])+' '+str(float(fields[-1])/m)+'\n')
        inFile.close()
        ouFile.close()


s=scatter_format(['SNV.genome.ICC4A.not.repeat.sca','SNV.genome.ICC4B.not.repeat.sca','SNV.genome.somatic.ICC4.not.repeat.sca'])
s=scatter_format(['SNV.genome.ICC5A.not.repeat.sca','SNV.genome.ICC5B.not.repeat.sca','SNV.genome.somatic.ICC5.not.repeat.sca'])
s=scatter_format(['SNV.genome.ICC9A.not.repeat.sca','SNV.genome.ICC9B.not.repeat.sca','SNV.genome.somatic.ICC9.not.repeat.sca'])
s=scatter_format(['SNV.genome.ICC10A.not.repeat.sca','SNV.genome.ICC10B.not.repeat.sca','SNV.genome.somatic.ICC10.not.repeat.sca'])
s=scatter_format(['SNV.genome.CHC5A.not.repeat.sca','SNV.genome.CHC5B.not.repeat.sca','SNV.genome.somatic.CHC5.not.repeat.sca'])
s=scatter_format(['SNV.genome.CHC6A.not.repeat.sca','SNV.genome.CHC6B.not.repeat.sca','SNV.genome.somatic.CHC6.not.repeat.sca'])
s=scatter_format(['SNV.genome.CHC7A.not.repeat.sca','SNV.genome.CHC7B.not.repeat.sca','SNV.genome.somatic.CHC7.not.repeat.sca'])
s=scatter_format(['SNV.genome.CHC10A.not.repeat.sca','SNV.genome.CHC10B.not.repeat.sca','SNV.genome.somatic.CHC10.not.repeat.sca'])


