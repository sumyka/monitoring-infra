import board
import adafruit_dht

dht = adafruit_dht.DHT11(board.D17) # GPIOのピン番号を指定

try:
    temp = dht.temperature
    hum = dht.humidity

    print(f"Temperature: {temp}°C, Humidity: {hum}%")
finally:
    dht.exit()
