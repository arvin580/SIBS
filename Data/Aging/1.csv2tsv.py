import csv

def csv2tsv(iFile):
    inFile = open(iFile)
    ouFile1 = open(iFile.rstrip('.csv')+'.txt', 'w')
    csvFile = csv.reader(inFile)
    head = csvFile.next()
    for fields in csvFile:
        ouFile1.write('\t'.join(fields) + '\n')
    inFile.close()
    ouFile1.close()

csv2tsv('genage_human.csv')
