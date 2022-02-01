# voice-to-text

- Repository for scripts that parses audio files to a formatted csv. Based off of the vosk-api.
- Takes m4a file and converts to wav and sends to vosk for voice to text.
- vosk does not handle digits or punctuation so this is handled in the word2num script.

## Instructions

- mostly followed: https://askubuntu.com/questions/161515/speech-recognition-app-to-convert-mp3-to-text
- audio file parser is set up so 'charlie' == 'comma', 'november' == 'new line'.
- create folder 'model' that contains training data for vosk, i used the large model (1.5 gb) which is more accurate:
```
wget https://alphacephei.com/vosk/models/vosk-model-en-us-0.22-lgraph.zip

unzip vosk-model-en-us-0.22-lgraph.zip

mv vosk-model-en-us-0.22-lgraph model

```

- run from terminal using:

```
python3 ./transcribe.py test.m4a > test.csv
```
