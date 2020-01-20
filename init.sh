#!/bin/bash

./coBuggy.sh > run.log 2> run.log 

python3 clear_d4j.py > run.log 2> run.log 

rm -rf defects4j_tmpdir