import sys
inFile = open('ERR0498-04-05.mpileup')
ouFile = open('ERR0498-04-05.mpileup.depth', 'w')

MIN = 5
MAX = 500
D = {}
for i in range(3):
    line = inFile.readline()
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    ch = fields[0]
    try:
        dp = int(fields[7].split(';')[0].split('DP=')[1])
        print(line)
        D.setdefault(ch, [0, 0])
        if dp >= MIN:
            if dp <= MAX:
                D[ch][0] += dp
                D[ch][1] += 1
            else:
                D[ch][0] += MAX
                D[ch][1] += 1
    except:
        pass
            
inFile.close()
for k in D:
    ouFile.write(k + '\t' + str(float(D[k][0])/D[k][1]) + '\n')
ouFile.close()
