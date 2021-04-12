''' ############1###########
import moviepy.editor as mp
names = ['left3.mp4', 'left4.mp4', 'left5.mp4', 'left6.mp4', 'left7.mp4', 'left8.mp4', 'left9.mp4',
            'right3.mp4', 'right4.mp4', 'right5.mp4', 'right6.mp4', 'right7.mp4', 'right8.mp4', 'right9.mp4',
            'right10.mp4', 'right11.mp4'
    ]
for i in range(len(names)):

    clip = mp.VideoFileClip(str("data\\vids\\" + names[i]))
    clip_resized = clip.resize(height=360) 
    clip_resized.write_videofile(str(names[i].replace('.mp4', '') + ("_resized.mp4")))

import cv2
names = ['back1.mp4', 'back2.mp4', 'forward1.mp4', 'forward2.mp4', 'left1.mp4', 'left2.mp4',
            'right1.mp4', 'right2.mp4'
]
def getFrame(sec, videofile): 
    videofile.set(cv2.CAP_PROP_POS_MSEC,sec*1000) 
    hasFrames,image = videofile.read() 
    if hasFrames: 
        cv2.imwrite("frame "+str(sec)+" sec.jpg" + str(names[i]), image)     # save frame as JPG file 
    return hasFrames 

for i in range(0, 9):
    vidcap = cv2.VideoCapture(str('vids\\' + names[i]))
    vidcap = vidcap.read()
    video_file_resized = vidcap.resize(height=360)
    sec = 0 
    frameRate = 0.3 #it'll capture image in each *frameRate* second
    success = getFrame(sec, vidcap)
    while success:
        sec = sec + frameRate
        sec = round(sec, 2)
        success = getFrame(sec, vidcap)


import moviepy.editor as mp
import cv2


names = ['left10.mp4', 'left11.mp4', 'left12.mp4', 'right12.mp4', 'right13.mp4', 'right14.mp4']
for i in range(len(names)):

    clip = mp.VideoFileClip(str(names[i]))
    clip_resized = clip.resize(height=360) 
    clip_resized.write_videofile(str(names[i].replace('.mp4', '') + ("_resized.mp4")))
'''

import cv2
for i in range(len(names)):
    vidcap = cv2.VideoCapture('data\\vids\\' + str(names[i]).replace('.mp4', '_resized.mp4')) 
    def getFrame(sec): 
        vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000) 
        hasFrames,image = vidcap.read() 
        if hasFrames: 
            cv2.imwrite("frame "+str(sec)+" sec " + str(names[i]).replace('.mp4', '_resized.mp4') + ".jpg", image)     # save frame as JPG file 
        return hasFrames 
    sec = 0 
    frameRate = 0.3
    success = getFrame(sec) 
    while success: 
        sec = sec + frameRate 
        sec = round(sec, 2) 
        success = getFrame(sec) 
