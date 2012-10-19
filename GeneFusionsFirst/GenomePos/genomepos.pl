#perl genomepos.pl fusion_point_3_2_complete_c_title_symbol_unique

open INFILE,"geneID_GeneName_Chr_Strand";
while(<INFILE>)
{
chomp;
s/\r$//g;
@a=split(/\t/,$_);
$hash{$a[-1]}=$_;
}
open INFILEa,"$ARGV[0]";
open OUTFILE,">$ARGV[0]\_pos";
while(<INFILEa>)
{
chomp;
s/\r$//g;
@a=split(/\t/,$_);
@b=split(/:/,$a[0]);
@c=split(/\t/,$hash{$b[0]});
@d=split(/\t/,$hash{$b[1]});
printf OUTFILE "$_\t$c[1]\t$c[5]\t$c[4]\t$d[1]\t$d[5]\t$d[4]\n";

}
