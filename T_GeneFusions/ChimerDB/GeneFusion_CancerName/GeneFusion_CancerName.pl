open INFILEa,"<PO_down_PubMed.txt";
open INFILEb,"<PO_down_OMIM.txt";
open INFILEc,"<PO_down_SangerCGP.txt";
open INFILEd,"<PO_down_Mitelman.txt";
open OUTFILE,">GeneFusion_CancerName";


while(<INFILEa>)
{
chomp;
s/\r//;
@line=split(/\t/,$_);
$fusion="$line[0]\t$line[1]";
$fusion2="$line[1]\t$line[0]";
if(exists($myhash{$fusion}))
{
$len=@{$myhash{$fusion}};
$myhash{$fusion}[$len]=$line[2];
}
elsif(exists($myhash{$fusion2}))
{
$len=@{$myhash{$fusion2}};
$myhash{$fusion2}[$len]=$line[2];

}
else
{
$len=@{$myhash{$fusion}};
$myhash{$fusion}[$len]=$line[2];
}
}

while(<INFILEb>)
{
chomp;
s/\r//;
@line=split(/\t/,$_);
$fusion="$line[2]\t$line[4]";
$fusion2="$line[4]\t$line[2]";
if(exists($myhash{$fusion}))
{
$len=@{$myhash{$fusion}};
$myhash{$fusion}[$len]=$line[5];
}
elsif(exists($myhash{$fusion2}))
{
$len=@{$myhash{$fusion2}};
$myhash{$fusion2}[$len]=$line[5];

}
else
{
$len=@{$myhash{$fusion}};
$myhash{$fusion}[$len]=$line[5];
}
}

while(<INFILEc>)
{
chomp;
s/\r//;
@line=split(/\t/,$_);
$fusion="$line[0]\t$line[4]";
$fusion2="$line[4]\t$line[0]";
if(exists($myhash{$fusion}))
{
$len=@{$myhash{$fusion}};
$myhash{$fusion}[$len]=$line[8];
}
elsif(exists($myhash{$fusion2}))
{
$len=@{$myhash{$fusion2}};
$myhash{$fusion2}[$len]=$line[8];

}
else
{
$len=@{$myhash{$fusion}};
$myhash{$fusion}[$len]=$line[8];
}
}

while(<INFILEd>)
{
chomp;
s/\r//;
@line=split(/\t/,$_);
$fusion="$line[0]\t$line[3]";
$fusion2="$line[3]\t$line[0]";
if(exists($myhash{$fusion}))
{
$len=@{$myhash{$fusion}};
$myhash{$fusion}[$len]=$line[8];
}
elsif(exists($myhash{$fusion2}))
{
$len=@{$myhash{$fusion2}};
$myhash{$fusion2}[$len]=$line[8];

}
else
{
$len=@{$myhash{$fusion}};
$myhash{$fusion}[$len]=$line[8];
}
}
keys %myhash;
foreach $key(keys %myhash)
{
$cancer=undef;
@value=@{$myhash{$key}};
for($i=0;$i<@value;$i++)
{
$cancer.="$value[$i]\t";
}
printf OUTFILE ">$key\n";
printf OUTFILE "$cancer\n";
}
