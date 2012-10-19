open INFILE,"$ARGV[0]";
open OUTFILE,">$ARGV[0]\_point";
while(<INFILE>)
{
@a=split(/\t/,$_);
@b=split(/:/,$a[2]);
$point=$b[-2];
if($a[3]<=$point && ($a[3]+length($a[9])> $point))
{
printf OUTFILE $_;
}
}
