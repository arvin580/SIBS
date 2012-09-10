def protein_human(dict1) :
    inFile=open('protein_HUMAN')
    for line in inFile :
        line=line.strip()
        fields=line.split('\t')
        dict1.setdefault(fields[21],[])
        dict1[fields[21]].append(line)
    inFile.close()
    #print(len(dict1))
    #for key in dict1 :
    #    if len(dict1[key])!=1 :
            #print(dict1[key][0])
   #         print(key+'\t'+str(len(dict1[key])))


def  dna_protein() :
    dict1=dict()
    protein_human(dict1)

    #inFile=open('dna_protein_out1')
    inFile=open('dna_protein_out1')
    ouFile=open('dna_protein_out1.anno','w')
    for line in inFile :
        line=line.strip()
        fields=line.split('\t')
        if len(fields)==6 :
            ouFile.write(line+'\t'+'\t'.join(dict1.get(fields[-1],[]))+'\n')
        else :
            ouFile.write(line+'\n')

    inFile.close()
    ouFile.close()




dna_protein()
