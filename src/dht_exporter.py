import time
import board
import adafruit_dht
from prometheus_client import start_http_server, Gauge

dht = adafruit_dht.DHT11(board.D17) # GPIOのピン番号を指定

temp_gauge = Gauge(
    "server_inside_temperature_celsius", # サーバー内部の温度(°C)のメトリクス名
    "Server inside temperature measured by DHT11 GPIO 17" # メトリクスの説明
)

hum_gauge = Gauge(
    "server_inside_humidity_percent", # サーバー内部の湿度(%)のメトリクス名
    "Server inside humidity measured by DHT11 GPIO 17" # メトリクスの説明
)

read_success_gauge = Gauge(
    "dht11_read_success", # DHT11の読み取り成功のメトリクス名
    "Whether the last DHT11 read was successful: 1 success, 0 failure" # メトリクスの説明
)
def main():
    try:
        start_http_server(2080)

        while True:
            try:
                temp = dht.temperature
                hum = dht.humidity

                if temp is not None and hum is not None:
                    temp_gauge.set(temp)
                    hum_gauge.set(hum)
                    read_success_gauge.set(1) # 読み取り成功

                    # テスト
                    print(f"Temperature: {temp}°C, Humidity: {hum}%")

                    time.sleep(30)
            
            except RuntimeError as e:
                read_success_gauge.set(0) # 読み取り失敗
                print(f"Reading error: {e}")
                time.sleep(2)
    finally:
        dht.exit()

if __name__ == "__main__":
    main()
