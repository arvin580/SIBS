inFile = open('ERR0498-04-05.unmapped.unique.human-viruse-checked.num-more_than_two')

for line in inFile:
    line = line.strip()
    fields = line.split('\t')
inFile.close()
