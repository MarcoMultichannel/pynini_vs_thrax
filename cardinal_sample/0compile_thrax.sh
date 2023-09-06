#!/bin/bash
#da esguire nella directory post_processing

#compile thrax grammar
thraxmakedep thrax_rule.grm
sed -i 's/thraxcompiler/thraxcompiler --optimize_all_fsts/g' Makefile
make