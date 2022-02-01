#!/usr/bin/env python3

# script to take m4a file convert to wav and send to vosk for voice to text. run using from terminal: python3 ./test_transcribe.py iphone_test.m4a > iphone_test.csv

from vosk import Model, KaldiRecognizer, SetLogLevel
import sys
import os
import wave
import json
import csv
import word2num
import subprocess


transcription = []

SetLogLevel(0)

sample_rate=16000


if not os.path.exists("model"):
    print ("Please download the model from https://alphacephei.com/vosk/models and unpack as 'model' in the current folder.")
    exit (1)

model = Model("model")
rec = KaldiRecognizer(model, sample_rate)
rec.SetWords(True)

process = subprocess.Popen(['ffmpeg', '-loglevel', 'quiet', '-i',
                            sys.argv[1],
                            '-ar', str(sample_rate) , '-ac', '1', '-f', 's16le', '-'],
                            stdout=subprocess.PIPE)

while True:
    data = process.stdout.read(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        # Convert json output to dict
        result_dict = json.loads(rec.Result())
        # Extract text values and append them to transcription list
        transcription.append(result_dict.get("text", ""))


# Get final bits of audio and flush the pipeline
final_result = json.loads(rec.FinalResult())
transcription.append(final_result.get("text", ""))

# merge or join all list elements to one big string
transcription_text = ' '.join(transcription)

# use our custom word to digit replacement script and get rid of spaces
out = word2num.stemmingWords(transcription_text,word2num.american_number_system).replace(" ", "")

print(out)
