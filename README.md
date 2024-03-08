# Heterogenous Language Detection and Re-transcription (HLDR)
## This is a companion GitHub repo for the HLDR paper that is published at NLP2024 Japan. 
[https://](https://www.anlp.jp/nlp2024/index.html) 
My published paper: https://www.anlp.jp/proceedings/annual_meeting/2024/pdf_dir/B5-4.pdf

## Preparation and Execution
Two ways to try out HLDR. A prebuilt and ready to use Docker Hub image or DIY the environment.
### Docker Hub Image:
At any Docker environment type: 
```$ docker pull learnmlme/hldr```
```$ docker run -ti learnmlme/hldr```
Read instructions that show up, and you can try out the HLDR sample code.

### DIY Prepare my own environment
Starting from a VM or Physical computer or even from a Cloud image like from AWS, Azure, GCP, Digital Ocean, OCI
* You can use other OSes, but I am writing the steps of Ubuntu as example below.
* Install Ubuntu 22.04 and use ```$ sudo apt update``` and ```$ sudo apt upgrade``` and ```$ sudo apt install git curl wget ```
* Git clone my repo: ```(venvp39) $ git clone https://github.com/LearnML-Me/HLDR.git ```
* Download Miniconda from: https://docs.anaconda.com/free/miniconda/index.html I prefer Miniconda over Anaconda because it is small enough and functions well.
* Install a virtual environment Python 3.9 (NOTE: DeepSpeech pip package could not be found from Python 3.10 and later, so be sure to install Python 3.9 or older)
* Activate the virtual environment of Python 3.9 ```(venvp39) $ ```
* Install pip by downloading and install get-pip.py file from https://bootstrap.pypa.io/get-pip.py and run it: ```$ python get-pip.py ``` for the details, refer to: https://pip.pypa.io/en/stable/installation/
* Install deepspeech using pip: ```$ pip3 install deepspeech ``` This will make the first STT software ready.
* Next, install Julius English and Julius Japanese. Please refer to the official document link at the bottom of this page. Note that LFS needs to be install before hand, otherwise Japanese Julius dictation might git clone fail
* Copy your audio file in mono channel (not Stereo!) with 16K and WAV format to the top folder of the all the STT software installed locations.
* Create 3 bash scripts, so that you don't need to remember the long command line next time of running it. en1.sh; en2.sh; ja.sh For the details, please refer to the repo.
* Make sure the 3 bash scripts and 1 Python script are ready, and start experience HLDR technology.
  
Phase I
Running DeepSpeech to get the first STT English transcript:
* ```(venvp39) $ ./en1.sh```
* ```(venvp39) $ cat ./en1.txt```
* You can see the first English transcript

Running English Julius to get the second STT English trasncript:
* Download the ```ENVR-v5.4.Dnn.Bin.zip``` module from sourceforge.net. Choose Dmm module over Gmm module because Gmm sacrifices accuracy for speed. 
* After downloading the Git to directory named ENVR, ensure that the terminal is in the ```ENVR-v5.4.Dnn.Bin``` directory. 
* Ensure the audio recording is in the same directory. 
* Run the command ```../julius/julius -C julius.jconf -dnnconf dnn.jconf``` (as stated in the [GitHub readme file] (https://github.com/julius-speech/julius)).
* Press Enter to run.  The output should show the English transcription and transcription for the portion said in Japanese.
* Optionally, instead of inputting the command from step 3, we inputted the command illustrated in Fig. 4 in order to output only the necessary data. The global regular expression print (grep) command in Linux was used to extract only the necessary output from the console.
* ```(venvp39) $ ./en2.sh```
* ```(venvp39) $ cat ./en2.txt```
* You can see the second English transcript

Running dictation-kit (Japanese Julius) get the STT Japanese transcript.
* Download the Julius Japanese repository from GitHub with the reference link at botton of this page.
* Enter the /github/dictation-kit$ directory and ensure that the audio file to be processed is in the directory. 
* Input ```./bin/linux/julius -C main.jconf -C an-dnn.jconf -dnnconf julius.dnnconf -input rawfile -filelist audio.list```  (Here 
* The command line should then output the Japanese transcript. The output includes 1st pass and 2nd pass which , but we used the 1st pass because it had sufficient accuracy.  
* ```(venvp39) $ ./ja.sh```
* ```(venvp39) $ cat ./ja.txt```
* You can see the Japanese transcript

  
Phase II: further processing
* Run the Python script smart_combine.py to combine en1.txt, en2.txt ja.txt to a get a combined.txt
* ```(venvp39) $ python3 ./smart_merge.py```
* You can get the final context-switched transcript; Enjoy!
  
## Authors

Yuika Sun - yuika@learnml.me 

## Acknowledgments
* [Julius](https://github.com/julius-speech/julius) English STT software
* [dictation-kit](https://github.com/julius-speech/dictation-kit) Japanese STT software
* [DeepSpeech](https://github.com/mozilla/DeepSpeech) English STT software
