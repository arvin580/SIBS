#perl pep2dna_4.pl fusion_point_3_2_complete_c_title
#perl pep2dna_4.pl splicing_point_3_2_complete_c_title 
open INFILE,"$ARGV[0]";
open OUTFILE,">$ARGV[0]\_dna";
while($peptide=<INFILE>)
{
$title=<INFILE>;
chomp($title);
$title=~s/\r$//g;
if($ARGV[0]=~/fusion/)
{

open INFILEa,"../Translate/exon_fusion";
}
else
{
open INFILEa,"../Translate/splicing_exon";
}
while($s1=<INFILEa>)
{
$s2=<INFILEa>;
if($s1=~/$title/)
{
printf OUTFILE "$peptide";
#printf OUTFILE "$title\n";
printf OUTFILE "$s1";
printf OUTFILE "$s2";
}
}
close(INFILEa)
}
