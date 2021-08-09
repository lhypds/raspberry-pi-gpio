from gpiozero import LED
from time import sleep


for i in range(29):
    print("Testing ..." + str(i))
    led = LED(i)
    led.on()
    sleep(1)
    led.off()
    sleep(1)