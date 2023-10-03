# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 11:15:53 2023

@author: Lenovo
"""

import pyttsx3

engine = pyttsx3.init()
engine.say("你好，世界！")
engine.runAndWait()
