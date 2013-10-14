inFile = open('ERR0498-04-05.unmapped.unique.human-viruse-checked.num-more_than_two')

for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    pos1 = fields[10]
    pos2 = fields[11]
    pos3 = fields[22]
    pos3 = fields[23]

inFile.close()
