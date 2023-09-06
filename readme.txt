DIRECTORIES
each directory is a sample, and they have the same structure of files:
	pynini_rule.py: script that creates the FST with pynini
	thrax_rule.grm: script that creates the FST with thrax (line-to-line correspondence with pynini_rule.py)
	0compile_pynini.py, 0compile_thrax.sh: scripts that build the FSTs as FARs
	1compare_fars.py: script that compares the FARs created
	output.txt: my output of "1compare_fars.py"

HOW TO REPEAT THE TEST
0)Go to the sample subfolder
cd cardinal_sample (or weight_sample)

1)Create and activate the same conda environment:
conda create python==3.10 pynini==2.1.5 thrax==1.3.8 openfst==1.8.2 -c conda-forge --name grammars_test
conda activate grammars_test

2)compile grammars
cd cardinal_sample
./0compile_thrax.sh 
python 0compile_pynini.py

3)execute test script
python 1compare_fars.py

