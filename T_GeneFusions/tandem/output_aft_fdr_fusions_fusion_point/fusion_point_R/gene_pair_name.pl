open INFILE,"<gene_pair_name";
while(<INFILE>)
{
	chmod;
	s/\r//g;
	@arr=split(/\s+/,$_);
	$hash{$arr[0]}++;
	$hash{$arr[1]}++;
}
foreach $key (sort by_score keys %hash)
{
$val=$hash{$key};
print "$key\t$val\n";
}

sub by_score
{
        $a_val=$hash{$a};
        $b_val=$hash{$b};
        $b_val<=>$a_val;
}

