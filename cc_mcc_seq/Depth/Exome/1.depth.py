import sys

for i in range(3):
    line = sys.stdin.readline()

depth = [0]*16
depth2 = [0]*16
site = [0]*16
site2 = [0]*16

while True:
    line = sys.stdin.readline()
    if line:
        line = line.strip()
        fields = line.split('\t')
        for i,item in enumerate(fields[-16:]):
            d = int(item.split(':')[1])
            if d >800:
                depth[i]+=800
            else:
                depth[i]+=d
            if d > 0 :
                site[i] += 1
            if d > 30:
                site2[i] += 1
                if d >800:
                    depth2[i]+=800
                else:
                    depth2[i]+=d
    else:
        break

print('\t'.join([str(x) for x in depth]))
print('\t'.join([str(x) for x in site]))
print('\t'.join([str(x) for x in depth2]))
print('\t'.join([str(x) for x in site2]))
