#perl pep2dna_2.pl fusion_point_3_2_complete
#perl pep2dna_2.pl splicing_point_3_2_complete
open INFILE,"$ARGV[0]";
open OUTFILE,">$ARGV[0]\_c";
while(<INFILE>)
{
$n++;
if(/^#/ && $n!=1)
{
if(!($pep=~/annotated/))
{
printf OUTFILE $pep;
}
$pep=undef;
}
$pep.=$_;
}
if(!($pep=~/annotated/))
{
printf OUTFILE $pep;
$pep=undef;
}
