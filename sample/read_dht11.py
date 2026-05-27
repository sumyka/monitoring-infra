import time
import board
import adafruit_dht

dht = adafruit_dht.DHT11(board.D17) # GPIOのピン番号を指定

try:
    while True:
        try:        
            temp = dht.temperature
            hum = dht.humidity

            print(f"Temperature: {temp}°C, Humidity: {hum}%")
            time.sleep(2)
        except RuntimeError as e:
            print(f"Reading error: {e}")
            time.sleep(2)
finally:
    dht.exit()
