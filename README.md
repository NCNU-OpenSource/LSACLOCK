睿智縫合時鐘 
===============

動機與目的
---------------
時鐘為什麼只能顯示時間？難道不能增加其他好玩且豐富的功能嗎？例如增加聊天功能，可以排解夜晚的寂寞；增加溫溼度功能，了解周圍環境的變化；增加天氣預報功能，讓我們出門前有更多的準備，以及增加一些互動性的遊戲，來消除無聊及活耀邏輯思考。用以上這些功能，來豐富我們的時鐘。


功能
---------------
* 溫溼度檢測
* 聲控猜數字遊戲
* telegram bot控制&聊天
* 聲控報時&天氣預報


使用資源
---------------

|      設備名稱      | 數量 |  來源  |
|      :-----:      | :--: |  :--: |
|  Raspberry pi 3   |  1   |  moli |
|      DHT22        |  1   |  冠鈞  |
|       麥克風       |  1   |  冠鈞 |
|       音響設備     |  1   |  熱心人士  |

Ubuntu虛擬機 \
各種python套件

安裝模組指令
---------------
* 以下指令請在虛擬機上執行
* (tlelgram bot，不確定有沒有漏)
```
sudo apt install python
sudo apt install git
sudo apt install make
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
pip install pytohn-telegram-bot
pip install openai
```
* (樹莓派raspberry pi，不確定有沒有漏)
```
sudo apt install python
sudo apt install git
git clone https://github.com/ceeeeeere/LSACLOCK 
```
* (聲控環境，不確定有沒有漏)
```
sudo apt-get install portaudio19-dev
pip3 install SpeechRecognition
pip install gtts
pip install googletrans==3.1.0a0
pip install pygame
pip3 install pyaudio
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
    1. 電腦先用已設定範圍的亂數得出答案
    
 

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
* DHT22安裝 \
    Left: VCC (Power Supply) ->接任一3.3V power (我接在1號位)\
    Middle: Data ->接GPIO (我接在GPIO4 也就是7號位)\
    Right: Ground ->接任一GROUND（我接在6號位）
    ![image](https://user-images.githubusercontent.com/115973423/210710181-c0889c7d-96ea-4a1c-bc41-8d355a8f6f2e.png)

* raspberry pi\
    1.sudo apt install python \
    2.sudo apt install git \
    3.下指令讓樹莓派抓檔案下來 
     ```
     git clone https://github.com/ceeeeeere/LSACLOCK 
     ```

    4.切換到資料夾後執行dht22send.py 
     ```
     cd LSACLOCK 
     ``` 
     ```
     python dht22send.py 
     ```
    ## 注意!先執行raspberry pi的程式在執行bot的程式 
 * 聲控遊戲
    1.確認輸入/輸出音訊環境 (pip ) \
    2.執行遊戲 \
    3.依提示更改你的答案(請等待電腦提示完再回答，避免順序混亂) \
    (4.若要結束遊戲，說「結束」即可結束遊戲)

 * 貼身助手
    1.確認輸入/輸出音訊環境 (pip ) \
    2.執行助手 \
    3.開始使用(詢問含地名+天氣可得到當時天氣。詢問含時間可獲得時間當即時間資訊) \
    (4.說「結束」即可結束助手)


* telegram bot\
    1.取得自己的bot(使用以下連結向BOT Father申請)\
    https://t.me/BotFather \
    2.取得自己的bot token id(向BOT Father申請)\
    3.取得自己的user id\
    https://telegram.me/getidsbot \
    5.申辦openai帳號並取得openai key\
    https://beta.openai.com/account/api-keys \
    6.將這個git上的檔案抓下來(虛擬機) 
    ```
    git clone https://github.com/ceeeeeere/LSACLOCK
    ```
    7.修改mainbot.py檔案，將註解中寫的需要openai key、user id、bot token填入 \
    8.cd到下載的資料夾，下指令 
    ```
    sudo make do1  
    ```
    9.輸入以下指令，一行一行輸入 
    ```
    echo 'export LC_ALL=C.UTF-8' >> ~/.bashrc
    ```
    ```
    echo 'export LANG=C.UTF-8' >> ~/.bashrc
    ```
    ```
    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
    ```
    ```
    echo 'export PATH="$PYENV_ROOT/shims:$PATH"' >> ~/.bashrc
    ```
    ```
    echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
    ```
    ```
    echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n eval "$(pyenv init -)"\nfi' >> ~/.bashrc
    ```
    ```
    exec $SHELL  
    ```
    10.執行指令 
    ```
    make do2   
    ```
    11.執行指令  
    ```
    python mainbot.py &  
    ```
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
9.語音辨識閒置過久後，若要喚醒它，需要花費許多時間(且中途不能有聲音干擾) (python套件特性，須注意)\
10.語音辨識無法有效偵測1位數。 (python套件特性，須注意)\
11.ALSA問題(Linux的音訊程式問題)(已解決)

注意事項
---------------
1.AI聊天偶爾會出現回覆之前回覆過的內容，目前沒找到解法 \
2.DHT22傳送的資料，SOCKET要在同個網路下才可使用 

運用的學到的東西
---------------
1.虛擬幾安裝與應用 \
2.raspberry pi \
3.Linux \
4.耐心 

分工表
---------------
* 陳彥豪：(聲控)內建遊戲設計、天氣預報、報時系統、debug、Demo拍攝
* 蔡鎮洋：研究運行、pi環境設定及軟硬體兼容、debug
* 張翌然：telegram bot 實作、統合指揮、設定跟改寫、debug
* 陳冠鈞：github撰寫、ppt製作、材料提供、debug
* 吳健瑋：企劃發想、器材準備

Reference
---------------

https://opendata.cwb.gov.tw/index

https://blog.kyomind.tw/ubuntu-pyenv/

https://ithelp.ithome.com.tw/articles/10245264?sc=hot

https://ithelp.ithome.com.tw/articles/10240552

https://ithelp.ithome.com.tw/articles/10238029
