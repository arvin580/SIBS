import sys
head = 3537
D = dict()
inFile = open(sys.argv[1])

for n in range(head):
    inFile.readline()

for line in inFile:
    try:
        fields = line.split('\t')
        flag = int(fields[1])
        D.setdefault(flag, 0)
        D[flag] += 1
        if flag != 4:
            print(fields[9])
    except:
        pass
        

inFile.close()

for k in D:
    print(str(k) + '\t' + str(D[k]))




