#perl pep2dna_4_2.pl splicing_point_3_2_complete_c_title 
open INFILE,"$ARGV[0]";
open OUTFILE,">$ARGV[0]\_dna";
while($peptide=<INFILE>)
{
$title=<INFILE>;
chomp($title);
$title=~s/\r$//g;
##*****##open INFILEa,"../Translate/exon_fusion";
open INFILEa,"/netshare1/home1/people/hansun/GeneFusions/Translate/splicing_exon";
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
