import sys
inFile = open(sys.argv[1])
D = dict()
while True:
    head = inFile.readline().strip()
    if head:
        fields = head.split()
        D.setdefault(fields[0],0)
        D[fields[0]] += 1
    else:
        break
inFile.close()

for k in D:
    if D[k] > 1:
        print(k)
        print(D[k])
