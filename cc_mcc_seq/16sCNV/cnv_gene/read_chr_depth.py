inFile = open('/netshare1/home1/szzhongxin/proj1/hansun/Depth/Exome/1.depth')

row = 0
Depth = {}

Depth.setdefault('ICC4A', {})
Depth.setdefault('ICC5A', {})
Depth.setdefault('ICC9A', {})
Depth.setdefault('ICC10A', {})
Depth.setdefault('CHC5A', {})
Depth.setdefault('CHC6A', {})
Depth.setdefault('CHC7A', {})
Depth.setdefault('CHC10A', {})
Depth.setdefault('ICC4B', {})
Depth.setdefault('ICC5B', {})
Depth.setdefault('ICC9B', {})
Depth.setdefault('ICC10B', {})
Depth.setdefault('CHC5B', {})
Depth.setdefault('CHC6B', {})
Depth.setdefault('CHC7B', {})
Depth.setdefault('CHC10B', {})

while True:
    line1 = inFile.readline().strip()
    line2 = inFile.readline().strip()
    line3 = inFile.readline().strip()
    line4 = inFile.readline().strip()
    if line1:
        row += 1
        depths = line3.split('\t')
        sites = line4.split('\t')
        if row <= 22:
            Depth['ICC4A']['chr'+str(row)]=float(depths[0])/float(sites[0])
            Depth['ICC5A']['chr'+str(row)]=float(depths[1])/float(sites[1])
            Depth['ICC9A']['chr'+str(row)]=float(depths[2])/float(sites[2])
            Depth['ICC10A']['chr'+str(row)]=float(depths[3])/float(sites[3])
            Depth['CHC5A']['chr'+str(row)]=float(depths[4])/float(sites[4])
            Depth['CHC6A']['chr'+str(row)]=float(depths[5])/float(sites[5])
            Depth['CHC7A']['chr'+str(row)]=float(depths[6])/float(sites[6])
            Depth['CHC10A']['chr'+str(row)]=float(depths[7])/float(sites[7])

            Depth['ICC4B']['chr'+str(row)]=float(depths[8])/float(sites[8])
            Depth['ICC5B']['chr'+str(row)]=float(depths[9])/float(sites[9])
            Depth['ICC9B']['chr'+str(row)]=float(depths[10])/float(sites[10])
            Depth['ICC10B']['chr'+str(row)]=float(depths[11])/float(sites[11])
            Depth['CHC5B']['chr'+str(row)]=float(depths[12])/float(sites[12])
            Depth['CHC6B']['chr'+str(row)]=float(depths[13])/float(sites[13])
            Depth['CHC7B']['chr'+str(row)]=float(depths[14])/float(sites[14])
            Depth['CHC10B']['chr'+str(row)]=float(depths[15])/float(sites[15])

        elif row == 23:
            Depth['ICC4A']['chrX']=float(depths[0])/float(sites[0])
            Depth['ICC5A']['chrX']=float(depths[1])/float(sites[1])
            Depth['ICC9A']['chrX']=float(depths[2])/float(sites[2])
            Depth['ICC10A']['chrX']=float(depths[3])/float(sites[3])
            Depth['CHC5A']['chrX']=float(depths[4])/float(sites[4])
            Depth['CHC6A']['chrX']=float(depths[5])/float(sites[5])
            Depth['CHC7A']['chrX']=float(depths[6])/float(sites[6])
            Depth['CHC10A']['chrX']=float(depths[7])/float(sites[7])

            Depth['ICC4B']['chrX']=float(depths[8])/float(sites[8])
            Depth['ICC5B']['chrX']=float(depths[9])/float(sites[9])
            Depth['ICC9B']['chrX']=float(depths[10])/float(sites[10])
            Depth['ICC10B']['chrX']=float(depths[11])/float(sites[11])
            Depth['CHC5B']['chrX']=float(depths[12])/float(sites[12])
            Depth['CHC6B']['chrX']=float(depths[13])/float(sites[13])
            Depth['CHC7B']['chrX']=float(depths[14])/float(sites[14])
            Depth['CHC10B']['chrX']=float(depths[15])/float(sites[15])
        elif row == 24:
            Depth['ICC4A']['chrY']=float(depths[0])/float(sites[0])
            Depth['ICC5A']['chrY']=float(depths[1])/float(sites[1])
            Depth['ICC9A']['chrY']=float(depths[2])/float(sites[2])
            Depth['ICC10A']['chrY']=float(depths[3])/float(sites[3])
            Depth['CHC5A']['chrY']=float(depths[4])/float(sites[4])
            Depth['CHC6A']['chrY']=float(depths[5])/float(sites[5])
            Depth['CHC7A']['chrY']=float(depths[6])/float(sites[6])
            Depth['CHC10A']['chrY']=float(depths[7])/float(sites[7])

            Depth['ICC4B']['chrY']=float(depths[8])/float(sites[8])
            Depth['ICC5B']['chrY']=float(depths[9])/float(sites[9])
            Depth['ICC9B']['chrY']=float(depths[10])/float(sites[10])
            Depth['ICC10B']['chrY']=float(depths[11])/float(sites[11])
            Depth['CHC5B']['chrY']=float(depths[12])/float(sites[12])
            Depth['CHC6B']['chrY']=float(depths[13])/float(sites[13])
            Depth['CHC7B']['chrY']=float(depths[14])/float(sites[14])
            Depth['CHC10B']['chrY']=float(depths[15])/float(sites[15])

    else:
        break

inFile.close()


