import csv


def csv2tsv(iFile):
    inFile = open(iFile)
    ouFile1 = open(iFile.rstrip('.csv'), 'w')
    ouFile2 = open(iFile.rstrip('.csv')+'.indel', 'w')
    csvFile = csv.reader(inFile)
    head = csvFile.next()
    for fields in csvFile:
        if fields[33].find('INDEL')==0:
            ouFile2.write('\t'.join(fields) + '\n')
        else:
            ouFile1.write('\t'.join(fields) + '\n')
    inFile.close()
    ouFile1.close()
    ouFile2.close()

csv2tsv('sum_snv16sExome.exome_summary.csv')
csv2tsv('sum_snv16sExome.genome_summary.csv')
