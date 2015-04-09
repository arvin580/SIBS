translocation=[7, 9, 14, 20, 17, 10, 3, 3, 8, 13, 12, 9, 7, 7, 4, 3, 6, 6, 6, 4]
deletion=[372, 447, 441, 510, 528, 447, 480, 409, 549, 429, 516, 589, 564, 487, 374, 265, 314, 276, 333, 367]
inversion=[7, 8, 13, 10, 8, 8, 5, 7, 12, 3, 6, 7, 11, 9, 6, 8, 6, 6, 8, 9]
duplication=[15, 15, 16, 8, 14, 9, 9, 10, 4, 13, 11, 17, 11, 13, 17, 14, 9, 11, 10, 6]

translocation_icc_total = sum(translocation[0:10])
deletion_icc_total = sum(deletion[0:10])
inversion_icc_total = sum(inversion[0:10])
duplication_icc_total = sum(duplication[0:10])

translocation_chc_total = sum(translocation[10:])
deletion_chc_total = sum(deletion[10:])
inversion_chc_total = sum(inversion[10:])
duplication_chc_total = sum(duplication[10:])

translocation_total = sum(translocation[0:])
deletion_total = sum(deletion[0:])
inversion_total = sum(inversion[0:])
duplication_total = sum(duplication[0:])

print(deletion_icc_total)
print(duplication_icc_total)
print(inversion_icc_total)
print(translocation_icc_total)

print(deletion_chc_total)
print(duplication_chc_total)
print(inversion_chc_total)
print(translocation_chc_total)

print(deletion_total)
print(duplication_total)
print(inversion_total)
print(translocation_total)

print('*******************')


translocation=[4, 4, 8, 8, 7, 6, 3, 2, 6, 6, 7, 4, 4, 5, 1, 1, 3, 5, 3, 2]
deletion=[144, 156, 162, 191, 191, 165, 172, 139, 178, 146, 177, 204, 194, 164, 133, 92, 103, 103, 111, 125]
inversion=[3, 2, 5, 3, 2, 1, 1, 3, 5, 1, 1, 3, 4, 4, 0, 4, 1, 3, 2, 4]
duplication=[7, 5, 8, 4, 5, 2, 4, 3, 1, 8, 5, 9, 6, 4, 6, 2, 4, 5, 6, 0]


translocation_icc_total = sum(translocation[0:10])
deletion_icc_total = sum(deletion[0:10])
inversion_icc_total = sum(inversion[0:10])
duplication_icc_total = sum(duplication[0:10])

translocation_chc_total = sum(translocation[10:])
deletion_chc_total = sum(deletion[10:])
inversion_chc_total = sum(inversion[10:])
duplication_chc_total = sum(duplication[10:])

translocation_total = sum(translocation[0:])
deletion_total = sum(deletion[0:])
inversion_total = sum(inversion[0:])
duplication_total = sum(duplication[0:])

print(deletion_icc_total)
print(duplication_icc_total)
print(inversion_icc_total)
print(translocation_icc_total)

print(deletion_chc_total)
print(duplication_chc_total)
print(inversion_chc_total)
print(translocation_chc_total)

print(deletion_total)
print(duplication_total)
print(inversion_total)
print(translocation_total)

print('*******************')




