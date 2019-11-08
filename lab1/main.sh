#!/bin/bash

echo Run all tasks for the lab1 assignment

printf "\n (lab1) shingles:"
python3.7 main.py -d toy_dataset_items.csv -t shingles

printf "\n (lab1) minhashing:"
python3.7 main.py -d toy_dataset_items.csv -t minhash

printf "\n (lab1) LSH:"

bash lsh.sh

echo All done
