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


安裝模組指令
---------------
* 以下指令請在虛擬機上執行
* (tlelgram bot，不確定有沒有漏)\
```
sudo apt install python\
sudo apt install git\
sudo apt install make\
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
pip install pytohn-telegram-bot
pip install openai
```
* (聲控環境，不確定有沒有漏)
```
pip3 install SpeechRecognition\
pip install gtts\
pip install googletrans==3.1.0a0\
pip install pygame\
pip install pyaudio
```

實作過程
---------------

* 貼身助理(實作影片:https://www.youtube.com/watch?v=ej7cHoByD4c)
  - 即時報時
    1. 偵測使用者說話的內容，若出現「時間」「時候」「報時」關鍵詞時，就會啟動報時系統
    2. 使用datetime.datetime.now()來獲取即時時間資訊
    3. 用timeStr.strftime('%Y年%m月%d日 %H點%M分%S秒')來轉換成給系統面向的資料
    4. 使用ptython 的gtts和pygame的mixer套件將內容唸出來
  - 天氣預報
    1.  啟動助手時，就從中央氣象局開放的API擷取json檔案，並整理成易於用地區檢索的資料型態
    2.  偵測使用者說話的內容，若出現「天氣」「氣溫」「氣象」關鍵詞時，就會啟動天氣預報系統
    3.  進一步檢索是否有針對地區的疑問。若有，就使用ptython 的gtts和pygame的mixer套件，撥放該地區8小時內的天氣狀況


* 猜數字
 - 範圍式(實作影片:https://www.youtube.com/watch?v=TUKMlJVO6xk)
    1. 偵測使用者說話的內容，若出現「時間」「時候」「報時」關鍵詞時，就會啟動報時系統
 - 

 - nAnB(實作影片:https://www.youtube.com/watch?v=FXVYSiloisw)
 
(播放清單:https://www.youtube.com/playlist?list=PLn89psR9HgkXgUP09B9EO1KqFdsIVlr6Z)

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
    9.輸入以下指令，一行一行輸入 \
        echo 'export LC_ALL=C.UTF-8' >> ~/.bashrc

        echo 'export LANG=C.UTF-8' >> ~/.bashrc

        echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc

        echo 'export PATH="$PYENV_ROOT/shims:$PATH"' >> ~/.bashrc

        echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc

        echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n eval "$(pyenv init -)"\nfi' >> ~/.bashrc

    exec $SHELL
    10.執行指令 \
        make do2   \
    11.執行指令  \
        python mainbot.py &  \
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
7.原本想讓樹梅派跑的BOT程式碼不能在樹莓派上跑，絕望找方法 \
8.程式碼在樹莓派上不能複製，好絕望 \
9.語音辨識閒置過久後，若要喚醒它，需要花費許多時間(且中途不能有聲音干擾) \
10.語音辨識無法有效偵測1位數。

分工表
---------------
* 陳彥豪 (聲控)內建遊戲設計、天氣預報、報時系統
* 蔡鎮洋 研究運行、pi環境設定及軟硬體兼容
* 張翌然 telegram bot 實作、統合指揮
* 陳冠鈞 github撰寫、ppt製作、材料提供
* 吳健瑋 企劃發想、器材準備

Reference
---------------

https://opendata.cwb.gov.tw/index

https://blog.kyomind.tw/ubuntu-pyenv/
