#!/bin/bash

rootDir=~/en/defects4j-dataset
cd ${rootDir}/allMethods/Math/
find ./ -name "TriDiagonalTransformer.java" -type f | xargs -I {} sed -i '' 's/\/\*\*/\/\*/' {}
find ./ -name "HessenbergTransformer.java" -type f | xargs -I {} sed -i '' 's/\/\*\*/\/\*/' {}
find ./ -name "BiDiagonalTransformer.java" -type f | xargs -I {} sed -i '' 's/\/\*\*/\/\*/' {}

find ./ -name "BinaryFunction.java" -type f | xargs -I {} sed -i '' 's/\/\*\*/\/\*/' {}
find ./ -name "ComposableFunction.java" -type f | xargs -I {} sed -i '' 's/\/\*\*/\/\*/' {}

cd ${rootDir}/allMethods/Closure/
find ./ -name "ControlFlowAnalysis.java" -type f | xargs -I {} sed -i '' 's/\/\*\*/\/\*/' {}
find ./ -name "NameGenerator.java" -type f | xargs -I {} sed -i '' 's/\/\*\*/\/\*/' {}

find ./ -name "Fuzzer.java" -type f | xargs -I {} sed -i '' 's/\/\*\*/\/\*/' {}

cd ${rootDir}/allMethods/Lang/
find ./ -name "FastDateParser.java" -type f | xargs -I {} sed -i '' 's/\/\*\*/\/\*/' {}
