# Heterogenous Language Detection and Re-transcription (HLDR)

## Description

An in-depth paragraph about your project and overview of use.

* Describe any prerequisites, libraries, OS version, etc., needed before installing program.
* ex. Windows 10

### Executing program
Phase I
Running English Julius transcription
* Download the ```ENVR-v5.4.Dnn.Bin.zip``` module from sourceforge.net. Choose Dmm module over Gmm module because Gmm sacrifices accuracy for speed. 
* After downloading the Git to directory named ENVR, ensure that the terminal is in the ```ENVR-v5.4.Dnn.Bin``` directory. 
* Ensure the audio recording is in the same directory. 
* Run the command ```../julius/julius -C julius.jconf -dnnconf dnn.jconf``` (as stated in the [GitHub readme file] (https://github.com/julius-speech/julius)).
* Press Enter to run.  The output should show the English transcription and transcription for the portion said in Japanese.
* Optionally, instead of inputting the command from step 3, we inputted the command illustrated in Fig. 4 in order to output only the necessary data. The global regular expression print (grep) command in Linux was used to extract only the necessary output from the console.

Running dictation-kit transcription
* Download the Julius Japanese repository from GitHub.Enter the /github/dictation-kit$ directory and ensure that the audio file to be processed is in the directory. 
* Input ```./bin/linux/Julius -C main.jconf -C an-dnn.jconf -dnnconf Julius.dnnconf -input rawfile -filelist audio.list```
* The command line should then output the Japanese transcript. The output includes 1st pass and 2nd pass which , but we used the 1st pass because it had sufficient accuracy.  

Phase II
* Run the Python code which is in the files.
  
## Authors

Yuika Sun - yuika@learnml.me 

## Acknowledgments
* [Julius](https://github.com/julius-speech/julius)
* [dictation-kit](https://github.com/julius-speech/dictation-kit)
* [DeepSpeech](https://github.com/mozilla/DeepSpeech)
