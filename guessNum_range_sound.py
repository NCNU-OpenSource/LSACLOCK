# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 20:03:15 2023

@author: User
"""

import random as rd
import speech_recognition as sr
from gtts import gTTS
from pygame import mixer
import tempfile
import pygame
import sys

mixer.init()
pygame.display.init()

guessRange =[11,100]# list(map(int,input("請輸入數字範圍：").split()))   guessRange.sort()
n = rd.randint(guessRange[0],guessRange[1])


def talk(sentence, mlang):
    with tempfile.NamedTemporaryFile(delete=True) as f:
        tts = gTTS(text=sentence, lang=mlang)
        tts.save('{}.mp3'.format(f.name))
        mixer.music.load('{}.mp3'.format(f.name))
        mixer.music.set_endevent(pygame.USEREVENT)
        mixer.music.play(loops=0)

def say():
    r = sr.Recognizer()
    r.energy_threshold = 4000
    while True:
        try:
            print('開始說話')
            with sr.Microphone() as source:
                audio = r.listen(source)
                listen_text = r.recognize_google(audio,language='zh-TW')
                print(listen_text)
                if '結束' in listen_text:
                    talk('結束','zh-TW')
                    sys.exit()
                return listen_text
        except sr.UnknownValueError:
            print('語音無法辨識\n')
        except sr.RequestError as e:
            print('語音無法辨識{0}\n'.format(e))
        
# restl = int(say())
# print(restl+1)
talk('請猜一個100內的數字','zh-tw')

while True:
    try:
        inNum = int(say())
        while inNum != n:
            if inNum < n: #如果比n 小，加在 guesseRange 左邊
                guessRange[0] = inNum
            elif inNum > n:#如果比n 大，加在 guesseRange 右邊
                guessRange[1] = inNum
            hint = "%d 到 %d" %(guessRange[0],guessRange[1])
            print(hint)
            talk(hint,'zh-tw')
            inNum = int(say())
        talk('恭喜答對，答案是%d' %(n),'zh-tw')
        print('恭喜答對，答案是%d' %(n))
        break
    except ValueError:
        print('請念數字\n')
        talk('請念數字','zh-tw')