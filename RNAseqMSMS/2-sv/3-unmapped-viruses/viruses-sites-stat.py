def virus(inF, v, pos):
    inFile = open(inF)
    ouFile = open(inF + '.stat', 'w')
    before = 0
    after = 0
    while True:
        line1 = inFile.readline().strip()
        line2 = inFile.readline().strip()
        if line1:
            fields = line1.split('\t')
            if fields[1] == v:
                if int(fields[8]) < pos and int(fields[9]) < pos:
                    before += 1
                else:
                    after += 1
        else:
            break
    inFile.close()
    print(before)
    print(after)

virus('unmapped-blated-viruses-90-60.seq', 'NC_001357.1', 3000)
