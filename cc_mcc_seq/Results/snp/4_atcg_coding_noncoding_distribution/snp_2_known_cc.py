dict1=dict()
dict2=dict()
inFile=open('sum_snp.genome_combined.sorted.pass012.known.atcg.coding_noncoding')
for line in inFile :
    line=line.strip('\r\n')
    fields=line.split('\t')
    dict1.setdefault(fields[0],{})
    dict2.setdefault(fields[0],{})
    dict1[fields[0]][fields[1]]=[int(i) for i in fields[2:12]]
    dict2[fields[0]][fields[1]]=[int(i) for i in fields[12:22]]

inFile.close()


dict7=dict()
dict7['Genomic']=3095.6939830
dict7['Coding']=63.8689240
dict7['Non-Coding']=278.878894
dict7['Intronic']=917.8244030
dict7['Intergenic']=1889.0479750
#dict5['UTR']=155.9631540
#dict5['ncRNA']=122.9157400




for key1 in dict1  :
    for key2 in dict1[key1] :
        for i in range(len(dict1[key1][key2])) :
            dict1[key1][key2][i]=dict1[key1][key2][i]/dict7[key1]

for key1 in dict2  :
    for key2 in dict2[key1] :
        for i in range(len(dict2[key1][key2])) :
            dict2[key1][key2][i]=dict2[key1][key2][i]/dict7[key1]



type=['AT','AC','AG','TA','TC','TG','CA','CT','CG','GA','GT','GC']
type2=['T>G/A>C','T>C/A>G','T>A/A>T','C>A/G>T','C>G/G>C','C>T/G>A']
type3=['Coding','Non-Coding','Intronic','Intergenic']
dict3=dict()
dict4=dict()
dict5=dict()
dict6=dict()

for it in type3 : 
    dict5.setdefault(it,{})
    dict6.setdefault(it,{})
    for item in type2 :
        dict5[it].setdefault(item,[0]*10)
        dict6[it].setdefault(item,[0]*10)

for item in type3 : 
    for i in range(10) :
        dict5[item][type2[0]][i]=dict1[item]['TG'][i]+dict1[item]['AC'][i]
        dict5[item][type2[1]][i]=dict1[item]['TC'][i]+dict1[item]['AG'][i]
        dict5[item][type2[2]][i]=dict1[item]['TA'][i]+dict1[item]['AT'][i]
        dict5[item][type2[3]][i]=dict1[item]['CA'][i]+dict1[item]['GT'][i]
        dict5[item][type2[4]][i]=dict1[item]['CG'][i]+dict1[item]['GC'][i]
        dict5[item][type2[5]][i]=dict1[item]['CT'][i]+dict1[item]['GA'][i]
        dict6[item][type2[0]][i]=dict2[item]['TG'][i]+dict2[item]['AC'][i]
        dict6[item][type2[1]][i]=dict2[item]['TC'][i]+dict2[item]['AG'][i]
        dict6[item][type2[2]][i]=dict2[item]['TA'][i]+dict2[item]['AT'][i]
        dict6[item][type2[3]][i]=dict2[item]['CA'][i]+dict2[item]['GT'][i]
        dict6[item][type2[4]][i]=dict2[item]['CG'][i]+dict2[item]['GC'][i]
        dict6[item][type2[5]][i]=dict2[item]['CT'][i]+dict2[item]['GA'][i]







import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt

for key in type3 :
    dict3.setdefault(key,{})
    dict4.setdefault(key,{})
    for item in type2 :
        dict3[key].setdefault(item,[])
        dict4[key].setdefault(item,[])

        dict3[key][item].append(np.array(dict5[key][item]).mean())
        dict3[key][item].append(np.array(dict5[key][item]).std())
        dict3[key][item].append(np.array(dict5[key][item]))

        dict4[key][item].append(np.array(dict6[key][item]).mean())
        dict4[key][item].append(np.array(dict6[key][item]).std())
        dict4[key][item].append(np.array(dict6[key][item]))

#    dict3[item].append(np.array([i/300 for i in dict1[item]]).mean())
#    dict3[item].append(np.array([i/300 for i in dict1[item]]).std())
#    dict3[item].append(np.array([i/300 for i in dict1[item]]))

#    dict4[item].append(np.array([i/300 for i in dict2[item]]).mean())
#    dict4[item].append(np.array([i/300 for i in dict2[item]]).std())
#    dict4[item].append(np.array([i/300 for i in dict2[item]]))
 

#N = len(type)
#danMean   = [dict3[item][0] for item in type]
#hunMean   = [dict4[item][0] for item in type]
#danStd   = [dict3[item][1] for item in type]
#hunStd  = [dict4[item][1] for item in type]
danMean=dict()
hunMean=dict()
danStd=dict()
hunStd=dict()

for key in type3 :
    danMean[key] = [dict3[key][item][0] for item in type2]
    hunMean[key]   = [dict4[key][item][0] for item in type2] 
    danStd[key]   = [dict3[key][item][1] for item in type2]
    hunStd[key]  = [dict4[key][item][1] for item in type2]


fig = plt.figure()
ax = fig.add_subplot(111)

N = len(type2)
ind = np.arange(N)    # the x locations for the groups
width = 0.15       # the width of the bars: can also be len(x) sequence

p0 = ax.bar(ind, danMean[type3[0]],   width, color='r', yerr=danStd[type3[0]])
p1 = ax.bar(ind+width, danMean[type3[1]],   width, color='y', yerr=danStd[type3[1]])
p2 = ax.bar(ind+2*width, danMean[type3[2]],   width, color='b', yerr=danStd[type3[2]])
p3 = ax.bar(ind+3*width, danMean[type3[3]],   width, color='g', yerr=danStd[type3[3]])
#p4 = ax.bar(ind+4*width, danMean[type3[4]],   width, color='c', yerr=danStd[type3[4]])


ax.set_xlim(-0.25,6)
ax.set_ylim(0,)
ax.set_ylabel('Substitutions per Mb')
#plt.yticks(np.arange(0,81,10))

ax.set_xticks(ind+width*2.5)
ax.set_xticklabels(type2) 
#ax.legend( (p1[0], p2[0]), ('CC', 'MCC') )
#ax.legend( (p0[0], p1[0],p2[0],p3[0],p4[0]), ('exonic', 'intronic','UTR','ncRNA','intergenic'),loc='upper right',bbox_to_anchor=(0.85,0.95))
ax.legend( (p0[0], p1[0],p2[0],p3[0]), ('Coding', 'Non-Coding','Intronic','Intergenic'),loc='upper right',bbox_to_anchor=(0.85,0.95))




plt.savefig('sum_snp.genome_combined.sorted.pass012.known.atcg.cc.coding_noncoding.pdf')



'''

N = 5
menMeans   = (20, 35, 30, 35, 27)
womenMeans = (25, 32, 34, 20, 25)
menStd     = (2, 3, 4, 1, 2)
womenStd   = (3, 5, 2, 3, 3)
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, menMeans,   width, color='r', yerr=womenStd)
p2 = plt.bar(ind, womenMeans, width, color='y',
                     bottom=menMeans, yerr=menStd)

plt.ylabel('Scores')
plt.title('Scores by group and gender')
plt.xticks(ind+width/2., ('G1', 'G2', 'G3', 'G4', 'G5') )
plt.yticks(np.arange(0,81,10))
plt.legend( (p1[0], p2[0]), ('Men', 'Women') )

plt.show()

'''
