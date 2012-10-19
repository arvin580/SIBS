open INFILE,"peptide_complete_c_title_dna";
open OUTFILE,">peptide_complete_c_title_dna_c";
while($s1=<INFILE>)
{
chomp($s1);
$s2=<INFILE>;
$s3=<INFILE>;
$s4=<INFILE>;
printf OUTFILE ">$s1|$s2";
printf OUTFILE "$s4";

}
