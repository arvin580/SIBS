#perl frameshift2.pl fusion_point_3_2_complete_c_title2_orig2_nogap_noshort_c_phase

open INFILE,"$ARGV[0]";
open OUTFILE,">$ARGV[0]\_c";
open OUTFILEa,">$ARGV[0]\_cc";
while(<INFILE>)
{
@a=split(/\t/,$_);
if($a[2]==-1 || $a[3]==-1)
{
printf OUTFILE $_;
}
else
{
printf OUTFILEa $_;
}
}
