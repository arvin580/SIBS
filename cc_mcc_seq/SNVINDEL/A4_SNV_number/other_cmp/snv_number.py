file=['SNV.genome.ICC10A10B',
'SNV.genome.ICC10A4B',
'SNV.genome.ICC10A5B',
'SNV.genome.ICC10A9B',
'SNV.genome.ICC4A10B',
'SNV.genome.ICC4A4B',
'SNV.genome.ICC4A5B',
'SNV.genome.ICC4A9B',
'SNV.genome.ICC5A10B',
'SNV.genome.ICC5A4B',
'SNV.genome.ICC5A5B',
'SNV.genome.ICC5A9B',
'SNV.genome.ICC9A10B',
'SNV.genome.ICC9A4B',
'SNV.genome.ICC9A5B',
'SNV.genome.ICC9A9B',
'SNV.genome.CHC10A10B',
'SNV.genome.CHC10A5B',
'SNV.genome.CHC10A6B',
'SNV.genome.CHC10A7B',
'SNV.genome.CHC5A10B',
'SNV.genome.CHC5A5B',
'SNV.genome.CHC5A6B',
'SNV.genome.CHC5A7B',
'SNV.genome.CHC6A10B',
'SNV.genome.CHC6A5B',
'SNV.genome.CHC6A6B',
'SNV.genome.CHC6A7B',
'SNV.genome.CHC7A10B',
'SNV.genome.CHC7A5B',
'SNV.genome.CHC7A6B',
'SNV.genome.CHC7A7B']

ouFile=open('SNV_number','w')
for j in file :
    inFile=open(j)
    d=inFile.readlines()
    ouFile.write(j+'\t'+str(len(d))+'\n')
    inFile.close()
ouFile.close()


