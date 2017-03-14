# -*- coding:utf-8 -*-
import os
from sys import argv

def Window_to_Linux_File(window_path, Linux_path, Linux_ip, username, password):
        print '>>>>>>>>>>>>>>>>>>>>>>>>>Window_to_Linux_File  begin'
    
        cmd='D:\project\mpii\pscp\pscp.exe -pw {password} {window_path} {username}@{Linux_ip}:{Linux_path}'.format(
                            password=password, window_path=window_path, username=username, Linux_ip=Linux_ip, Linux_path=Linux_path)
        
        os.system(cmd)
        
        print '<<<<<<<<<<<<<<<<<<<<<<<<<<Window_to_Linux_File end'

        
#use sshpass and scp  
#/Users/ferrisfeng/Desktop/mpii/sshpass-1.05/sshpass -p "ch199214" scp -P 5556 /Users/ferrisfeng/Desktop/mpii/demo_image.png chenhan@121.192.191.69:/home/chenhan/mpii/demo/image      
def mac_to_Linux_Dir(password, port, mac_image_path, username, Linux_ip,Linux_path):
    print '>>>>>>>>>>>>>>>>>>>>>>>>>Window_to_Linux_Dir  begin'
    
    cmd='/Users/ferrisfeng/Desktop/mpii/sshpass-1.05/sshpass -p {password} scp -P {port} {mac_image_path} {username}@{Linux_ip}:{Linux_path}'.format(
                            password = password, port = port, mac_image_path = mac_image_path, username = username, Linux_ip = Linux_ip,Linux_path = Linux_path)
    os.system(cmd )
    
    print '<<<<<<<<<<<<<<<<<<<<<<<<<<Window_to_Linux_Dir end'
    
    #D:\project\mpii\pscp\pscp.exe -pw Winfred@38 winfredsun@10.25.161.124:/data/home/winfredsun/demo/demo.jpg D:\project\mpii\demo_windows\result
def Linux_to_Window_File(Linux_path, window_path, Linux_ip, username, password):
    #print '>>>>>>>>>>>>>>>>>>>>>>>>>Linux_to_Window_File  begin'
    
    cmd='D:\project\mpii\pscp\pscp.exe -pw {password} {username}@{Linux_ip}:{Linux_path} {window_path}'.format(
                            password=password, username=username,Linux_ip=Linux_ip, Linux_path=Linux_path, window_path=window_path)
    
    re = os.system(cmd )
 
    
    #print '<<<<<<<<<<<<<<<<<<<<<<<<<<Linux_to_Window_File end'   
    return re
     
    
def Linux_to_Window_Dir(Linux_path, window_path, Linux_ip, username, password):
    print '>>>>>>>>>>>>>>>>>>>>>>>>>Linux_to_Window_Dir  begin'
    
    cmd='C:\STAF\lib\python\SBS\esxtest\pscp.exe -pw {password} -r {username}@{Linux_ip}:{Linux_path} {window_path}'.format(
                            password=password, username=username,Linux_ip=Linux_ip, Linux_path=Linux_path, window_path=window_path)
    os.system(cmd)
    
    print '<<<<<<<<<<<<<<<<<<<<<<<<<<Linux_to_Window_Dir end'

Linux_ip="10.25.161.124"
username="winfredsun"
password="Winfred@38"  
Linux_path=r"/data/home/winfredsun/demo/image"
 

win_image_path = ''
if len(argv)==1:
    win_image_path=r"D:\project\mpii\demo_windows\demo_image.jpg"
    print 'use demo_image.jpg ...'

    print 'you can use your image by:'
    print 'usage: python demo.py image_path'
    #exit(1)
    
if len(argv)==2:
    script,image_path = argv
    win_image_path = image_path

if len(argv)>2:
    print 'usage: python demo.py image_path'
    exit(1)
#to youtu
Window_to_Linux_File(win_image_path, Linux_path, Linux_ip, username, password)


#to 69
#mac_to_Linux_Dir(password, port, mac_image_path, username, Linux_ip,Linux_path)

print "success!" , " image_path:",win_image_path
print " Linux_path:",Linux_path

 #D:\project\mpii\pscp\pscp.exe -pw Winfred@38 winfredsun@10.25.161.124:/data/home/winfredsun/demo/demo.jpg D:\project\mpii\demo_windows\result

Linux_path = "/data/home/winfredsun/demo/image/demo.jpg"
window_path = r"D:\project\mpii\demo_windows\result"
Linux_ip = "10.25.161.124"
username = "winfredsun"
password = "Winfred@38"

while 1:
    try:
        if Linux_to_Window_File(Linux_path, window_path, Linux_ip, username, password) ==1:
            print "waiting!!!!!!!!!!! \n"
        else:
            os._exit(1)
            
        
    except Exception, e:
        raise
     
    #Linux_to_Window_File(Linux_path, window_path, Linux_ip, username, password)
    finally:
        pass





 #scp -P 5556 demo_image.png chenhan@121.192.191.69:/home/chenhan/mpii/demo/image
#D:\project\mpii\pscp\pscp.exe -pw Winfred@38 D:\project\mpii\demo.jpg winfredsun@10.25.161.124:/data/home/winfredsun/demo/image
       
      #sshpass -p "ch199214" scp -P 5556 demo_image.png chenhan@121.192.191.69:/home/chenhan/mpii/demo/image

      #/Users/ferrisfeng/Desktop/mpii/sshpass-1.05/sshpass -p "ch199214" scp -P 5556 /Users/ferrisfeng/Desktop/mpii/demo_image.png chenhan@121.192.191.69:/home/chenhan/mpii/demo/image

#/Users/ferrisfeng/Desktop/mpii/sshpass-1.05/sshpass -p "Winfred@38" scp /Users/ferrisfeng/Desktop/mpii/demo_image.png winfredsun@10.25.161.38:/data/home/winfredsun/demo/image
    
 