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
    m=4084.0
    for item in inFlist :
        #m=scatter_max([item])
        inFile=open(item)
        ouFile=open(item+'tter','w')
        for line in inFile :
            line=line.strip()
            fields=line.split('\t')
            ouFile.write(' '.join(fields[0:-1])+' '+str(float(fields[-1])/m)+'\n')
        inFile.close()
        ouFile.close()


s=scatter_format(['SNV.genome.ICC4A.sca','SNV.genome.ICC4B.sca','SNV.genome.somatic.ICC4.sca'])
s=scatter_format(['SNV.genome.ICC5A.sca','SNV.genome.ICC5B.sca','SNV.genome.somatic.ICC5.sca'])
s=scatter_format(['SNV.genome.ICC9A.sca','SNV.genome.ICC9B.sca','SNV.genome.somatic.ICC9.sca'])
s=scatter_format(['SNV.genome.ICC10A.sca','SNV.genome.ICC10B.sca','SNV.genome.somatic.ICC10.sca'])
s=scatter_format(['SNV.genome.CHC5A.sca','SNV.genome.CHC5B.sca','SNV.genome.somatic.CHC5.sca'])
s=scatter_format(['SNV.genome.CHC6A.sca','SNV.genome.CHC6B.sca','SNV.genome.somatic.CHC6.sca'])
s=scatter_format(['SNV.genome.CHC7A.sca','SNV.genome.CHC7B.sca','SNV.genome.somatic.CHC7.sca'])
s=scatter_format(['SNV.genome.CHC10A.sca','SNV.genome.CHC10B.sca','SNV.genome.somatic.CHC10.sca'])


