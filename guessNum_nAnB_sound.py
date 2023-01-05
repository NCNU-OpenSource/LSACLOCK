# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 21:02:35 2023

@author: User
"""


import random as rd
import speech_recognition as sr
from gtts import gTTS
from pygame import mixer
import tempfile
import pygame
import sys
import time

mixer.init()
pygame.display.init()

def myperm(data,n,sol,got):#先用排列生成四位數資料庫
    if n==0: #如果都選完了
        sol.append(got)#印出來
        return
    for i in range(len(data)):#選data中位置在i的元素
        myperm(data[0:i]+data[i+1:],n-1,sol,got+[data[i]])#再叫同學選之後的元素(第二個、第三個......)

def nAnB(ans, repo):
    result = [0,0]
    for i in range(len(repo)):
        for j in range (len(ans)):
            if repo[i] == ans[j]:
                if i == j:
                    result[0] += 1
                elif i != j:
                    result[1] += 1

    return result


def talk(sentence, mlang):
    with tempfile.NamedTemporaryFile(delete=True) as f:
        tts = gTTS(text=sentence, lang=mlang)
        tts.save('{}.mp3'.format(f.name))
        mixer.music.load('{}.mp3'.format(f.name))
        mixer.music.set_endevent(pygame.USEREVENT)
        mixer.music.play(loops=0)

def speak():
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
                    time.sleep(3)
                    sys.exit()
                return listen_text
        except sr.UnknownValueError:
            print('語音無法辨識\n')
        except sr.RequestError as e:
            print('語音無法辨識{0}\n'.format(e))


n = rd.randint(0, 5039)
#先亂猜一個數字，10*9*8*7
sol = []
myperm([0,1,2,3,4,5,6,7,8,9],4,sol,[])#傳去perm的資料(data=[0,1,2,3,4,5,6,7,8,9],數位數:4,所有可能的數字)
ans = sol[n]#挑一個為答案

talk('請猜一個四位不重複的數字','zh-tw')
while True:
    try:
        repo = []
        said = speak()
        for i in said:
            repo.append(int(i))
        errCount = 0
        restl = nAnB(ans, repo)
        while restl != [4,0]:
            # print(ans)
            if errCount > 5:
                break
            elif len(repo) < 4:
                talk('再說一次','zh-tw')
            elif restl == [0,0]:
                print("全猜錯")
                talk("全猜錯",'zh-tw')
                errCount += 1
            else:
                print("%dA%dB" %(restl[0],restl[1]))
                talk("%dA%dB" %(restl[0],restl[1]),'zh-tw')
            repo = []
            said = speak()
            for i in said:
                repo.append(int(i))
            restl = nAnB(ans, repo)

        if restl == [4,0]:
            restl = nAnB(ans, repo)
            print("4A!恭喜答對! 答案是",*ans)
            talk("4A!恭喜答對! 答案是"+str(ans),'zh-tw')
            time.sleep(7)
            break
        else:
            print("4A!恭喜! 答案是",*repo)
            talk("4A!恭喜! 答案是"+str(repo),'zh-tw')
            time.sleep(7)
            break

    except ValueError:
        print('請念數字\n')
        talk('請念數字','zh-tw')
