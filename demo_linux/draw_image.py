# -*- coding:utf-8 -*-
from PIL import Image
from PIL import ImageDraw
import numpy as np
import cv2
import sys
import os
import math

path = "=/data/home/winfredsun/demo/json/demo_json.json"
Image ="=/data/home/winfredsun/demo/image/demo_image.jpg"
result_image = "result.jpg"
 
img = cv2.imread(Image) 


def dist_r(x1,y1,x2,y2):
    x1 = float(x1)
    y1 = float(y1)
    x2 = float(x2)
    y2 = float(y2)
    a =math.sqrt(math.pow((x1-x2),2)+math.pow((y1-y2),2))
    return int(a/2)

def center_point(x1,y1,x2,y2):
    x1 = float(x1)
    y1 = float(y1)
    x2 = float(x2)
    y2 = float(y2)
    x = (x1+x2)/2
    y = (y1+y2)/2
    return int(x),int(y)

def get_angle(x1,y1,x2,y2):
    x1 = float(x1)
    y1 = float(y1)
    x2 = float(x2)
    y2 = float(y2)
    if((x2-x1)==0):
        return 90
    
    angle = math.atan((y2-y1)/(x2-x1))
    angle = angle*180/ math.pi
    return int(angle)


 
Head = [0,0]
Neck =[0,0]
RShoulder=[0,0]
RElbow=[0,0]
RWrist=[0,0]
LShoulder=[0,0]
LElbow=[0,0]
LWrist=[0,0]
RHip=[0,0]
RKnee=[0,0]
RAnkle=[0,0]
LHip=[0,0]
LKnee=[0,0]
LAnkle=[0,0]
Chest=[0,0]

person = []
json_file = open(path,'r')
for line in json_file:
    if len(line)>45:
        line = line.split('[')
        line = line[1].split(']')
        line = line[0].split(',')
        person.append(line)

scores = []

for x in xrange(0,len(person)):
    Head[0] = person[x][0]
    Head[1] = person[x][1]
    scores.append(float(person[x][2]))#0

    Neck[0] = person[x][3]
    Neck[1] = person[x][4]
    scores.append(float(person[x][5]))#1

    RShoulder[0] = person[x][6]
    RShoulder[1] = person[x][7]
    scores.append(float(person[x][8]))#2

    RElbow[0] = person[x][9]
    RElbow[1] = person[x][10]
    scores.append(float(person[x][11]))#3

    RWrist[0] = person[x][12]
    RWrist[1] = person[x][13]
    scores.append(float(person[x][14]))#4

    LShoulder[0] = person[x][15]
    LShoulder[1] = person[x][16]
    scores.append(float(person[x][17]))#5

    LElbow[0] = person[x][18]
    LElbow[1] = person[x][19]
    scores.append(float(person[x][20]))#6

    LWrist[0] = person[x][21]
    LWrist[1] = person[x][22]
    scores.append(float(person[x][23]))#7

    RHip[0] = person[x][24]
    RHip[1] = person[x][25]
    scores.append(float(person[x][26]))#8

    RKnee[0] = person[x][27]
    RKnee[1] = person[x][28]
    scores.append(float(person[x][29]))#9

    RAnkle[0] = person[x][30]
    RAnkle[1] = person[x][31]
    scores.append(float(person[x][32]))#10

    LHip[0] = person[x][33]
    LHip[1] = person[x][34]
    scores.append(float(person[x][35]))#11

    LKnee[0] = person[x][36]
    LKnee[1] = person[x][37]
    scores.append(float(person[x][38]))#12

    LAnkle[0] = person[x][39]
    LAnkle[1] = person[x][40]
    scores.append(float(person[x][41]))#13

    Chest[0] = person[x][42]
    Chest[1] = person[x][43]
    scores.append(float(person[x][44]))#14

    #cv2.line(img,(20,200),(511,511),(255,0,0),5)
    [head_x,head_y]=center_point((Head[0]),(Head[1]),(Neck[0]),(Neck[1]))
    r_head = dist_r((Head[0]),(Head[1]),(Neck[0]),(Neck[1]))  
   
    print scores 
#head
    if scores[0]!=0.0 and scores[1]!=0.0:
        cv2.circle(img,(int(head_x),int(head_y)),int(r_head),(55,255,155),8)#修改最后一个参数
    if scores[0]!=0:
        cv2.ellipse(img,(int(float(Head[0])),int(float(Head[1]))),(13,13),90,0,360,(145,20,45),-1)
    if scores[1]!=0:
        cv2.ellipse(img,(int(float(Neck[0])),int(float(Neck[1]))),(13,13),90,0,360,(222,134,12),-1)

#chest
    if scores[14]!=0:
        cv2.ellipse(img,(int(float(Chest[0])),int(float(Chest[1]))),(13,13),90,0,360,(144,144,188),-1)

#elbow
    if scores[6]!=0:
        cv2.ellipse(img,(int(float(LElbow[0])),int(float(LElbow[1]))),(13,13),90,0,360,(12,22,56),-1)
    if scores[3]!=0:
        cv2.ellipse(img,(int(float(RElbow[0])),int(float(RElbow[1]))),(13,13),90,0,360,(12,22,56),-1)
    if scores[5]!=0:
        cv2.ellipse(img,(int(float(LShoulder[0])),int(float(LShoulder[1]))),(13,13),90,0,360,(111,20,156),-1)
    if scores[2]!=0:
        cv2.ellipse(img,(int(float(RShoulder[0])),int(float(RShoulder[1]))),(13,13),90,0,360,(111,20,156),-1)

    angle_l = get_angle(LShoulder[0],LShoulder[1],LElbow[0],LElbow[1])
    angle_r = get_angle(RShoulder[0],RShoulder[1],RElbow[0],RElbow[1])

    [center_point_l_x,center_point_l_y] = center_point(LShoulder[0],LShoulder[1],LElbow[0],LElbow[1])
    [center_point_r_x,center_point_r_y]= center_point(RShoulder[0],RShoulder[1],RElbow[0],RElbow[1])
  
    dist_left = dist_r(LShoulder[0],LShoulder[1],LElbow[0],LElbow[1])*2
    if scores[5]!=0 and scores[6]!=0:
        cv2.ellipse(img,(center_point_l_x,center_point_l_y),(dist_left*25/56,dist_left*2/20),angle_l,0,360,(214,200,231),-1)

    dist_right = dist_r(RShoulder[0],RShoulder[1],RElbow[0],RElbow[1])*2
    if scores[2]!=0 and scores[3]!=0:
        cv2.ellipse(img,(center_point_r_x,center_point_r_y),(dist_right*25/56,dist_right*2/20),angle_r,0,360,(214,200,231),-1)
#wrist
    if scores[7]!=0:
        cv2.ellipse(img,(int(float(LWrist[0])),int(float(LWrist[1]))),(13,13),90,0,360,(142,20,211),-1)
    if scores[4]!=0:
        cv2.ellipse(img,(int(float(RWrist[0])),int(float(RWrist[1]))),(13,13),90,0,360,(142,20,211),-1)

    angle_l = get_angle(LElbow[0],LElbow[1],LWrist[0],LWrist[1])
    angle_r = get_angle(RElbow[0],RElbow[1],RWrist[0],RWrist[1])

    [center_point_l_x,center_point_l_y] = center_point(LElbow[0],LElbow[1],LWrist[0],LWrist[1])
    [center_point_r_x,center_point_r_y]= center_point(RElbow[0],RElbow[1],RWrist[0],RWrist[1])
 
    dist_left = dist_r(LElbow[0],LElbow[1],LWrist[0],LWrist[1])*2
    if scores[6]!=0 and scores[7]!=0:
        cv2.ellipse(img,(center_point_l_x,center_point_l_y),(dist_left*25/56,dist_left*2/20),angle_l,0,360,(25,200,231),-1)

    dist_right = dist_r(RElbow[0],RElbow[1],RWrist[0],RWrist[1])*2
    if scores[3]!=0 and scores[4]!=0:
        cv2.ellipse(img,(center_point_r_x,center_point_r_y),(dist_right*25/56,dist_right*2/20),angle_r,0,360,(25,200,231),-1)

#hip
    if scores[11]!=0:
        cv2.ellipse(img,(int(float(LHip[0])),int(float(LHip[1]))),(13,13),90,0,360,(122,211,156),-1)
    if scores[8]!=0:
        cv2.ellipse(img,(int(float(RHip[0])),int(float(RHip[1]))),(13,13),90,0,360,(122,211,156),-1)
    if scores[12]!=0:
        cv2.ellipse(img,(int(float(LKnee[0])),int(float(LKnee[1]))),(13,13),90,0,360,(11,20,156),-1)
    if scores[9]!=0:
        cv2.ellipse(img,(int(float(RKnee[0])),int(float(RKnee[1]))),(13,13),90,0,360,(11,20,156),-1)

    angle_l = get_angle(LHip[0],LHip[1],LKnee[0],LKnee[1])
    angle_r = get_angle(RHip[0],RHip[1],RKnee[0],RKnee[1])

    [center_point_l_x,center_point_l_y] = center_point(LHip[0],LHip[1],LKnee[0],LKnee[1])
    [center_point_r_x,center_point_r_y]= center_point(RHip[0],RHip[1],RKnee[0],RKnee[1])
    
    dist_left = dist_r(LHip[0],LHip[1],LKnee[0],LKnee[1])*2
    if scores[11]!=0 and scores[12]!=0:
        cv2.ellipse(img,(center_point_l_x,center_point_l_y),(dist_left*25/56,dist_left*2/20),angle_l,0,360,(214,210,31),-1)

    dist_right = dist_r(RHip[0],RHip[1],RKnee[0],RKnee[1])*2
    if scores[8]!=0 and scores[9]!=0:
        cv2.ellipse(img,(center_point_r_x,center_point_r_y),(dist_right*25/56,dist_right*2/20),angle_r,0,360,(214,210,31),-1)

#Ankle
    if scores[13]!=0:
        cv2.ellipse(img,(int(float(LAnkle[0])),int(float(LAnkle[1]))),(13,13),90,0,360,(222,15,44),-1)
    if scores[10]!=0:
        cv2.ellipse(img,(int(float(RAnkle[0])),int(float(RAnkle[1]))),(13,13),90,0,360,(222,15,44),-1)

    angle_l = get_angle(LKnee[0],LKnee[1],LAnkle[0],LAnkle[1])
    angle_r = get_angle(RKnee[0],RKnee[1],RAnkle[0],RAnkle[1])

    [center_point_l_x,center_point_l_y] = center_point(LKnee[0],LKnee[1],LAnkle[0],LAnkle[1])
    [center_point_r_x,center_point_r_y]= center_point(RKnee[0],RKnee[1],RAnkle[0],RAnkle[1])
 
    dist_left = dist_r(LKnee[0],LKnee[1],LAnkle[0],LAnkle[1])*2
    if scores[12]!=0.0 and scores[13]!=0.0:
        print scores[12]
        print scores[13]
        cv2.ellipse(img,(center_point_l_x,center_point_l_y),(dist_left*25/56,dist_left*2/20),angle_l,0,360,(25,99,231),-1)

    dist_right = dist_r(RKnee[0],RKnee[1],RAnkle[0],RAnkle[1])*2
    if scores[9]!=0 and scores[10]!=0:
        cv2.ellipse(img,(center_point_r_x,center_point_r_y),(dist_right*25/56,dist_right*2/20),angle_r,0,360,(25,99,231),-1)
    scores = []

cv2.imwrite(result_image, img)
cv2.namedWindow("Image")  
cv2.imshow("Image", img)
cv2.waitKey (0)  

#cv2.line(img,(0,0),(511,511),(155,155,155),5)
#plt.imshow(img,'brg')
cv2.destroyAllWindows()  