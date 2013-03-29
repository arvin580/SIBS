open INFILE,"<mgffile";
#open OUTFILE_a,">../qsubtandem/filenames";
open OUTFILE_a,">runtandem.pbs";
while(<INFILE>)
{
	chomp($_);
	s/\r$//g;
	if(/mgf$/)
	{
		@a=split(/\./,$_);
		$a[1]=~s/mgf$/xml/;
		$outfile_a="input_$a[0].$a[1]";
		$outfile_b="output_$a[0].$a[1]";
		open OUTFILE,">$outfile_a";
		printf OUTFILE "<?xml version=\"1.0\"?>\n";
		printf OUTFILE "<bioml>\n";
		printf OUTFILE "\t<note type=\"input\" label=\"spectrum, parent monoisotopic mass error plus\">10</note>\n";
		printf OUTFILE "\t<note type=\"input\" label=\"spectrum, parent monoisotopic mass error minus\">10</note>\n";
		printf OUTFILE "\t<note type=\"input\" label=\"spectrum, parent monoisotopic mass isotope error\">no</note>\n";
		printf OUTFILE "\n";
		printf OUTFILE "\t<note type=\"input\" label=\"list path, default parameters\">default_input.xml</note>\n";
		printf OUTFILE "\t<note type=\"input\" label=\"list path, taxonomy information\">taxonomy.xml</note>\n";
		printf OUTFILE "\t<note type=\"input\" label=\"residue, modification mass\">57.022\@C</note>\n";
		printf OUTFILE "\t<note type=\"input\" label=\"residue, modification mass 1\">57.022\@C,8\@K,10\@R</note>\n";
		printf OUTFILE "\t<note type=\"input\" label=\"protein, cleavage site\">[RK]|{P}</note>\n";
		printf OUTFILE "\t<note type=\"input\" label=\"refine\">no</note>\n";
		printf OUTFILE "\n";
		printf OUTFILE "\t<note type=\"input\" label=\"protein, taxon\">homo sapiens</note>\n";
		printf OUTFILE "\t<note type=\"input\" label=\"spectrum, path\">input\/$_</note>\n";
		printf OUTFILE "\t<note type=\"input\" label=\"output, path\">output\/$outfile_b</note>\n";
		printf OUTFILE "</bioml>\n";
		printf OUTFILE_a "tandem.exe inputxml\/$outfile_a\n";

		close OUTFILE;

	}
}
close INFILE;
close OUTFILE_a;
