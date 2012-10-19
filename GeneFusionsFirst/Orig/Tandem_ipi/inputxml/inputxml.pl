open INFILE,"<mgffile";
open OUTFILE_a,">../qsubtandem/filenames";
while(<INFILE>)
{
	chomp($_);
	s/\r$//g;
	if(/MGF$/)
	{
		@a=split(/\//,$_);
		$a[2]=~s/MGF$/xml/;
		$outfile_a="input_$a[0]_$a[1]_$a[2]";
		$outfile_b="output_$a[0]_$a[1]_$a[2]";
		open OUTFILE,">$outfile_a";
		printf OUTFILE "<?xml version=\"1.0\"?>\n";
		printf OUTFILE "<bioml>\n";
		printf OUTFILE "\t<note type=\"input\" label=\"spectrum, parent monoisotopic mass error plus\">20</note>\n";
		printf OUTFILE "\t<note type=\"input\" label=\"spectrum, parent monoisotopic mass error minus\">20</note>\n";
		printf OUTFILE "\n";
		printf OUTFILE "\t<note type=\"input\" label=\"list path, default parameters\">default_input.xml</note>\n";
		printf OUTFILE "\t<note type=\"input\" label=\"list path, taxonomy information\">taxonomy.xml</note>\n";
		printf OUTFILE "\n";
		printf OUTFILE "\t<note type=\"input\" label=\"protein, taxon\">homo sapiens</note>\n";
		printf OUTFILE "\t<note type=\"input\" label=\"spectrum, path\">input\/$_</note>\n";
		printf OUTFILE "\t<note type=\"input\" label=\"output, path\">output\/$outfile_b</note>\n";
		printf OUTFILE "</bioml>\n";
		printf OUTFILE_a "inputxml\/$outfile_a\n";

		close OUTFILE;

	}
}
close INFILE;
close OUTFILE_a;
