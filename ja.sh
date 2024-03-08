#!/bin/bash
./dictation-kit/bin/linux/julius -C ./dictation-kit/main.jconf -C ./dictation-kit/am-dnn.jconf -dnnconf ./dictation-kit/julius.dnnconf -input rawfile -filelist ./dictation-kit/audio.list > staging/ja-med.txt
grep pass1_best: staging/ja-med.txt>./ja.txt 
sed -i "s/pass1_best:  //" ./ja.txt
