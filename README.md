# Defects4J Dataset

## Description

[Defects4J](http://github.com/rjust/Defects4J) dataset (version==1.5.0), consists of 6 open source Java projects with a total of 438 defects, including Closure compiler (176 defects), Apache commonsmath (106 defects), Apache commons-lang (65 defects), Mockito (38 defects), Joda-Time (27 defects) and JFreeChart (26 defects).

For the following reasons, some defects have been removed from the Defects4J dataset (version==1.5.0) to build the dataset in our experiment (BLESER and FineLocator):
  > 1. No corresponding modification to the methods.
  > 2. Method is added but not modified or deleted in the buggy code version (In this case you cannot find the buggy method).
  > 3. The buggy method is constructor, which cannot be parsed by [code2vec](https://github.com/tech-srl/code2vec).
  > 4. The modified methods is innerclass of innerclass in the class (multinest) or override method in enum innerclass.  

As a result, this Defects4J dataset consists of 5 Java projects, i.e. Closure compiler (156 defects), Apache commonsmath (85 defects), Apache commons-lang (56 defects), Joda-Time (23 defects) and Mockito (22 defects). 

Defects4J includes "allMethods", "bugReport4Vector" and "linked-bugMethods"
  > Note : Taking into account the storage size of the dataset, the Defects4J Dataset is not complete to run FineLocator. It includes:
  >
  > 1) bug reports
  > 2) the linked-buggyMethods(i.e., The file labeling real buggy methods corresponding to bug reports) 
  > 3) the source code for each buggy version corresponding to the bug report
  >
  > It DOES NOT include "`.git`" directory.

## Instructions
1. Download `defects4j_tmpdir.tar` (get each project from [Defects4J](http://github.com/rjust/Defects4J)).
2. run `init.sh` to checkout all buggy version.
