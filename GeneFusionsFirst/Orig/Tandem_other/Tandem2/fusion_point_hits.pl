#print:outputfile $ARGV[0]:inputfile $ARGV[1]:flag for whether output groupid
open INFILE,$ARGV[0];
while(<INFILE>)
{
chomp;
s/\r$//;
@arr=split(/\t/,$_);
$hash{$arr[9]}[0]++;
$hash{$arr[9]}[1].="$arr[0]\t";
}
foreach $key (sort by_score keys %hash)
{
$val=$hash{$key}[0];
$val2=$hash{$key}[1];
if($val>=1)
{
if($ARGV[1]==1)
{
print "$key\t$val\t$val2\n";
}
else
{
print "$key\t$val\n";
}

}
}
sub by_score
{
        $a_val=$hash{$a}[0];
        $b_val=$hash{$b}[0];
        $b_val<=>$a_val;
}
