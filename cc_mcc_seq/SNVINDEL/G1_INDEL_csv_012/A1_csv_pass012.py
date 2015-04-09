import csv
def quality_pass_012_csv(file,sampleNum) :
    inFile=open(file)
    ouFile=open(file.rstrip('csv')+'012','w')
    csvFile=csv.reader(inFile)
    head=csvFile.next()
    for fields in csvFile :
        #if fields[32]=='PASS' :
        for i in range(-sampleNum,0) :
            if fields[i].find('0/1')==0 or fields[i].find('1/0')==0 :
                fields[i]='1'
            elif fields[i].find('1/1')==0 :
                fields[i]='2'
            else :
                fields[i]='0'
        ouFile.write('\t'.join(fields)+'\n')

    inFile.close()
    ouFile.close()


quality_pass_012_csv('sum_indel.exome_summary.csv',10)
quality_pass_012_csv('sum_indel2.exome_summary.csv',10)
quality_pass_012_csv('sum_indel34.exome_summary.csv',8)

quality_pass_012_csv('sum_indel.genome_summary.csv',10)
quality_pass_012_csv('sum_indel2.genome_summary.csv',10)
quality_pass_012_csv('sum_indel34.genome_summary.csv',8)
