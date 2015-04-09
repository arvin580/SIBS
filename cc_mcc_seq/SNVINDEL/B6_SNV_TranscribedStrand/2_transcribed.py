from PyPlot.PyPlotClass import PyPlot
from PyStats.PyStatsClass import PyStats
type=['TG','TC','TA','CA','CG','CT']
def get_pvalue(List1,List2) :
    star=[]
    ps=PyStats()
    for i in range(len(List1)) :
        p=ps.fisher_test([List1[i],List2[i],(List1[i]+List2[i])/2.0,(List1[i]+List2[i])/2.0])
        if p <10e-6 :
            star.append('***')
        elif p<0.0001 :
            star.append('**')
        elif p<0.01 :
            star.append('*')
        else :
            star.append('')
    return star

def plot_trans(inF,xTitle,legX,legY) :
    inFile=open(inF)
    tran={}
    untran={}
    for line in inFile :
        line=line.strip()
        fields=line.split('\t')
        tran[fields[0]]=int(fields[1])
        untran[fields[0]]=int(fields[2])
    inFile.close()

    tranL=[tran[x] for x in type]
    untranL=[untran[x] for x in type]
    starList=get_pvalue(tranL,untranL)

    pp=PyPlot()
    print(pp.filename)

    pp.multi_bar_star([tranL,untranL],xLabel=['T>G','T>C','T>A','C>A','C>G','C>T'],legTitle=['transcribed strand','untranscribed strand'],xTitle=xTitle,yTitle='Number of SNV',legX=legX,legY=legY,starList=starList)


plot_trans('SNV.genome.somatic.ICC4.trans','ICC4',0.83,0.99)
plot_trans('SNV.genome.somatic.ICC5.trans','ICC5',0.83,0.99)
plot_trans('SNV.genome.somatic.ICC9.trans','ICC9',0.83,0.99)
plot_trans('SNV.genome.somatic.ICC10.trans','ICC10',0.83,0.99)

plot_trans('SNV.genome.somatic.CHC5.trans','CHC5',0.83,0.99)
plot_trans('SNV.genome.somatic.CHC6.trans','CHC6',0.83,0.99)
plot_trans('SNV.genome.somatic.CHC7.trans','CHC7',0.83,0.99)
plot_trans('SNV.genome.somatic.CHC10.trans','CHC10',0.83,0.99)
