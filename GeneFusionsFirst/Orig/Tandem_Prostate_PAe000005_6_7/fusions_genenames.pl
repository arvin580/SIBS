open INFILE,"$ARGV[0]";
while(<INFILE>)
{
if(/genefusions:(\w+):(\w+):/)
{
$hash{"$1\t$2"}++;
}
}
while(($key,$val)=each %hash)
{
print "$key\t$val\n";
}
