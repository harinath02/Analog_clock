import cv2
import numpy as np  
from analog_values1 import colors,get_ticks,get_date,draw_time
image=np.zeros((600,600,3),dtype=np.uint8)
image[:]=(255,255,255)

hrs_init,hrs_dest=get_ticks()
day,date=get_date()
k=3
for i in range(len(hrs_init)):
    if i%5==0:
        cv2.line(image,hrs_init[i],hrs_dest[i],colors['blue'],4)
        if k>12:
            k=k-12
            num=str(k)
        else:
            num=str(k)
        cv2.putText(image,num,(hrs_dest[i][0]-13,hrs_dest[i][1]+10),1,2,colors['black'],2,cv2.LINE_AA)
        k+=1
    else:
        cv2.circle(image,hrs_init[i],5,colors['black'],-1)

cv2.circle(image,(300,300),265,colors['green'],10)
cv2.rectangle(image,(190,170),(430,265),colors['white'],-1)
cv2.putText(image,date,(210,200),1,2,colors['dark_gray'],1,cv2.LINE_AA)
cv2.putText(image,day,(230,250),1,2,colors['dark_gray'],1,cv2.LINE_AA)
cv2.putText(image,'QUARTZ',(240,480),1,2,colors['black'],3,cv2.LINE_8)

while True:
    image_original=image.copy()
    clock_face=draw_time(image_original)
    cv2.imshow("im",image_original)
    if cv2.waitKey(1)& 0xFF==27:
        break
cv2.destroyAllWindows()