inFile=open('omssa_fusion_point_2')
dict1=dict()

for line in inFile :
    line=line.strip()
    dict1[line]=1

inFile.close()

inFile=open('fusion_point_3_2')

for line in inFile :
    line=line.strip()
    if line in dict1 :
        print(line)
        

inFile.close()


