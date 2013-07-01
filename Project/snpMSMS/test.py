inFile = open('CosmicCodingMuts_v64_02042013_noLimit-snp.pep.not-ref-alt')
row = 0
while True:
    line1 = inFile.readline()
    line2 = inFile.readline()
    row+=2
    if line1:
        if line1[0]!='>':
            print(row)
    else:
        break
inFile.close()
