#perl pep2dna_11.pl fusion_point_3_2_complete_c_title2_orig2_gap_noshort fusion_point_3_2_complete_c_title2_orig2_gap_short
open INFILEa,"$ARGV[0]";
open INFILEb,"$ARGV[1]";
open OUTFILEa,">$ARGV[0]\_c";
open OUTFILEb,">$ARGV[1]\_c";

while(<INFILEa>)
{
@a=split(/\t/,$_);
if(index($a[0],"*")==-1)
{
printf OUTFILEa $_;
}
else
{
printf OUTFILEb $_;
}
}
while(<INFILEb>)
{
printf OUTFILEb $_;
}
