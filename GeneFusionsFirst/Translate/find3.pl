open INFILE,"<$ARGV[0]";
while($title=<INFILE>)
{
$seq=<INFILE>;
if($title eq ">$ARGV[1]\n")
{
print $title;
print $seq;
}
}
