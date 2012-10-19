#perl pep2dna_7.pl fusion_point_3_2_complete_c 
open INFILE,"$ARGV[0]";
open OUTFILE,">$ARGV[0]\_title2";
while($peptide=<INFILE>)
{
$num++;
if($peptide=~/^\#/)
{
$title=<INFILE>;
$num++;
if($title=~/^>/)
{
$title=~s/^>//g;
@a=split(/\&/,$title);
$a[0]=~s/^>//g;
chomp($a[0]);
$comp=<INFILE>;
printf OUTFILE "$peptide$a[0]\n$comp";
}
else
{
print "ERROR:$num\n";
}

}
}
