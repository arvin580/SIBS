import sys

inFile = open(sys.argv[1])
row = 0
bs = 0
for line in inFile:
    row += 1
    line = line.strip()
    fields = line.split('\t')
    repeat = int(fields[0])
    notrepeat = int(fields[1])
    if row == 1:
        repeat_notrepeat = float(repeat + 1)/float(notrepeat + 1)
        print(repeat_notrepeat)
    else:
        #if float(repeat + 1)/float(notrepeat + 1) >= repeat_notrepeat:
        if float(repeat + 1)/float(notrepeat + 1) >= 10:
            bs += 1
inFile.close()

print(bs)
