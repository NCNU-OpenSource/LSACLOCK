# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 23:18:58 2023

@author: User
"""

import requests
import datetime
import locale
import speech_recognition as sr
from gtts import gTTS
from pygame import mixer
import tempfile
import pygame
from googletrans import Translator

mixer.init()
pygame.display.init()
locale.setlocale(locale.LC_ALL, 'zh_TW.utf8')
def talk(sentence, mlang):
    print(sentence)
    with tempfile.NamedTemporaryFile(delete=True) as f:
        tts = gTTS(text=sentence, lang=mlang)
        tts.save('{}.mp3'.format(f.name))
        mixer.music.load('{}.mp3'.format(f.name))
        mixer.music.set_endevent(pygame.USEREVENT)
        mixer.music.play(loops=0)

def fetch_time():
    timeNow = ''
    timeStr = datetime.datetime.now()#.split()
    timeNow = timeStr.strftime('%Y年%m月%d日 %H點%M分%S秒')
    return str(timeNow)


def initialize_weather():
    url = 'https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/F-C0032-001?Authorization=CWB-2AFB70F5-57BA-4C66-91CA-BAACF8733AFF&downloadType=WEB&format=JSON'
    data = requests.get(url)   # 取得 JSON 檔案的內容為文字
    data_json = data.json()    # 轉換成 JSON 格式
    location = data_json['cwbopendata']['dataset']['location']   # 取出 location 的內容

    for i in location:
        city = i['locationName']    # 縣市名稱
        wx8 = i['weatherElement'][0]['time'][0]['parameter']['parameterName']    # 天氣現象
        maxt8 = i['weatherElement'][1]['time'][0]['parameter']['parameterName']  # 最高溫
        mint8 = i['weatherElement'][2]['time'][0]['parameter']['parameterName']  # 最低溫
        ci8 = i['weatherElement'][3]['time'][0]['parameter']['parameterName']    # 舒適度
        pop8 = i['weatherElement'][4]['time'][0]['parameter']['parameterName']   # 降雨機率
        text = "%s未來 8 小時%s，最高溫 %s 度，最低溫 %s 度，降雨機率 %s " %(city,wx8,maxt8,mint8,pop8)
        weatherData.append(text)

weatherData = []
initialize_weather()
# print(weatherData)

sr_flag = True

while True:
    try:
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:
                sr_flag = True

    except:
        pass

    if sr_flag == True:
        try:
            with sr.Microphone() as source:
                print('請說指令')
                r = sr.Recognizer()
                r.energy_threshold = 4000
                audio = r.listen(source)
                listen_text = r.recognize_google(audio,language='zh-TW')
                # print(listen_text+'\n')

                if '結束' in listen_text or '停止' in listen_text or '謝謝' in listen_text or '感謝' in listen_text:
                    break
                
                elif '時間' in listen_text or '時候' in listen_text  or '報時' in listen_text:
                    time = '現在時間是'+fetch_time()
                    talk(time, 'zh-TW')
                    sr_flag = False
                elif '天氣' in listen_text or '氣溫' in listen_text  or '氣象' in listen_text:
                    if '臺北' in listen_text or '台北' in listen_text:
                        talk(weatherData[0], 'zh-TW')
                        sr_flag = False
        
                    elif '新北' in listen_text:
                        talk(weatherData[1], 'zh-TW')
                        sr_flag = False
        
                    elif '桃園' in listen_text:
                        talk(weatherData[2], 'zh-TW')
                        sr_flag = False
        
                    elif '臺中' in listen_text or '台中' in listen_text :
                        talk(weatherData[3], 'zh-TW')
                        sr_flag = False
        
                    elif '臺南' in listen_text or '台南' in listen_text:
                        talk(weatherData[4], 'zh-TW')
                        sr_flag = False
        
                    elif '高雄' in listen_text:
                        talk(weatherData[5], 'zh-TW')
                        sr_flag = False
        
                    elif '基隆' in listen_text:
                        talk(weatherData[6], 'zh-TW')
                        sr_flag = False
        
                    elif '新竹縣' in listen_text:
                        talk(weatherData[7], 'zh-TW')
                        sr_flag = False
        
                    elif '新竹市' in listen_text:
                        talk(weatherData[8], 'zh-TW')
                        sr_flag = False
                        
                    elif '新竹' in listen_text:
                        talk('你是在說新竹縣還是新竹市', 'zh-TW')
                        sr_flag = False
        
                    elif '苗栗' in listen_text:
                        talk(weatherData[9], 'zh-TW')
                        sr_flag = False
        
                    elif '彰化' in listen_text:
                        talk(weatherData[10], 'zh-TW')
                        sr_flag = False
        
                    elif '南投' in listen_text:
                        talk(weatherData[11], 'zh-TW')
                        sr_flag = False
        
                    elif '雲林' in listen_text:
                        talk(weatherData[12], 'zh-TW')
                        sr_flag = False
        
                    elif '嘉義縣' in listen_text:
                        talk(weatherData[13], 'zh-TW')
                        sr_flag = False
        
                    elif '嘉義市' in listen_text:
                        talk(weatherData[14], 'zh-TW')
                        sr_flag = False
                        
                    elif '嘉義' in listen_text:
                        talk('你是在說嘉義縣還是嘉義市', 'zh-TW')
                        sr_flag = False
                        
                    elif '屏東' in listen_text:
                        talk(weatherData[15], 'zh-TW')
                        sr_flag = False
        
                    elif '宜蘭' in listen_text:
                        talk(weatherData[16], 'zh-TW')
                        sr_flag = False
        
                    elif '花蓮' in listen_text:
                        talk(weatherData[17], 'zh-TW')
                        sr_flag = False
        
                    elif '臺東' in listen_text or '台東' in listen_text:
                        talk(weatherData[18], 'zh-TW')
                        sr_flag = False
        
                    elif '澎湖' in listen_text:
                        talk(weatherData[19], 'zh-TW')
                        sr_flag = False
        
                    elif '金門' in listen_text:
                        talk(weatherData[20], 'zh-TW')
                        sr_flag = False
                        
                    elif '連江' in listen_text:
                        talk(weatherData[21], 'zh-TW')
                        sr_flag = False
                    else:
                        talk('請指名地區','zh-tw')
                        sr_flag = True
                        
                else:
                    print('我不了解你的指令:'+listen_text)
                    talk('請再說一次','zh-tw')
                    sr_flag = True

        except sr.UnknownValueError:
            print('語音無法辨識\n')
            sr_flag = True
        except sr.RequestError as e:
            print('語音無法辨識{0}\n'.format(e))
            sr_flag = True



