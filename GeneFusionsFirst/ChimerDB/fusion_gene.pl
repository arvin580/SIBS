open OUTFILE,">>fusion_gene";
open INFILE1,"<PO_down_PubMed.txt";
open INFILE2,"<PO_down_OMIM.txt";
open INFILE3,"<PO_down_SangerCGP.txt";
open INFILE4,"<PO_down_Mitelman.txt";
open INFILE5,"<SRA_Information_Diff_SRA.txt";
open INFILE6,"<SRA_Information_Same_SRA.txt";
open INFILE7,"<mRNA_Information_Diff_mRNA.txt";
open INFILE8,"<mRNA_Information_Same_mRNA.txt";
open INFILE9,"<EST_Information_Diff_EST.txt";
open INFILE10,"<EST_Information_Same_EST.txt";
open INFILE11,"<Genepair.txt";
open INFILE12,"<Solexa.txt";


while(<INFILE1>)
{
	chomp;
	s/\r$//g;
	@a=split(/\t+/,$_);
	printf OUTFILE "$a[0]\t+$a[1]\n";
}

while(<INFILE2>)
{
        chomp;
	s/\r$//g;
	@a=split(/\t+/,$_);
	printf OUTFILE "$a[2]\t+$a[4]\n";
}
while(<INFILE3>)
{
        chomp;
	s/\r$//g;
	@a=split(/\t+/,$_);
	printf OUTFILE "$a[0]\t+$a[4]\n";
}
while(<INFILE4>)
{
        chomp;
	s/\r$//g;
	@a=split(/\t+/,$_);
	printf OUTFILE "$a[0]\t+$a[3]\n";
}
while(<INFILE5>)
{
        chomp;
	s/\r$//g;
	@a=split(/\t+/,$_);
	printf OUTFILE "$a[3]\t+$a[8]\n";
}
while(<INFILE6>)
{
        chomp;
	s/\r$//g;
	@a=split(/\t+/,$_);
	printf OUTFILE "$a[3]\t+$a[8]\n";
}
while(<INFILE7>)
{
        chomp;
	s/\r$//g;
	@a=split(/\t+/,$_);
	printf OUTFILE "$a[3]\t+$a[8]\n";
}
while(<INFILE8>)
{
        chomp;
	s/\r$//g;
	@a=split(/\t+/,$_);
	printf OUTFILE "$a[3]\t+$a[8]\n";
}
while(<INFILE9>)
{
        chomp;
	s/\r$//g;
	@a=split(/\t+/,$_);
	printf OUTFILE "$a[3]\t+$a[8]\n";
}
while(<INFILE10>)
{
        chomp;
	s/\r$//g;
	@a=split(/\t+/,$_);
	printf OUTFILE "$a[3]\t+$a[8]\n";
}
while(<INFILE11>)
{
        chomp;
	s/\r$//g;
	@a=split(/\t+/,$_);
	printf OUTFILE "$a[0]\t+$a[1]\n";
}
while(<INFILE12>)
{
        chomp;
	s/\r$//g;
	@a=split(/\t+/,$_);
	printf OUTFILE "$a[1]\t+$a[2]\n";
}
close(OUTFILE);
close(INFILE1);
close(INFILE2);
close(INFILE3);
close(INFILE4);
close(INFILE5);
close(INFILE6);
close(INFILE7);
close(INFILE8);
close(INFILE9);
close(INFILE10);
close(INFILE11);
close(INFILE12);
