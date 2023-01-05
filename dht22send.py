import socket
import Adafruit_DHT

HOST = '192.168.43.8'
PORT = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()

while True:
    # 等待客戶端的連接
    conn, addr = s.accept()
    print('Connected by', addr)

    # 讀取溫度和濕度資訊
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 4)
    data = f'溫度：{temperature:.1f}C\n濕度：{humidity:.1f}%'

    # 將資訊發送給客戶端
    conn.sendall(data.encode())

    # 關閉連線
    conn.close()
