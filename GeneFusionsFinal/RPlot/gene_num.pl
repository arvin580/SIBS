#perl gene_num.pl fusion_point_3_2_complete_c_title_symbol_3
#perl gene_num.pl splicing_point_3_2_complete_c_title_symbol_2
open INFILE,"$ARGV[0]";
open OUTFILE,">$ARGV[0]\_num";
while(<INFILE>)
{
@a=split(/\t/,$_);
@b=split(/:/,$a[0]);
$hash{$b[0]}++;
$hash{$b[1]}++;
}

foreach $key (sort by_score keys %hash)
{
printf OUTFILE "$key\t$hash{$key}\n";
}

sub by_score
{
        $hash{$b}<=>$hash{$a};
}
