inFile = open('12-maxuqant-sequest/HeLa-Peptide-Variant-Maxquant-Sequest-new')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')

inFile.close()
