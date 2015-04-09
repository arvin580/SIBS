import sys
inFile = open(sys.argv[1])
D = dict()
while True:
    head = inFile.readline().strip()
    seq = inFile.readline().strip()
    if head:
        D.setdefault(head,0)
        D[head] += 1
    else:
        break
inFile.close()

for k in D:
    if D[k] > 1:
        print(k)
        print(D[k])
