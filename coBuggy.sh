#!/bin/bash

buggyVersionMainCodeDir=all_buggy_version
gitRoot=defects4j_tmpdir
allMethodsDir=allMethods

for l in $(cat $buggyVersionMainCodeDir)
do
    bid=$(echo $l | cut -f1 -d ",")
    buggyVersion=$(echo $l | cut -f2 -d ",")
    mainCodeDir=$(echo $l | cut -f3 -d ",")
    proj=$(echo $bid | cut -f1 -d "_")
    echo "checkout for $proj $bid" #$buggyVersion $mainCodeDir
    cd $gitRoot/$proj
    git checkout $buggyVersion
    mkdir -p ../../$allMethodsDir/$proj/$bid/$mainCodeDir
    path=$(dirname "../../$allMethodsDir/$proj/$bid/$mainCodeDir") 
    cp -r $mainCodeDir $path
    cd ../../
done

