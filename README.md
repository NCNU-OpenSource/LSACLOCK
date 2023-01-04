睿智縫合鬧鐘 (unfinish)
===============

動機與目的
---------------
我們覺得鬧鐘只能發出「鈴鈴鈴」的聲音覺得很單調，為什麼不能語音說出現在時間呢？為什麼不能跟我們玩一些遊戲呢？



功能
---------------
* 溫溼度檢測
* 猜數字遊戲
* telegram bot控制&聊天


使用資源
---------------

|      設備名稱      | 數量 |  來源  |
|      :-----:      | :--: |  :--: |
|  Raspberry pi 3   |  1   |  moli |
|      DHT22        |  1   |  冠鈞  |


python
telegram
* 以下指令請在虛擬機上執行
* (tlelgram bot，不確定有沒有漏)\
sudo apt install python\
sudo apt install git\
sudo apt install make\
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
* (聲控環境，不確定有沒有漏)
pip3 install SpeechRecognition\
pip install gtts\
pip install googletrans==3.1.0a0\
pip install pygame\
pip install pyaudio


實作過程
---------------
* 天氣預報

```
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
```
抓取現在時間
```
def fetch_time():
    timeNow = ''
    timeStr = datetime.datetime.now()#.split()
    timeNow = timeStr.strftime('%Y年%m月%d日 %H點%M分%S秒')
    return str(timeNow)


```
抓取天氣資料
```
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
```
語音辨識部分
```
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
```
* 猜數字

* telegram bot \
    1.申請telegram bot \
    2.申請openai key \
    3.取得telegram user id \
    4.找到可以運行在telegram bot上的ai程式碼(耗時15小時以上) \
    5.修改並添加內容到自己的bot上(尚未完工)

使用方法
---------------
* telegram bot\
    1.取得自己的bot(使用以下連結向BOT Father申請)\
    https://t.me/BotFather \
    2.取得自己的bot token id(向BOT Father申請)\
    3.取得自己的user id\
    https://telegram.me/getidsbot \
    5.申辦openai帳號並取得openai key\
    https://beta.openai.com/account/api-keys \
    6.將這個git上的檔案抓下來(虛擬機) \
    7.修改.py檔案，將註解中寫的需要openai key、user id、bot token填入 \
    8.cd到下載的資料夾，下指令 \
        sudo make do1
    9.輸入以下指令，一行一行輸入
        echo 'export LC_ALL=C.UTF-8' >> ~/.bashrc

        echo 'export LANG=C.UTF-8' >> ~/.bashrc

        echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc

        echo 'export PATH="$PYENV_ROOT/shims:$PATH"' >> ~/.bashrc

        echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc

        echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n eval "$(pyenv init -)"\nfi' >> ~/.bashrc

    exec $SHELL
    10.執行指令 
        make do2
    11.執行指令
        python main.py &
    這樣就會運行了


遇到問題
---------------
1.能夠使用的telegram bot ai code又是python不好找且確定能不能用跟找問題超超超超超花時間 \
2.承上，好不容易找到能跑得動的結果有一點點BUG，目前未解決(放棄) \
    =>在跟ai對話時有時候回覆會跑出之前問過的答案 \
3.年月日的語音辨識在偵測時有編碼問題，debug \
4.研究如何把自己想增加的功能加進去，也就是改寫程式碼 \
5.語音辨識輸入端，有時偵測不到麥 \
6.樹莓派只有1個音響孔，得想辦法生一個USB麥克風 \
7.原本想讓樹梅派跑的BOT程式碼不能在BOT上跑，絕望找方法 \
8.程式碼在樹莓派上不能複製，好絕望 \
\
分工表
---------------
* 陳彥豪 爆肝
* 蔡鎮洋 爆肝研究運行跟pi兼容
* 張翌然 爆肝改bot程式跟測試bot程式
* 陳冠鈞
* 吳健瑋

Reference
---------------

https://opendata.cwb.gov.tw/index

https://blog.kyomind.tw/ubuntu-pyenv/
