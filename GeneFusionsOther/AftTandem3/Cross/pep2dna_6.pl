#perl pep2dna_6.pl fusion_point_3_2_complete_c_title_dna
#perl pep2dna_6.pl splicing_point_3_2_complete_c_title_dna
open INFILE,"$ARGV[0]";
open OUTFILE,">$ARGV[0]\_c";
while($s1=<INFILE>)
{
chomp($s1);
$s2=<INFILE>;
$s3=<INFILE>;
$s2=~s/^>//g;
printf OUTFILE ">$s1|$s2";
printf OUTFILE "$s3";

}
