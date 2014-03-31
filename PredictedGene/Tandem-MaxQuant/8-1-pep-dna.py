import string
trans = string.maketrans('ATCGatcg','TAGCtagc')

inFile = open('HeLa-Peptide-Validation-non_blast2.fa')
while True:
    line1 = inFile.readline().strip()
    line2 = inFile.readline().strip()
    line3 = inFile.readline().strip()
    line4 = inFile.readline().strip()
    line5 = inFile.readline().strip()
    line6 = inFile.readline().strip()
    line7 = inFile.readline().strip()
    line8 = inFile.readline().strip()
    line9 = inFile.readline().strip()
    if line1:
        pep = line2
        dna = line3
        if pep in line4:
            start_pep = line4.find(pep)
            start_dna = start_pep*3
            end_dna = start_dna + len(pep)*3
            seq_dna = dna[start_dna:end_dna]
            print('+0')
            print(pep)
            print(seq_dna)
        elif pep in line5:
            start_pep = line5.find(pep)
            start_dna = start_pep*3+1
            end_dna = start_dna + len(pep)*3
            seq_dna = dna[start_dna:end_dna]
            print('+1')
            print(pep)
            print(seq_dna)
        elif pep in line6:
            start_pep = line6.find(pep)
            start_dna = start_pep*3+2
            end_dna = start_dna + len(pep)*3
            seq_dna = dna[start_dna:end_dna]
            print('+2')
            print(pep)
            print(seq_dna)
        elif pep in line7:
            start_pep = line7.find(pep)
            end_dna = len(dna)-start_pep*3
            start_dna = end_dna - len(pep)*3
            seq_dna = dna[start_dna:end_dna]
            seq_dna = seq_dna[::-1]
            seq_dna = string.translate(seq_dna, trans)
            print('-0')
            print(pep)
            print(seq_dna)
        elif pep in line8:
            start_pep = line8.find(pep)
            end_dna = len(dna)-start_pep*3-1
            start_dna = end_dna - len(pep)*3
            seq_dna = dna[start_dna:end_dna]
            seq_dna = seq_dna[::-1]
            seq_dna = string.translate(seq_dna, trans)
            print('-1')
            print(pep)
            print(seq_dna)

        elif pep in line9:
            start_pep = line9.find(pep)
            end_dna = len(dna)-start_pep*3-2
            start_dna = end_dna - len(pep)*3
            seq_dna = dna[start_dna:end_dna]
            seq_dna = seq_dna[::-1]
            seq_dna = string.translate(seq_dna, trans)
            print('-2')
            print(pep)
            print(seq_dna)

        else:
            print('--')
            print(pep)
            print(line3)




    else:
        break
inFile.close()
