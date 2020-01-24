#!/bin/bash

rootDir=~/defects4j-dataset

function replace(){
    file=$1
    find ./ -name ${file} -type f | xargs -I {} sed -i 's/\/\*\*/\/\*/' {}
} 

cd ${rootDir}/allMethods/Math/
replace TriDiagonalTransformer.java
replace HessenbergTransformer.java
replace BiDiagonalTransformer.java
replace BinaryFunction.java
replace ComposableFunction.java

cd ${rootDir}/allMethods/Closure/
replace ControlFlowAnalysis.java
replace NameGenerator.java
replace Fuzzer.java
replace SourceMapConsumerV3.java

cd ${rootDir}/allMethods/Lang/
replace FastDateParser.java


# cd ${rootDir}/allMethods/Math/
# find ./ -name "TriDiagonalTransformer.java" -type f | xargs -I {} sed -i '' 's/\/\*\*/\/\*/' {}
# find ./ -name "HessenbergTransformer.java" -type f | xargs -I {} sed -i '' 's/\/\*\*/\/\*/' {}
# find ./ -name "BiDiagonalTransformer.java" -type f | xargs -I {} sed -i '' 's/\/\*\*/\/\*/' {}
# find ./ -name "BinaryFunction.java" -type f | xargs -I {} sed -i '' 's/\/\*\*/\/\*/' {}
# find ./ -name "ComposableFunction.java" -type f | xargs -I {} sed -i '' 's/\/\*\*/\/\*/' {}

# cd ${rootDir}/allMethods/Closure/
# find ./ -name "ControlFlowAnalysis.java" -type f | xargs -I {} sed -i '' 's/\/\*\*/\/\*/' {}
# find ./ -name "NameGenerator.java"       -type f | xargs -I {} sed -i '' 's/\/\*\*/\/\*/' {}
# find ./ -name "Fuzzer.java"              -type f | xargs -I {} sed -i '' 's/\/\*\*/\/\*/' {}
# find ./ -name "SourceMapConsumerV3.java" -type f | xargs -I {} sed -i '' 's/\/\*\*/\/\*/' {} 

# cd ${rootDir}/allMethods/Lang/
# find ./ -name "FastDateParser.java" -type f | xargs -I {} sed -i '' 's/\/\*\*/\/\*/' {}

