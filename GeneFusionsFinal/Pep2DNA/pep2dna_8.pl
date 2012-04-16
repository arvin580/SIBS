#perl pep2dna_8.pl fusion_point_3_2_complete_c_title2 /netshare1/home1/people/hansun/GeneFusions/Translate/exon_fusion_peptide_qc
open INFILE,"$ARGV[0]";
open INFILEa,"$ARGV[1]";
open OUTFILE,">$ARGV[0]\_orig";
while($line1=<INFILE>)
{
$line2=<INFILE>;
$line3=<INFILE>;
chomp($line1);
chomp($line2);
chomp($line3);
$line1=~s/\r$//g;
$line2=~s/\r$//g;
$line3=~s/\r$//g;
if($line2=~/(.*\|)\d+\|\d+/)
{
$tt=$1;
open INFILEa,"$ARGV[1]";
while($x=<INFILEa>)
{
$y=<INFILEa>;
chomp($x);
chomp($y);
$x=~s/\r$//g;
$x=~s/^>//g;
$y=~s/\r$//g;
if($x eq $tt)
{
printf OUTFILE "$line1\n";
printf OUTFILE "$line2\n";
printf OUTFILE "$line3\n";
printf OUTFILE "$x\n";
printf OUTFILE "$y\n";
}

}
close INFILEa;
}
}
