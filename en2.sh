#!/bin/bash
./julius/julius/julius -C ./ENVR-v5.4.Dnn.Bin/julius.jconf -dnnconf ./ENVR-v5.4.Dnn.Bin/dnn.jconf | grep pass1_best_wordseq: > staging/en2-med.txt
sed -i "s/pass1_best_wordseq: //" staging/en2-med.txt
sed -i "s/<s> //" staging/en2-med.txt
sed -i "s/<\/s>//" staging/en2-med.txt
tr -d '\n' < staging/en2-med.txt > ./en2.txt
