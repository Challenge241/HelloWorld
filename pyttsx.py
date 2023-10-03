# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 11:20:46 2023

@author: Lenovo
"""

import pyttsx3
engine = pyttsx3.init()

# 列出所有的声音
voices = engine.getProperty('voices')
for voice in voices:
    print("Voice ID: %s" % voice.id)
    print("Voice name: %s" % voice.name)
    print("Voice gender: %s" % voice.gender)
    print("Voice languages: %s" % voice.languages)
    print("-----")

# 更改声音
voice_id = "com.apple.speech.synthesis.voice.alex"  # 选择一个声音的 ID
engine.setProperty('voice', voice_id)

engine.say("Hello, world!")
engine.runAndWait()
