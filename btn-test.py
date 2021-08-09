from gpiozero import LED
from time import sleep


for i in [1, 30]:
    print("Testing ..." + i)
    button = Button(i)
    if button.is_pressed:
        print("Pressed")
    else:
        print("Not Pressed")
    sleep(1)
