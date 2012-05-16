open INFILE,"fusion_point_3_2_complete_c_title_symbol";
open OUTFILE,">fusion_type_chimerdb";
while(<INFILE>)
{
@a=split(/\t/,$_);
@b=split(/:/,$a[0]);
printf OUTFILE "$b[0]:$b[1]\t";

open INFILEa,"EST_Information_Diff_EST.txt";
while(<INFILEa>)
{
if(/$b[0]/ && /$b[1]/)
{
printf OUTFILE "EST_Diff\t";
last;
}
}
close INFILEa;

open INFILEa,"EST_Information_Same_EST.txt";
while(<INFILEa>)
{
if(/$b[0]/ && /$b[1]/)
{
printf OUTFILE "EST_Same\t";
last;
}
}
close INFILEa;

open INFILEa,"mRNA_Information_Diff_mRNA.txt";
while(<INFILEa>)
{
if(/$b[0]/ && /$b[1]/)
{
printf OUTFILE "mRNA_Diff\t";
last;
}
}
close INFILEa;

open INFILEa,"mRNA_Information_Same_mRNA.txt";
while(<INFILEa>)
{
if(/$b[0]/ && /$b[1]/)
{
printf OUTFILE "mRNA_Same\t";
last;
}
}
close INFILEa;

open INFILEa,"PO_down_Mitelman.txt";
while(<INFILEa>)
{
if(/$b[0]/ && /$b[1]/)
{
printf OUTFILE "PO_Mitelman\t";
last;
}
}
close INFILEa;

open INFILEa,"PO_down_OMIM.txt";
while(<INFILEa>)
{
if(/$b[0]/ && /$b[1]/)
{
printf OUTFILE "PO_OMIM\t";
last;
}
}
close INFILEa;


open INFILEa,"PO_down_PubMed.txt";
while(<INFILEa>)
{
if(/$b[0]/ && /$b[1]/)
{
printf OUTFILE "PO_PubMed\t";
last;
}
}
close INFILEa;


open INFILEa,"PO_down_SangerCGP.txt";
while(<INFILEa>)
{
if(/$b[0]/ && /$b[1]/)
{
printf OUTFILE "PO_SangerCGP\t";
last;
}
}
close INFILEa;


open INFILEa,"Solexa.txt";
while(<INFILEa>)
{
if(/$b[0]/ && /$b[1]/)
{
printf OUTFILE "Solexa\t";
last;
}
}
close INFILEa;

open INFILEa,"SRA_Information_Diff_SRA.txt";
while(<INFILEa>)
{
if(/$b[0]/ && /$b[1]/)
{
printf OUTFILE "SRA_Diff\t";
last;
}
}
close INFILEa;




open INFILEa,"SRA_Information_Same_SRA.txt";
while(<INFILEa>)
{
if(/$b[0]/ && /$b[1]/)
{
printf OUTFILE "SRA_Same\t";
last;
}
}
close INFILEa;

printf OUTFILE "\n";


}
