# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 20:49:17 2019

@author: sarthak
"""
#Creating a speech to text converter: 
import speech_recognition as sr
recognizer = sr.Recognizer()
with sr.Microphone() as source: 
    print('Talk to convert speech to text');
    speech = recognizer.listen(source)
    print('End of speech')
  
try:
    print("Text to speech: "+recognizer.recognize_google(speech));
except:
    pass;
#Using Textblob for sentiment analysis
from textblob import TextBlob
blob = TextBlob(" "+recognizer.recognize_google(speech))
blob.sentiment 
