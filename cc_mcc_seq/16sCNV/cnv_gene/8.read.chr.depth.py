inFile = open('/netshare1/home1/szzhongxin/proj1/hansun/Depth/Exome/1.depth')

row = 0
D = {}

D.setdefault('ICC4A', {})
D.setdefault('ICC5A', {})
D.setdefault('ICC9A', {})
D.setdefault('ICC10A', {})
D.setdefault('CHC5A', {})
D.setdefault('CHC6A', {})
D.setdefault('CHC7A', {})
D.setdefault('CHC10A', {})
D.setdefault('ICC4B', {})
D.setdefault('ICC5B', {})
D.setdefault('ICC9B', {})
D.setdefault('ICC10B', {})
D.setdefault('CHC5B', {})
D.setdefault('CHC6B', {})
D.setdefault('CHC7B', {})
D.setdefault('CHC10B', {})

while True:
    line1 = inFile.readline().strip()
    line2 = inFile.readline().strip()
    line3 = inFile.readline().strip()
    line4 = inFile.readline().strip()
    if line1:
        row += 1
        depths = line3.split('\t')
        sites = line4.split('\t')
        D['ICC4A']['chr'+str(row)]=float(depths[0])/float(sites[0])
        D['ICC4B']['chr'+str(row)]=float(depths[1])/float(sites[1])
        D['ICC5A']['chr'+str(row)]=float(depths[2])/float(sites[2])
        D['ICC5B']['chr'+str(row)]=float(depths[3])/float(sites[3])
        D['ICC9A']['chr'+str(row)]=float(depths[4])/float(sites[4])
        D['ICC9B']['chr'+str(row)]=float(depths[5])/float(sites[5])
        D['ICC10A']['chr'+str(row)]=float(depths[6])/float(sites[6])
        D['ICC10B']['chr'+str(row)]=float(depths[7])/float(sites[7])

        D['CHC5A']['chr'+str(row)]=float(depths[8])/float(sites[8])
        D['CHC5B']['chr'+str(row)]=float(depths[9])/float(sites[9])
        D['CHC6A']['chr'+str(row)]=float(depths[10])/float(sites[10])
        D['CHC6B']['chr'+str(row)]=float(depths[11])/float(sites[11])
        D['CHC7A']['chr'+str(row)]=float(depths[12])/float(sites[12])
        D['CHC7B']['chr'+str(row)]=float(depths[13])/float(sites[13])
        D['CHC10A']['chr'+str(row)]=float(depths[14])/float(sites[14])
        D['CHC10B']['chr'+str(row)]=float(depths[15])/float(sites[15])
 
    else:
        break

inFile.close()
