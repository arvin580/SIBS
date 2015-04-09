inFile = open('invy.jumpy.duppy.1.sv.stat.gene.symbol.heatmap')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    if sum([int(x) for x in fields[1:]]) > 1:
        print(line)
inFile.close()
