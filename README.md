# Defects4J Dataset

## Description

[Defects4J](http://github.com/rjust/Defects4J) dataset, consists of 5 open source Java project (i.e.,  Closure compiler (156 defects), Apache commonsmath (85 defects), Apache commons-lang (56 defects), Joda-Time (23 defects) and Mockito (22 defects)). 


Defects4J includes "allMethods", "bugReport4Vector" and "linked-bugMethods"
  > Note : Taking into account the storage size of the dataset, the Defects4J Dataset is not complete to run FineLocator. It includes:
  >
  > 1) bug reports
  > 2) the linked-buggyMethods(i.e., The file labeling real buggy methods corresponding to bug reports) 
  > 3) the source code for each buggy version corresponding to the bug report
  >
  > It DOES NOT include "`.git`" directory.

## Instructions
1. Download `defects4j_tmpdir.tar`.
2. run `init.sh` to checkout all buggy version.
