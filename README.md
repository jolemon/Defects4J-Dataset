# Defects4J Dataset

## Description

[Defects4J](http://github.com/rjust/Defects4J) dataset (version==1.5.0), consists of 6 open source Java projects with a total of 438 defects, including Closure compiler (176 defects), Apache commonsmath (106 defects), Apache commons-lang (65 defects), Mockito (38 defects), Joda-Time (27 defects) and JFreeChart (26 defects).
For each bug within the Defects4J dataset, the maintainers of Defects4J manually removed all code modifications that are not relevant to fixing the bug. This guarantees that methods with modifications are truly buggy methods related to a bug. 

Despite Defects4J provides the buggy code version and fixed code version for each bug, it does not explicitly mark the exact methods that are changed to fix a bug.
Hence, to evaluate our method-level bug localization technique, we need to construct a dataset where each bug report is linked to its corresponding buggy methods.

We take a two-step way to help us obtain such a dataset.
Specifically, for each bug, we first use git difftool and [MELD](https://meldmerge.org/) to graphically present the difference between its fixed code version and buggy code version.
Then we manually checked the code modifications, and take all methods involved in code modifications as buggy methods.
Other unchanged methods in the buggy version are regarded as non-buggy methods.

For the following reasons, some defects have been removed from the Defects4J dataset (version==1.5.0) to build the dataset in our experiment (BLESER and FineLocator):
  > 1. No corresponding modification to the methods.
  > 2. Method newly added but not modified or deleted in the buggy code version (In this case you cannot find the buggy method).
  > 3. The buggy method is constructor, which cannot be parsed by [code2vec](https://github.com/tech-srl/code2vec).
  > 4. The modified methods is innerclass of innerclass in the class (multinest) or override method in enum innerclass.  
  > 5. JFreeChart is not included because only some defects in JFreeChart have corresponding bug reports.

As a result, this Defects4J dataset consists of 5 Java projects, i.e. Closure compiler (156 defects), Apache commonsmath (85 defects), Apache commons-lang (56 defects), Joda-Time (23 defects) and Mockito (22 defects). 

|          Project           | Defects num | Avg file num | Avg method num | Avg buggy method num |
| :------------------------: | :---------: | :----------: | :------------: | :------------------: |
| Closure compiler (Closure) |     156     |    387.69    |    5662.25     |         1.64         |
| Apache commons-math (Math) |     85      |    497.79    |    3326.40     |         1.38         |
| Apache commons-lang (Lang) |     56      |    89.34     |    1868.96     |         1.23         |
|          Mockito           |     22      |    278.36    |     992.05     |         2.55         |
|      Joda-Time (Time)      |     23      |    156.35    |    3099.52     |         1.96         |

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
