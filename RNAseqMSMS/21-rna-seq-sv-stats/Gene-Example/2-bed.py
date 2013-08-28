def bed(inF,pos):
    D = {}
    D2 = {}
    D2['Deletion']='255,0,0'
    D2['Duplication']='0,255,0'
    D2['Inversion']='0,0,255'
    D2['Translocation']='255,255,0'
    inFile = open(inF)
    ouFile = open(inF+'.bed','w')
    head='''
browser position %s
browser hide all
track name="HeLa-SV" description="" visibility=2
'''%pos
    ouFile.write(head+'\n')

    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        tp = fields[2]
        D.setdefault(tp,0)
        D[tp] += 1
        ch = fields[4].split(':')[0]
        start = int(fields[4].split(':')[1])
        end = int(fields[4].split(':')[3])
        if start <= end:
            ft = [ch, str(start), str(end), tp+'-'+str(D[tp]), '0', '+', str(start), str(end), D2[tp] ]
        else:
            ft = [ch, str(end), str(start), tp+'-'+str(D[tp]), '0', '+', str(end), str(start), D2[tp] ]

        #################
        ouFile.write('\t'.join(ft)+'\n')
    inFile.close()
    ouFile.close()

bed('Gene-FLNA','chrX:153576900-153603006')
