def pass_truth(inF1,inF2) :
    D=dict()
    inFile=open(inF2)
    for line in inFile :
        line=line.strip()
        fields=line.split('\t')
        k='\t'.join(fields[21:26])
        D[k]=fields[32]
    inFile.close()

    p=0
    t=0
    inFile=open(inF1)
    for line in inFile :
        line=line.strip()
        fields=line.split('\t')
        k='\t'.join(fields[1:6])
        if D[k]=='PASS' :
            p+=1
        if D[k].find('Truth') ==0 :
            t+=1
    inFile.close()
    print(p)
    print(t)
pass_truth('SNV.genome.nopass.CHC6A','sum_snp2.genome_summary.012')
pass_truth('SNV.genome.nopass.CHC6B','sum_snp34.genome_summary.012')
