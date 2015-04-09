def sort_dict_by_chrom_postition(aDict,outputfile) :
    '''
    aDict format :key='NOC2L\tchr1\t888659\t888659\tT\tC',val=[1,2,3,4,5]
    '''
    dict1=dict()
    list1=list()
    ouFile=open(outputfile,'w')
    chr=['chr1','chr2','chr3','chr4','chr5','chr6','chr7','chr8','chr9','chr10','chr11','chr12','chr13','chr14','chr15','chr16','chr17','chr18','chr19','chr20','chr21','chr22','chrM']
    for key in aDict :
        fields=key.split('\t')
        dict1.setdefault(fields[1],[])
        dict1[fields[1]].append(key)
    for key in chr :
        if key in dict1 :
            val=dict1[key]
            val.sort(cmp=lambda x,y:cmp(int(x.split('\t')[2]),int(y.split('\t')[2])))
            list1+=val
    for key in dict1 :
        if key not in chr :
            val=dict1[key]
            val.sort(cmp=lambda x,y:cmp(int(x.split('\t')[2]),int(y.split('\t')[2])))
            list1+=val
    for item in list1 :
        ouFile.write(item+'\t'+'\t'.join([str(x) for x in aDict[item]])+'\n')

    ouFile.close()


def combine_single(iFileList,oFile) :
    dict1=dict()
    for n,file in enumerate(iFileList) :
        inFile=open(file)
        for line in inFile :
            line=line.strip()
            fields=line.split('\t')
            key='\t'.join(fields[0:-1])
            dict1.setdefault(key,[0]*len(iFileList))
            dict1[key][n]=fields[-1]
        inFile.close()

    sort_dict_by_chrom_postition(dict1,oFile)



combine_single(['INDEL.exome.somatic.ICC4.frameshift_nondbsnp','INDEL.exome.somatic.ICC5.frameshift_nondbsnp','INDEL.exome.somatic.ICC9.frameshift_nondbsnp','INDEL.exome.somatic.ICC10.frameshift_nondbsnp','INDEL.exome.somatic.CHC5.frameshift_nondbsnp','INDEL.exome.somatic.CHC6.frameshift_nondbsnp','INDEL.exome.somatic.CHC7.frameshift_nondbsnp','INDEL.exome.somatic.CHC10.frameshift_nondbsnp'],'INDEL.exome.somatic.frameshift_nondbsnp')
