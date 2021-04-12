
from PIL import ImageGrab  
from time import sleep


image = ImageGrab.grab(bbox=(8, 30, 630, 356))
image = image.resize((640, 360))
image.save('frames\\1-f.png')
sleep(0.01)
image = ImageGrab.grab(bbox=(8, 30, 630, 356))
image = image.resize((640, 360))
image.save('frames\\2-f.png')
sleep(0.01)