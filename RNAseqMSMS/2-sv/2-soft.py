import re
inFile = open('ERR0498-04-05.soft')
ouFile = open('ERR0498-04-05.soft2','w')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    s = re.search('(\d+)S',fields[5])
    if s:
        if int(s.group(1))>5:
            print(line)

inFile.close()
ouFile.close()
