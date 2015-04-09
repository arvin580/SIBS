inFile = open('br.txt')
sv = {}
seq = []
L = 35
for line in inFile:
    line = line.strip()
    fields = line.split()
    if len(fields) > 2:
        if fields[0].find('chr')!=0:
            s = ''.join(fields[0:-1])
            n = 0
            for item in fields[0:-1]:
                if len(item)>35:
                    n += 1
            if n >= 2:
                seq.append(s)
        
        else:
            k=':'.join(fields)
            sv[k] = seq
            seq = []


inFile.close()

for key in sv:
    if sv[key]:
        print('>'+key)
        print(sv[key][0])
