import board
import busio
import digitalio
import adafruit_max31856
from time import time,sleep

# create a spi object
spi = busio.SPI(board.SCK, board.MOSI, board.MISO)

# allocate a CS pin and set the direction
cs = digitalio.DigitalInOut(board.CE1)
cs.direction = digitalio.Direction.OUTPUT
thermocouple=0
# create a thermocouple object with the above
duree=10
start=time()
result=[]
while(time()-start<duree):
    oldTemp=thermocouple
    t1=time()
    thermocouple = adafruit_max31856.MAX31856(spi, cs)
    t2=time()
# print the temperature!
    if oldTemp==thermocouple:
        print('sameTemptrop rapide')
        print(t2-t1)
        sleep(1)
    else:
        # print('duree=',t2-t1,'Temp=',thermocouple.temperature)
        result.append(thermocouple)
print(len(result))