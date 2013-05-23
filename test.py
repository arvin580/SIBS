start1_query=1
end1_query=54
start2_query=41
end2_query=76
seq1='GTTGTCTATAGCCTCCGTACTGCCGCCACTACATACATTGCCGCCATGTTCGCC'
seq2='CCGCCAGATCGCCCTGCAGGAGAAGCACGACGCGG'
CCGCCAGATCGCCCTGCAGGAGAAGCACGACGCGG

L0 = ['0']*76
L1 = ['0']*76
L2 = ['0']*76


for i in range(start1_query-1, end1_query):
    print(i-start1_query+1)
for i in range(start2_query-1, end2_query):
    print(i-start2_query+1)
    #L2[i]=seq2[i-start2_query+1]

