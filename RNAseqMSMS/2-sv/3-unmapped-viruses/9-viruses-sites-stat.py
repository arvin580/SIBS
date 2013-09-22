def virus(inF, v):
    D = {}
    D['LCR'] = [0,1,104]
    D['E1'] = [0,914,2887]
    D['E2'] = [0,2817,3914]
    D['E4'] = [0,3418,3684]
    D['E5'] = [0,3936,4157]
    D['E6'] = [0,105,581]
    D['E7'] = [0,590,907]
    D['L1'] = [0,5430,7136]
    D['L2'] = [0,4244,5632]

    ouFile = open(inF + '.gene-stat', 'w')
    inFile = open(inF)
    while True:
        line1 = inFile.readline().strip()
        line2 = inFile.readline().strip()
        if line1:
            fields = line1.split('\t')
            if fields[1] == v:
                for g in D:
                    if D[g][1] <= int(fields[8]) <= D[g][2] or D[g][1] <= int(fields[9]) <= D[g][2]:
                        D[g][0] += 1
        else:
            break
    inFile.close()
    for g in D:
        ouFile.write(g+'\t'+str(D[g][0])+'\n')
    ouFile.close()
        
        

virus('unmapped-blated-viruses-90-60.seq', 'NC_001357.1' )
virus('unmapped-blated-viruses-100-76.seq', 'NC_001357.1')
