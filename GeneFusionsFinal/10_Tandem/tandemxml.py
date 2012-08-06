from xml.etree.ElementTree import *
tree = ElementTree()
tree.parse('output_liuxiaohui_serum2_1210lxh61.2012_03_12_14_00_56.t.xml')

group=tree.findall('group')
for item in group :
    seq=[]
    mgf=[]
    s=item.findall('protein/peptide/domain')
    for it in s :
        seq.append(it.get('seq'))
    m=item.findall('group/note')
    for it in m :
        mgf.append(it.text.strip())

    print('\t'.join(seq))
    print('\t'.join(mgf))
