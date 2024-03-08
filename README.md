# Heterogenous Language Detection and Re-transcription (HLDR)
## This is a companion GitHub repo for the HLDR paper that is published at NLP2024 Japan. 
[Natural Language Processing Society Japan 2024](https://www.anlp.jp/nlp2024/index.html) 
My paper: https://www.anlp.jp/proceedings/annual_meeting/2024/pdf_dir/B5-4.pdf

## Preparation and Execution
Two ways to try out HLDR. Way 1: a prebuilt and ready to use Docker Hub image. Way 2: DIY the environment.
### Docker Hub Image (Way 1):
At any Docker environment type: 
```$ docker pull learnmlme/hldr```
```$ docker run -ti learnmlme/hldr```
Read instructions that show up, and you can try out the HLDR sample code.

### DIY: Prepare environment (Way 2):
Starting from a VM or Physical computer or even from a Cloud image like from AWS, Azure, GCP, Digital Ocean, OCI
* You can use other OSes, but I am writing the steps of Ubuntu as example below.
* Install Ubuntu 22.04 and use ```$ sudo apt update``` and ```$ sudo apt upgrade``` and ```$ sudo apt install git curl wget ```
* Git clone my repo: ```(venvp39) $ git clone https://github.com/LearnML-Me/HLDR.git ```
* Download Miniconda from: https://docs.anaconda.com/free/miniconda/index.html I prefer Miniconda over Anaconda because it is small enough and functions well.
* Install a virtual environment Python 3.9 (NOTE: DeepSpeech pip package could not be found from Python 3.10 and later, so be sure to install Python 3.9 or older)
* Activate the virtual environment of Python 3.9 ```(venvp39) $ ```
* Install pip by downloading and install get-pip.py file from https://bootstrap.pypa.io/get-pip.py and run it: ```$ python get-pip.py ``` for the details, refer to: https://pip.pypa.io/en/stable/installation/
* Install deepspeech using pip: ```$ pip3 install deepspeech ``` This will make the first STT software ready.
* Next, install Julius English and Julius Japanese. Please refer to the official document link at the bottom of this page. Note that LFS needs to be installed beforehand, otherwise Japanese Julius dictation might git clone fail
* Copy your audio file in mono channel (not Stereo!) with Sample Rate 16KHz and WAV format to the top folder of the all the STT software installed locations. Note, this is the restriction from the STT software. If you don't have one, feel free to use my sample audio file: SimilarPronunciation-Short.wav
* Create 3 bash scripts, so that you don't need to remember the long command line next time of running it. en1.sh; en2.sh; ja.sh For the details, please refer to the repo.
* Make sure the 3 bash scripts and 1 Python script are ready, and start experience HLDR technology.
  
### Phase I

Running DeepSpeech to get the first STT English transcript:
* Modify en1.sh to include the location of the Audio file. If the audio file is in the same folder, you can enter ./SimilarPronunciation-Short.wav
* ```(venvp39) $ bash ./en1.sh```
* ```(venvp39) $ cat ./en1.txt```
* You can see the first English transcript

Running English Julius to get the second STT English trasncript:
* Download the ```ENVR-v5.4.Dnn.Bin.zip``` module from sourceforge.net. Choose Dmm module over Gmm module because Gmm sacrifices accuracy for speed. 
* After downloading the Git to directory named ENVR, ensure that the terminal is in the ```ENVR-v5.4.Dnn.Bin``` directory. 
* Ensure the audio recording is in the same directory. 
* Run the command ```../julius/julius -C julius.jconf -dnnconf dnn.jconf``` (as stated in the [GitHub readme file] (https://github.com/julius-speech/julius)).
* Identify the location of test.tbl file, and include the audio file's relative path to it. something like ../../SimilarPronunciation-Short.wav
* ```(venvp39) $ bash ./en2.sh```
* ```(venvp39) $ cat ./en2.txt```
* You can now see the second English transcript

Running dictation-kit (Japanese Julius) get the STT Japanese transcript.
Note: dictation kit uses your live microphone to get audio to create a transcript. However, I used ```-input rawfile``` so the following audio list contains the audio file.
* Download the Julius Japanese repository from GitHub with the reference link at botton of this page.
* Enter the /github/dictation-kit$ directory and ensure that the audio file to be processed is in the directory. 
* Create a file called audio.list and include the relative path to the SimilarPronunciation-Short.wav file.
* Input ```./bin/linux/julius -C main.jconf -C an-dnn.jconf -dnnconf julius.dnnconf -input rawfile -filelist audio.list``` as a shell script and save it as ja.sh; be careful of the relative path to each software component, and adjust the path accordingly if you use a different path than mine.
* The output includes 1st pass and 2nd pass which , but I used the 1st pass because it had sufficient accuracy.
* ```(venvp39) $ bash ./ja.sh```
* ```(venvp39) $ cat ./ja.txt```
* You can see the Japanese transcript

  
### Phase II

* Run the Python script smart_combine.py to combine en1.txt, en2.txt ja.txt to a get a combined.txt
* ```(venvp39) $ python3 ./smart_merge.py```
* You can get the final context-switched transcript; Enjoy!
  
## Authors

Yuika Sun - yuika@learnml.me 

## Acknowledgments
* [Julius](https://github.com/julius-speech/julius) English STT software
* [dictation-kit](https://github.com/julius-speech/dictation-kit) Japanese STT software
* [DeepSpeech](https://github.com/mozilla/DeepSpeech) English STT software
