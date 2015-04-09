def chr_filter(inF,chrom,start,end) :
    inFile=open(inF)
    ouFile=open(inF+'.%s_%s_%s'%(chrom,start,end),'w')
    for line in inFile :
        line=line.strip()
        fields=line.split('\t')
        if fields[1]==chrom :
            if start<= int(fields[2]) <=end :
                ouFile.write(line+'\n')

    inFile.close()
    ouFile.close()

chr_filter('SNV.genome.somatic.ICC4','chr6',57200000,57600000)
chr_filter('SNV.genome.somatic.ICC5','chr6',57200000,57600000)
chr_filter('SNV.genome.somatic.ICC9','chr6',57200000,57600000)
chr_filter('SNV.genome.somatic.ICC10','chr6',57200000,57600000)
chr_filter('SNV.genome.somatic.CHC5','chr6',57200000,57600000)
chr_filter('SNV.genome.somatic.CHC6','chr6',57200000,57600000)
chr_filter('SNV.genome.somatic.CHC7','chr6',57200000,57600000)
chr_filter('SNV.genome.somatic.CHC10','chr6',57200000,57600000)
