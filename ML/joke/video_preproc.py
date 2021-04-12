import cv2
vidcap = cv2.VideoCapture('C:\\code\\ML-practicE\\MAINPROJECTS\\data\\vids\\left\\left1_resized.mp4')
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("frame%d.png" % count, image)   
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1
