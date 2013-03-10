D = {}
inFile = open('/netshare1/home1/people/hansun/Data/Ensembl/Homo_sapiens.GRCh37.70.pep.all.fa.fa')
while True:
    line1 = inFile.readline().strip()
    line2 = inFile.readline().strip()
    if line1:
        D[line1] = line2
    else:
        break
inFile.close()

def ref_alt(inF):
    inFile = open(inF)
    ouFile1 = open(inF+'.ref-alt','w')
    ouFile2 = open(inF+'.not-ref-alt','w')
    ouFile3 = open(inF+'.ref-alt2','w')
    while True:
        L = []
        for i in range(24):
            line = inFile.readline().strip()
            if line:
                L.append(line)
            else:
                break
        if L:
            flag = 0
            for i in range(0,len(L),2):
                for k in D:
                    if L[i+1] in D[k]:
                        flag += 1
                        if L[i].find('REF')!=-1:
                            ouFile1.write(L[i]+'\t'+k+'\n')
                            ouFile1.write(L[i+1]+'\n')
                            ouFile1.write(L[i+2]+'\t'+k+'\n')
                            ouFile1.write(L[i+3]+'\n')
                        else:
                            ouFile3.write(L[i]+'\t'+k+'\n')
                            ouFile3.write(L[i+1]+'\n')
            if not flag:
                for item in L:
                    ouFile2.write(item+'\n')

        else:
            break

    inFile.close()
    ouFile1.close()
    ouFile2.close()
    ouFile3.close()

ref_alt('sum_snv.exome_summary.indel.overall.filter.pep')


