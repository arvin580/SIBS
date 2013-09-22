D = {}
D['LCR'] = 0
D['E1'] = 0
D['E2'] = 0
D['E3'] = 0
D['E4'] = 0
D['E5'] = 0
D['E6'] = 0
D['E7'] = 0
D['L1'] = 0
D['L2'] = 0
def virus(inF, v, POS):
    ouFile = open(inF + '.stat', 'w')
    for pos in POS:
        inFile = open(inF)
        before = 0
        after = 0
        while True:
            line1 = inFile.readline().strip()
            line2 = inFile.readline().strip()
            if line1:
                fields = line1.split('\t')
                if fields[1] == v:
                    if int(fields[8]) <= pos and int(fields[9]) <= pos:
                        before += 1
                    else:
                        after += 1
            else:
                break
        inFile.close()
        ouFile.write('before ' + str(pos) +'\t' +str(before)+'\t' )
        ouFile.write('after ' + str(pos) +'\t' +str(after)+'\n' )
    ouFile.close()
        
        

virus('unmapped-blated-viruses-90-60.seq', 'NC_001357.1', [1000,1500,2000,2500,3000,3500,4000,4500,5000,5500,6000,6500,7000,7500])
virus('unmapped-blated-viruses-100-76.seq', 'NC_001357.1', [1000,1500,2000,2500,3000,3500,4000,4500,5000,5500,6000,6500,7000,7500])
