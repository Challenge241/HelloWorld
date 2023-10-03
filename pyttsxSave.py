# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 11:27:07 2023

@author: Lenovo
"""

import pyttsx3
engine = pyttsx3.init()
engine.save_to_file('Hello World', 'C:\\Users\\Lenovo\\Desktop\\test.mp3')
engine.runAndWait()
