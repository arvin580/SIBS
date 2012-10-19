open INFILE,"fusion_point_3_2_complete_c_title_symbol";
while(<INFILE>)
{
@a=split(/\t/,$_);
if($a[-1]==0)
{
print "$a[0]\n";
}
}
