def select_chr_region(inF,ch,start,end,gene=''):
    inFile = open(inF)
    if gene:
        ouFile = open(inF+'-'+gene+'-'+ch+'-'+str(start)+'-'+str(end),'w')
    else:
        ouFile = open(inF+'-'+ch+'-'+str(start)+'-'+str(end),'w')
    while True:
        line1 = inFile.readline().strip()
        line2 = inFile.readline().strip()
        if line1:
            fields = line1.split('\t')
            ch1 = fields[3]
            ch2 = fields[15]
            pos1_query = int(fields[8])
            pos2_query = int(fields[9])
            pos3_query = int(fields[20])
            pos4_query = int(fields[21])
            pos1_subject = int(fields[10])
            pos2_subject = int(fields[11])
            pos3_subject = int(fields[22])
            pos4_subject = int(fields[23])
            if ch1 == ch:
                if start<= pos1_subject <= end or start<= pos2_subject <=end:
                    ouFile.write(line1+'\n')
                    ouFile.write(line2+'\n')
            elif ch2 == ch:
                if start<= pos3_subject <= end or start<= pos4_subject <=end:
                    ouFile.write(line1+'\n')
                    ouFile.write(line2+'\n')

        else:
            break
    inFile.close()
    ouFile.close()

#select_chr_region('ERR0498-04-05.unmapped.unique.human-viruse-checked','chr8',128230000,128250000)
#select_chr_region('ERR0498-04-05.unmapped.unique.human-viruse-checked','NC_001357.1',1420,1428)
#select_chr_region('ERR0498-04-05.unmapped.unique.human-viruse-checked','NC_001357.1',2236,2244)
#select_chr_region('ERR0498-04-05.unmapped.unique.human-viruse-checked','NC_001357.1',439,447)
#select_chr_region('ERR0498-04-05.unmapped.unique.human-viruse-checked','chr11',108075402,108286638 )
#select_chr_region('ERR0498-04-05.unmapped.unique.human-viruse-checked','chr16',69304112,69519874)
#select_chr_region('ERR0498-04-05.unmapped.unique.human-viruse-checked','chr11',61462834,61663976)
#select_chr_region('ERR0498-04-05.unmapped.unique.human-viruse-checked','chr22',41917295,42160052)
#select_chr_region('ERR0498-04-05.unmapped.unique.human-viruse-checked','chr8',30841215,31048048)

select_chr_region('ERR0498-04-05.unmapped.unique.human-viruse-checked','chr1',43824779-100000,43828873+100000,'CDC20')
select_chr_region('ERR0498-04-05.unmapped.unique.human-viruse-checked','chr15',40886447-100000,40917838+100000,'CASC5')
select_chr_region('ERR0498-04-05.unmapped.unique.human-viruse-checked','chr4',120980579-100000,120988013+100000,'MAD2L1')
select_chr_region('ERR0498-04-05.unmapped.unique.human-viruse-checked','chr17',45199810-100000,45266665+100000,'CDC27')
select_chr_region('ERR0498-04-05.unmapped.unique.human-viruse-checked','chr4',104059508-100000,104061571+100000,'CENPE')
select_chr_region('ERR0498-04-05.unmapped.unique.human-viruse-checked','chr9',140081125-100000,140083057+100000,'ANAPC2')
select_chr_region('ERR0498-04-05.unmapped.unique.human-viruse-checked','chr13',115000362-100000,115008823+100000,'CDC16')

