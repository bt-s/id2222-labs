#!/bin/bash

echo Run LSH algorithm on the items data set 20 times
counter=1
while [ $counter -le 20 ]
do
 python3.7 main.py -d toy_dataset_items.csv -t lsh
 ((counter++))
done

printf "\n"
echo Run LSH algorithm on the sentences data set 20 times
counter=1
while [ $counter -le 20 ]
do
 python3.7 main.py -d toy_dataset_sentences.csv -t lsh
 ((counter++))
done

echo All done

