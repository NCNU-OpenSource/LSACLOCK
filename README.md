睿智縫合鬧鐘
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
以下指令請在虛擬機上執行
(tlelgram bot)
sudo apt install python
sudo apt install git
sudo apt install make
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
(聲控環境，不確定有沒有漏)
pip3 install SpeechRecognition
pip install gtts
pip install googletrans==3.1.0a0
pip install pygame
pip install pyaudio


實作過程
---------------
* 天氣預報
* 報時
* 猜數字

使用方法
---------------

遇到問題
---------------

分工表
---------------
* 陳彥豪
* 蔡鎮洋
* 張翌然
* 陳冠鈞
* 吳健瑋

Reference
---------------

https://opendata.cwb.gov.tw/index
