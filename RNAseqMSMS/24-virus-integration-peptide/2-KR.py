inFile = open('ERR0498-04-05.unmapped.unique.human-viruse-checked.num-more_than_two.fa')
ouFile = open('ERR0498-04-05.unmapped.unique.human-viruse-checked.num-more_than_two.fa.fa','w')

while True:
    line1 = inFile.readline().strip()
    line2 = inFile.readline().strip()
    if line1:
        fields = line1.split('\t')
        point = int(fields[-1])
    else:
        break
inFile.close()
ouFile.close()

