import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt 

def snv_number(inF, xLabel=[]):
    snv = [0]*16
    snv2 = [0]*16
    snv3 = [0]*16
    inFile = open(inF)
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        for i, item  in enumerate(fields[-16:]):
            if item.find('0/0') == -1:
                if float(item.split(':')[-1]) >= 0:
                    snv[i] += 1
                if float(item.split(':')[-1]) >= 10:
                    snv2[i] += 1
                if float(item.split(':')[-1]) >= 20:
                    snv3[i] += 1



    inFile.close()
    
    leg = []
    fig = plt.figure()
    #ax = fig.add_axes([0.1,0.1,0.7,0.8])
    ax = fig.add_subplot(111)
    #ax.set_yscale('log')
    #ax.plot(range(1,9),snv[0:8],range(1,9),snv[8:],range(1,9),[10000,13000,11100,8000,9000,10000,11000,14000])
    ax.plot(range(1,9),snv[0:8],range(1,9),snv[8:],range(1,9),snv2[0:8],range(1,9),snv2[8:],range(1,9),snv3[0:8],range(1,9),snv3[8:])
    ax.set_xticks(range(10))
    if xLabel:
        ax.set_xticklabels(['']+xLabel+[''])
    ax.set_ylabel('SNV Number')
    ax.legend([r'Tumor($Q \geq 0$)',r'Normal($Q \geq 0$)',r'Tumor($Q \geq 10$)',r'Normal($Q \geq 10$)',r'Tumor($Q \geq 20$)',r'Normal($Q \geq 20$)'],loc='upper left',bbox_to_anchor=[0.9,0.95],prop={'size':6})
    #ax.legend(['Tumor','Normal','Somatic'],loc='upper right',bbox_to_anchor=[0.97,0.97])
    plt.grid(True)

    plt.savefig(inF+'.num.pdf')
    return snv

snv=snv_number('sum_snv16s.genome_summary', xLabel=['ICC4','ICC5','ICC9','ICC10','CHC5','CHC6','CHC7','CHC10'])
'''
snv=snv_number('sum_snv16s.exome_summary', 0, xLabel=['ICC4','ICC5','ICC9','ICC10','CHC5','CHC6','CHC7','CHC10'])
print(snv)
snv=snv_number('sum_snv16s.genome_summary', 0, xLabel=['ICC4','ICC5','ICC9','ICC10','CHC5','CHC6','CHC7','CHC10'])
print(snv)

snv=snv_number('sum_snv16s.exome_summary', 10, xLabel=['ICC4','ICC5','ICC9','ICC10','CHC5','CHC6','CHC7','CHC10'])
print(snv)
snv=snv_number('sum_snv16s.genome_summary', 10, xLabel=['ICC4','ICC5','ICC9','ICC10','CHC5','CHC6','CHC7','CHC10'])
print(snv)

snv=snv_number('sum_snv16s.exome_summary', 20, xLabel=['ICC4','ICC5','ICC9','ICC10','CHC5','CHC6','CHC7','CHC10'])
print(snv)
snv=snv_number('sum_snv16s.genome_summary', 20, xLabel=['ICC4','ICC5','ICC9','ICC10','CHC5','CHC6','CHC7','CHC10'])
print(snv)
'''



