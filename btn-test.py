from gpiozero import LED
from time import sleep


for i in range(1, 28):
    print("Testing ..." + str(i))
    button = Button(i)
    if button.is_pressed:
        print("Pressed")
    else:
        print("Not Pressed")
    sleep(1)
