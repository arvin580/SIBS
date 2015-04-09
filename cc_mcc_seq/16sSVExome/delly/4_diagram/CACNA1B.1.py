'''
mouse, using Diagram_class, key=gene
'''


from Diagram_class import *


inFile=open('CACNA1B.blasted')
dict1=dict()
for line in inFile :
    line=line.rstrip()
    fields=line.split('\t')
    key=fields[0]
    dict1.setdefault(key,0)
    dict1[key]+=1
inFile.close()


for key in dict1 :

    d=Diagram()
    inFile=open('CACNA1B.refGene.1')
    for line in inFile :
        line=line.rstrip()
        fields=line.split()
        #if fields[12]==key.split(':')[0]:
        d.Add_Anno(line)
        #    break
    inFile.close()

    d.Set_Blast_RowNum(dict1[key])

    inFile=open('CACNA1B.blasted')
    for line in inFile :
        line=line.rstrip()
        fields=line.split()
        if fields[0]==key :
            d.Add_Blast(line)
    inFile.close()

    d.Draw(key+'.1.pdf')
