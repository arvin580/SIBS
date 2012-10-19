#perl stat.pl fusion_point_3_2_complete_c_title2_orig2_nogap_noshort_phase

open INFILE,"$ARGV[0]";
open OUTFILE,">$ARGV[0]\_c2";
while(<INFILE>)
{
@a=split(/\t/,$_);
if($a[0]==$a[2]||$a[2]==-1)
{
$nf++;
}
if($a[1]==$a[3]||$a[3]==-1)
{
$ns++;
}
if(($a[1]==$a[3]||$a[3]==-1)&&($a[0]==$a[2]||$a[2]==-1))
{
$nt++;
}
}
print "$nf\t$ns\t$nt\n";
