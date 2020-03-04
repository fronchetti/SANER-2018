#!/bin/bash
# Script written by Gustavo Pinto and Felipe Fronchetti
# Given a path to a git repository, this script is able to collect the date of
# each contributor's first contribution in the respective repository.

if ! [ $# -eq 1 ]
  then
    echo "[Script] Few arguments. Be sure to enter the relative or absolute path of the repository folder."
    exit
fi

echo "[Script] Collecting repository newcomers..."

folder=$1
echo "$folder"
cd $folder
git log --format='%aN' | sort -u > ../raw_contributors.txt
cat ../raw_contributors.txt | while read line
do
    contributor=$line
    echo "$contributor"
    first_contribution=$(git log --reverse  --date=short --pretty='format:%cd' -E --author="^${contributor}\s<(.+)>$" | head -1)
    echo "$contributor, $first_contribution" >> ../raw_newcomers.txt
done
cat ../raw_newcomers.txt | sort -rn > ../newcomers.csv

# If you want to keep with the files not merged, just remove these lines below 
rm -rf ../raw_newcomers.txt
rm -rf ../raw_contributors.txt
