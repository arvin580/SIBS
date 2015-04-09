inFile=open('sum_indel.exome_combined.sorted')
ouFile=open('sum_indel.exome_combined.sorted.pass012','w')

for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    if fields[32]=='PASS' or fields[46]=='PASS':
        ouFile.write('\t'.join(fields[0:31])+'\t')
        ouFile.write('\t'.join([str(i) for i in fields[31:35]])+'\t')
        ouFile.write('\t'.join([str(i) for i in fields[45:49]])+'\t')

        fi=[]
        for item in fields[35:45] :
            if item.find('0/1')==0 or item.find('1/0')==0 :
                fi.append('1')
            elif item.find('1/1')==0 :
                fi.append('2')
            else :
                fi.append('0')
        
        ouFile.write('\t'.join(fi)+'\t')

        fi=[]
        for item in fields[49:] :
            if item.find('0/1')==0  or item.find('1/0')==0 :
                fi.append('1')
            elif item.find('1/1')==0 :
                fi.append('2')
            else :
                fi.append('0')
        
        ouFile.write('\t'.join(fi)+'\n')



inFile.close()


inFile=open('sum_indel.genome_combined.sorted')
ouFile=open('sum_indel.genome_combined.sorted.pass012','w')

for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    if fields[32]=='PASS' or fields[46]=='PASS':
        ouFile.write('\t'.join(fields[0:31])+'\t')
        ouFile.write('\t'.join([str(i) for i in fields[31:35]])+'\t')
        ouFile.write('\t'.join([str(i) for i in fields[45:49]])+'\t')

        fi=[]
        for item in fields[35:45] :
            if item.find('0/1')==0  or item.find('1/0')==0 :
                fi.append('1')
            elif item.find('1/1')==0 :
                fi.append('2')
            else :
                fi.append('0')
        
        ouFile.write('\t'.join(fi)+'\t')

        fi=[]
        for item in fields[49:] :
            if item.find('0/1')==0 or item.find('1/0')==0 :
                fi.append('1')
            elif item.find('1/1')==0 :
                fi.append('2')
            else :
                fi.append('0')
        
        ouFile.write('\t'.join(fi)+'\n')

inFile.close()
