inFile=open('new_distribution.csv')
ouFile1=open('new_snp_distribution','w')
ouFile2=open('new_indel_distribution','w')
row=0
for line in inFile :
    row+=1
    line=line.strip()
    fields=line.split(',')
    if row<=16 :
        if fields[0]=='Substitutions' :
            ouFile1.write('Genomic'+'\t'+'\t'.join(fields[4:])+'\n')
        if fields[0]=='Coding' :
            ouFile1.write('Coding'+'\t'+'\t'.join(fields[4:])+'\n')
        if fields[0]=='Non-Coding' :
            ouFile1.write('Non-Coding'+'\t'+'\t'.join(fields[4:])+'\n')
        if fields[0]=='Intronic' :
            ouFile1.write('Intronic'+'\t'+'\t'.join(fields[4:])+'\n')
        if fields[0]=='Intergenic' :
            ouFile1.write('Intergenic'+'\t'+'\t'.join(fields[4:])+'\n')
    else :
        if fields[0]=='Small INDEL' :
            ouFile2.write('Genomic'+'\t'+'\t'.join(fields[4:])+'\n')
        if fields[0]=='Coding' :
            ouFile2.write('Coding'+'\t'+'\t'.join(fields[4:])+'\n')
        if fields[0]=='Non-Coding' :
            ouFile2.write('Non-Coding'+'\t'+'\t'.join(fields[4:])+'\n')
        if fields[0]=='Intronic' :
            ouFile2.write('Intronic'+'\t'+'\t'.join(fields[4:])+'\n')
        if fields[0]=='Intergenic' :
            ouFile2.write('Intergenic'+'\t'+'\t'.join(fields[4:])+'\n')



inFile.close()
ouFile1.close()
ouFile2.close()




inFile=open('dbsnp_distribution.csv')
ouFile1=open('dbsnp_snp_distribution','w')
ouFile2=open('dbsnp_indel_distribution','w')
row=0
for line in inFile :
    row+=1
    line=line.strip()
    fields=line.split(',')
    if row<=16 :
        if fields[0]=='Substitutions' :
            ouFile1.write('Genomic'+'\t'+'\t'.join(fields[4:])+'\n')
        if fields[0]=='Coding' :
            ouFile1.write('Coding'+'\t'+'\t'.join(fields[4:])+'\n')
        if fields[0]=='Non-Coding' :
            ouFile1.write('Non-Coding'+'\t'+'\t'.join(fields[4:])+'\n')
        if fields[0]=='Intronic' :
            ouFile1.write('Intronic'+'\t'+'\t'.join(fields[4:])+'\n')
        if fields[0]=='Intergenic' :
            ouFile1.write('Intergenic'+'\t'+'\t'.join(fields[4:])+'\n')
    else :
        if fields[0]=='Small INDEL' :
            ouFile2.write('Genomic'+'\t'+'\t'.join(fields[4:])+'\n')
        if fields[0]=='Coding' :
            ouFile2.write('Coding'+'\t'+'\t'.join(fields[4:])+'\n')
        if fields[0]=='Non-Coding' :
            ouFile2.write('Non-Coding'+'\t'+'\t'.join(fields[4:])+'\n')
        if fields[0]=='Intronic' :
            ouFile2.write('Intronic'+'\t'+'\t'.join(fields[4:])+'\n')
        if fields[0]=='Intergenic' :
            ouFile2.write('Intergenic'+'\t'+'\t'.join(fields[4:])+'\n')



inFile.close()
ouFile1.close()
ouFile2.close()



inFile=open('total_distribution.csv')
ouFile1=open('total_snp_distribution','w')
ouFile2=open('total_indel_distribution','w')
row=0
for line in inFile :
    row+=1
    line=line.strip()
    fields=line.split(',')
    if row<=16 :
        if fields[0]=='Substitutions' :
            ouFile1.write('Genomic'+'\t'+'\t'.join(fields[4:])+'\n')
        if fields[0]=='Coding' :
            ouFile1.write('Coding'+'\t'+'\t'.join(fields[4:])+'\n')
        if fields[0]=='Non-Coding' :
            ouFile1.write('Non-Coding'+'\t'+'\t'.join(fields[4:])+'\n')
        if fields[0]=='Intronic' :
            ouFile1.write('Intronic'+'\t'+'\t'.join(fields[4:])+'\n')
        if fields[0]=='Intergenic' :
            ouFile1.write('Intergenic'+'\t'+'\t'.join(fields[4:])+'\n')
    else :
        if fields[0]=='Small INDEL' :
            ouFile2.write('Genomic'+'\t'+'\t'.join(fields[4:])+'\n')
        if fields[0]=='Coding' :
            ouFile2.write('Coding'+'\t'+'\t'.join(fields[4:])+'\n')
        if fields[0]=='Non-Coding' :
            ouFile2.write('Non-Coding'+'\t'+'\t'.join(fields[4:])+'\n')
        if fields[0]=='Intronic' :
            ouFile2.write('Intronic'+'\t'+'\t'.join(fields[4:])+'\n')
        if fields[0]=='Intergenic' :
            ouFile2.write('Intergenic'+'\t'+'\t'.join(fields[4:])+'\n')


inFile.close()
ouFile1.close()
ouFile2.close()
