file1=['INDEL.genome.ICC4A','INDEL.genome.ICC4B','INDEL.genome.somatic.ICC4']
file2=['INDEL.genome.ICC5A','INDEL.genome.ICC5B','INDEL.genome.somatic.ICC5']
file3=['INDEL.genome.ICC9A','INDEL.genome.ICC9B','INDEL.genome.somatic.ICC9']
file4=['INDEL.genome.ICC10A','INDEL.genome.ICC10B','INDEL.genome.somatic.ICC10']
file5=['INDEL.genome.CHC5A','INDEL.genome.CHC5B','INDEL.genome.somatic.CHC5']
file6=['INDEL.genome.CHC6A','INDEL.genome.CHC6B','INDEL.genome.somatic.CHC6']
file7=['INDEL.genome.CHC7A','INDEL.genome.CHC7B','INDEL.genome.somatic.CHC7']
file8=['INDEL.genome.CHC10A','INDEL.genome.CHC10B','INDEL.genome.somatic.CHC10']

file=[file1,file2,file3,file4,file5,file6,file7,file8]
ouFile=open('genome_INDEL_number','w')

for i in file :
    ouFile.write(i[2].split('.')[-1]+'\t')
    for j in i :
        print(j)
        inFile=open(j)
        d=inFile.readlines()
        ouFile.write(str(len(d))+'\t')
        inFile.close()
    ouFile.write('\n')
ouFile.close()




file1=['INDEL.exome.ICC4A','INDEL.exome.ICC4B','INDEL.exome.somatic.ICC4']
file2=['INDEL.exome.ICC5A','INDEL.exome.ICC5B','INDEL.exome.somatic.ICC5']
file3=['INDEL.exome.ICC9A','INDEL.exome.ICC9B','INDEL.exome.somatic.ICC9']
file4=['INDEL.exome.ICC10A','INDEL.exome.ICC10B','INDEL.exome.somatic.ICC10']
file5=['INDEL.exome.CHC5A','INDEL.exome.CHC5B','INDEL.exome.somatic.CHC5']
file6=['INDEL.exome.CHC6A','INDEL.exome.CHC6B','INDEL.exome.somatic.CHC6']
file7=['INDEL.exome.CHC7A','INDEL.exome.CHC7B','INDEL.exome.somatic.CHC7']
file8=['INDEL.exome.CHC10A','INDEL.exome.CHC10B','INDEL.exome.somatic.CHC10']

file=[file1,file2,file3,file4,file5,file6,file7,file8]
ouFile=open('exome_INDEL_number','w')

for i in file :
    ouFile.write(i[2].split('.')[-1]+'\t')
    for j in i :
        print(j)
        inFile=open(j)
        d=inFile.readlines()
        ouFile.write(str(len(d))+'\t')
        inFile.close()
    ouFile.write('\n')
ouFile.close()
