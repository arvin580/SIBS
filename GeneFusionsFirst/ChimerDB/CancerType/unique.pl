open INFILE,"$ARGV[0]";
while(<INFILE>)
{
$hash{$_}++;
}
while(($key,$val)=each %hash)
{
print $key;
}
