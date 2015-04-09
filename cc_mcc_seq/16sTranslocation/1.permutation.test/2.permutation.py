import sys

inFile = open(sys.argv[1])
row = 0
bs = 0
L = []
for line in inFile:
    row += 1
    line = line.strip()
    fields = line.split('\t')
    repeat = int(fields[0])
    notrepeat = int(fields[1])
    if row == 1:
        #repeat_notrepeat = float(repeat + 1)/float(notrepeat + 1)
        repeat_notrepeat = float(repeat)/float(notrepeat + repeat)
        print(repeat_notrepeat)
    else:
        if float(repeat)/float(notrepeat + repeat ) >= repeat_notrepeat:
            bs += 1
        L.append(float(repeat )/float(notrepeat + repeat))
inFile.close()

L.sort()
print(bs)
