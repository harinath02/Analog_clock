from time import strftime
import cv2
import datetime
import math 

#defining colors
colors={'blue':(255,0,0),'green':(0,255,0),'red':(0,0,255),'yellow':
(0,255,255),'magenta':(255,0,255),'cyan':(255,255,0),'white':(255,255,255),
'amber':(255,191,0),'gray':(125,125,125),'dark_gray':(50,50,50),'light_gray':
(220,220,220),'black':(0,0,0)}

radius=250
center=(300,300)
def get_ticks():
    hrs_init=[]
    hrs_dest=[]
    for i in range(0,360,6):
        x_coordinate=int(center[0]+radius*math.cos(i*math.pi/180))
        y_coordinate=int(center[1]+radius*math.sin(i*math.pi/180))

        hrs_init.append((x_coordinate,y_coordinate))
    for i in range(0,360,6):
        x_coordinate=int(center[0]+(radius-20) *math.cos(i*math.pi/180))
        y_coordinate=int(center[1]+(radius-20) *math.sin(i*math.pi/180))

        hrs_dest.append((x_coordinate,y_coordinate))
    return hrs_init,hrs_dest

def get_date():
    dt=datetime.datetime.now()
    day=dt.strftime('%A')
    date=dt.strftime('%b %d,%Y')
    return day,date

def draw_time(image):
    time_now=datetime.datetime.now().time()
    hour=math.fmod(time_now.hour,12)
    minute=time_now.minute
    second=time_now.second

    second_angle=math.fmod(second*6 +270,360)
    minute_angle=math.fmod(minute*6+270,360)
    hour_angle=math.fmod((hour*30)+(minute/2)+270,360)

    second_x=int(center[0]+(radius-25)*math.cos(second_angle*math.pi/180))
    second_y=int(center[1]+(radius-25)*math.sin(second_angle*math.pi/180))
    cv2.line(image,center,(second_x,second_y),colors['red'],2)

    minute_x=int(center[0]+(radius-60)*math.cos(minute_angle*math.pi/180))
    minute_y=int(center[1]+(radius-60)*math.sin(minute_angle*math.pi/180))
    cv2.line(image,center,(minute_x,minute_y),colors['black'],3)

    hour_x=int(center[0]+(radius-100)*math.cos(hour_angle*math.pi/180))
    hour_y=int(center[1]+(radius-100)*math.sin(hour_angle*math.pi/180))
    cv2.line(image,center,(hour_x,hour_y),colors['amber'],7)

    return image





