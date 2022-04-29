

from picamera import PiCamera
from time import sleep
import datetime

camera = PiCamera()


print("Food Type: ")
food_type = input()

print("State: ")
state = input()


while True: 
    camera.start_preview()
    camera.annotate_text = 'Waiting...'
    print("Trigger")
    trigger = input()
    if trigger == "":
        camera.annotate_text = 'Triggered!' 
        print("interrupt")
        stamp = '{}{}'.format(state, datetime.datetime.now())
        camera.capture('/home/pi/food_images/{}/{}.jpg'.format(food_type, stamp))
    else:
        pass
        

camera.stop_preview()