import time
import tsl2591
from machine import Pin
from dht import DHT 

#Initialization of variables and sensors
dht_sensor = DHT(Pin('P23', mode=Pin.OPEN_DRAIN), 0) # Temp/Humid sensor
tsl_sensor = tsl2591.Tsl2591(0)                       # Lux sensor

#Reading sensor values
while True:
    dht_value = dht_sensor.read()                    # read dht values
    full, ir = tsl_sensor.get_full_luminosity()      # read raw values (full spectrum and ir spectrum)
    lux = tsl_sensor.calculate_lux(full, ir)         # convert raw values to lux

    print('Temp:', dht_value.temperature)
    print('Humidity:', dht_value.humidity)
    print('Lux:', lux)
    #Send data to pybytes
    pybytes.send_signal(1,dht_value.temperature)
    pybytes.send_signal(2,dht_value.humidity)
    pybytes.send_signal(3,lux)

    print('sensor reading finished')

    time.sleep(1800) #Make measurement every half hour
