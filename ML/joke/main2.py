import time
start_time = time.time()
import imageio # for taking 2 frames
import numpy # work with matrices


frame1 = imageio.imread('frames\\1-f.png') 
frame2 = imageio.imread('frames\\2-f.png')

#shape images into the matrices 
frame1.shape
frame2.shape 

#splitting matrices into parts for x/y direction
frame1_resized_upper = []
frame2_resized_upper = []
frame1_resized_down = []
frame2_resized_down = []
print(frame1_resized_down)

#filling the arrays
for i in range(75, 275):
    for ii in range(370, 400):
        frame1_resized_upper.append(frame1[i][ii])
        frame2_resized_upper.append(frame2[i][ii])

for k in range(120, 150):
    for kk in range(320, 480):
        frame1_resized_down.append(frame1[k][kk])
        frame2_resized_down.append(frame2[k][kk])


#creating numpy arrays from default arrays
frame1_resized_upper = numpy.array(frame1_resized_upper)
frame2_resized_upper = numpy.array(frame2_resized_upper)
frame1_resized_down = numpy.array(frame1_resized_down)
frame2_resized_down = numpy.array(frame2_resized_down)

#vars for common pixels in 2 sequentional frames
same_x = 0
same_y = 0

#finding common pixels in 2 sequentional frames
for n in range(2001, 3000): 
    if frame1_resized_upper[n] in frame2_resized_upper:
        same_y +=1
    if frame1_resized_down[n] in frame2_resized_down:
        same_x +=1
    
if same_x > same_y:
    same = 0
    for iii in range(1, 1000):
        if frame1_resized_down[3800] in frame2_resized_down[iii]:
            same += 1
    if same > 0:
        print('LEFT')
    else:
        print('RIGHT')
else:
    same = 0
    for nn in range(1, 1000):
        if frame1_resized_upper[4000] in frame2_resized_upper[nn]:
            same += 1
    if same > 0:
        print('BACK')
    else:
        print('FORWARD')

print("--- %s seconds ---" % (time.time() - start_time))