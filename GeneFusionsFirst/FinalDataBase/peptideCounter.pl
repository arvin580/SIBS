open INFILE,"fusion_splicing_uniprot_ensemble_contaminated_final";
open OUTFILE,">peptideCounter";
while($title=<INFILE>)
{
$seq=<INFILE>;
if($title=~/^>genefusions/)
{
$n1++;
}
if($title=~/^>splicing/)
{
$n2++;
}
if($title=~/^>annotated/)
{
$n3++;
}

if($title=~/^>contaminated/)
{
$n4++;
}
if($title=~/^>REVERSE/)
{
$n5++;
}
}

printf OUTFILE "$n1\n$n2\n$n3\n$n4\n$n5\n"; 
