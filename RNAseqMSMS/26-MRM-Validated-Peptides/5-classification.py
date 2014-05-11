D = {}
inFile = open('HeLa-Peptide-Variant-MaxQuant-XTandem')
for line in inFile:
    line = line.strip()
    if line.find('SNV') != -1:
        D.setdefault('SNV', 0)
        D['SNV'] += 1
    elif line.find('INDEL') != -1:
        D.setdefault('INDEL', 0)
        D['INDEL'] += 1
    elif line.find('Deletion') != -1:
        D.setdefault('Deletion', 0)
        D['Deletion'] += 1
    elif line.find('Duplication') != -1:
        D.setdefault('Duplication', 0)
        D['Duplication'] += 1
    elif line.find('Inversion') != -1:
        D.setdefault('Inversion', 0)
        D['Inversion'] += 1
    elif line.find('Translocation') != -1:
        D.setdefault('Translocation', 0)
        D['Translocation'] += 1
    elif line.find('VIRUS') != -1:
        D.setdefault('Virus', 0)
        D['Virus'] += 1
inFile.close()
print(D)
for k in D:
    print(k + '\t' + str(D[k]))
