def snv_distribution_table(iFileList1,iFileList2,oFile) :
    dict1=dict()
    for i in range(len(iFileList1))  :
        sample=iFileList2[i]
        dict1[sample]=dict()
        inFile=open(iFileList1[i])
        for line in inFile :
            line=line.strip()
            fields=line.split('\t')
            key=fields[0]+'\t'+fields[1]
            val=int(fields[2])
            dict1[sample][key]=val
        inFile.close()


        dict1[sample]['StopGain']=dict1[sample].get('exonic;splicing\tstopgain SNV',0)+dict1[sample].get('exonic\tstopgain SNV',0)
        dict1[sample]['StopLoss']=dict1[sample].get('exonic;splicing\tstoploss SNV',0)+dict1[sample].get('exonic\tstoploss SNV',0)
        dict1[sample]['Nonsense']=dict1[sample]['StopGain']+dict1[sample]['StopLoss']

        dict1[sample]['Missense']=dict1[sample].get('exonic\tnonsynonymous SNV',0)+dict1[sample].get('exonic;splicing\tnonsynonymous SNV',0)
        dict1[sample]['Synonymous']=dict1[sample].get('exonic\tsynonymous SNV',0)+dict1[sample].get('exonic;splicing\tsynonymous SNV',0)
        dict1[sample]['UnKnown']=dict1[sample].get('exonic\tunknown',0)+dict1[sample].get('exonic;splicing\tunknown',0)

        dict1[sample]['Coding']=dict1[sample]['Nonsense']+dict1[sample]['Missense']+dict1[sample]['Synonymous']+dict1[sample]['UnKnown']

        dict1[sample]['UTR']=dict1[sample].get('UTR3\t',0)+dict1[sample].get('UTR5\t',0)+dict1[sample].get('UTR5;UTR3\t',0)
        dict1[sample]['ncRNA']=dict1[sample].get('ncRNA_exonic\t',0)+dict1[sample].get('ncRNA_intronic\t',0)+dict1[sample].get('ncRNA_UTR5\t',0)+dict1[sample].get('ncRNA_UTR3\t',0)+dict1[sample].get('ncRNA_UTR5;ncRNA_UTR3\t',0)+dict1[sample].get('ncRNA_splicing\t',0)

        dict1[sample]['NonCoding']=dict1[sample]['UTR']+dict1[sample]['ncRNA']


        dict1[sample]['Splicing']=dict1[sample].get('splicing\t',0)
        dict1[sample]['Other']=dict1[sample].get('intronic\t',0)
        dict1[sample]['Intronic']=dict1[sample]['Splicing']+dict1[sample]['Other']

        dict1[sample]['Intergenic']=dict1[sample].get('intergenic\t',0)+dict1[sample].get('upstream\t',0)+dict1[sample].get('downstream\t',0)+dict1[sample].get('upstream;downstream\t',0)

        dict1[sample]['Genomic']=dict1[sample]['Coding']+dict1[sample]['NonCoding']+dict1[sample]['Intronic']+dict1[sample]['Intergenic']


        type=['Genomic','Coding','Nonsense','StopGain','StopLoss','Missense','Synonymous','UnKnown','NonCoding','UTR','ncRNA','Intronic','Splicing','Other','Intergenic']

    list1=[['']+type]
    for key in iFileList2 :
        L=[key]
        for k in type :
            L.append(str(dict1[key][k]))
        list1.append(L)
            #print(key+'\t'+k+'\t'+str(dict1[key][k]))

    ouFile=open(oFile,'w')
    for j in range(len(list1[0])) :
        for i in range(len(list1)) :
            ouFile.write(list1[i][j]+'\t')
        ouFile.write('\n')






snv_distribution_table(['SNV.genome.somatic.ICC4.dist','SNV.genome.somatic.ICC5.dist','SNV.genome.somatic.ICC9.dist','SNV.genome.somatic.ICC10.dist','SNV.genome.somatic.CHC5.dist','SNV.genome.somatic.CHC6.dist','SNV.genome.somatic.CHC7.dist','SNV.genome.somatic.CHC10.dist'],['ICC4','ICC5','ICC9','ICC10','CHC5','CHC6','CHC7','CHC10'],'SNV.genome.somatic.distribution')

