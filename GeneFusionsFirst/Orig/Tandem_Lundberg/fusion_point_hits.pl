#print:outputfile $ARGV[0]:inputfile $ARGV[1]:flag for whether output groupid
open INFILE,$ARGV[0];
while(<INFILE>)
{
chomp;
s/\r$//;
@arr=split(/\t/,$_);
$hash{$arr[9]}[0]++;
$hash{$arr[9]}[1].="$arr[0]\n";
}
foreach $key (sort by_score keys %hash)
{
$val=$hash{$key}[0];
$val2=$hash{$key}[1];
if($val>=1)
{
if($ARGV[1]==1)
{
print "$key\n$val\n$val2\n";
}
elsif($ARGV[1]==0)
{
print "$key\t$val\n";
}
elsif($ARGV[1]==2)
{
print "$key\n";
}

}
}
sub by_score
{
        $a_val=$hash{$a}[0];
        $b_val=$hash{$b}[0];
        $b_val<=>$a_val;
}
