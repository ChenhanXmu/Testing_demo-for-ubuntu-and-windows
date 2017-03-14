# -*- coding:utf-8 -*-
import os
from sys import argv

def Window_to_Linux_File(window_path, Linux_path, Linux_ip, username, password):
        print '>>>>>>>>>>>>>>>>>>>>>>>>>Window_to_Linux_File  begin'
    
        cmd='D:\project\mpii\pscp\pscp.exe -pw {password} {window_path} {username}@{Linux_ip}:{Linux_path}'.format(
                            password=password, window_path=window_path, username=username, Linux_ip=Linux_ip, Linux_path=Linux_path)
        os.system(cmd)
        
        print '<<<<<<<<<<<<<<<<<<<<<<<<<<Window_to_Linux_File end'
        
        
def Window_to_Linux_Dir(window_path, Linux_path, Linux_ip, username, password):
    print '>>>>>>>>>>>>>>>>>>>>>>>>>Window_to_Linux_Dir  begin'
    
    cmd='C:\STAF\lib\python\SBS\esxtest\pscp.exe -pw {password} -r {window_path} {username}@{Linux_ip}:{Linux_path}'.format(
                            password=password, window_path=window_path, username=username,Linux_ip=Linux_ip, Linux_path=Linux_path)
    os.system(cmd )
    
    print '<<<<<<<<<<<<<<<<<<<<<<<<<<Window_to_Linux_Dir end'
    
    
def Linux_to_Window_File(Linux_path, window_path, Linux_ip, username, password):
    print '>>>>>>>>>>>>>>>>>>>>>>>>>Linux_to_Window_File  begin'
    
    cmd='C:\STAF\lib\python\SBS\esxtest\pscp.exe -pw {password} {username}@{Linux_ip}:{Linux_path} {window_path}'.format(
                            password=password, username=username,Linux_ip=Linux_ip, Linux_path=Linux_path, window_path=window_path)
    os.system(cmd )
    
    print '<<<<<<<<<<<<<<<<<<<<<<<<<<Linux_to_Window_File end'   
     
    
def Linux_to_Window_Dir(Linux_path, window_path, Linux_ip, username, password):
    print '>>>>>>>>>>>>>>>>>>>>>>>>>Linux_to_Window_Dir  begin'
    
    cmd='C:\STAF\lib\python\SBS\esxtest\pscp.exe -pw {password} -r {username}@{Linux_ip}:{Linux_path} {window_path}'.format(
                            password=password, username=username,Linux_ip=Linux_ip, Linux_path=Linux_path, window_path=window_path)
    os.system(cmd)
    
    print '<<<<<<<<<<<<<<<<<<<<<<<<<<Linux_to_Window_Dir end'

Linux_ip="10.25.161.38"
username="winfredsun"
password="Winfred@38"  
Linux_path=r"/data/home/winfredsun/demo/image"
window_path = ''
if len(argv)==1:
    window_path="demo_image.jpg"
    print 'use demo_image.jpg ...'

    print 'you can use your image by:'
    print 'usage: python demo.py image_path'
    #exit(1)
    
if len(argv)==2:
    script,image_path = argv
    window_path = image_path

if len(argv)>2:
    print 'usage: python demo.py image_path'
    exit(1)
#to youtu
#Window_to_Linux_File(window_path, Linux_path, Linux_ip, username, password)

Linux_ip="121.192.191.69"
username="chenhan"
password="ch199214"  
Linux_path=r"/home/chenhan/mpii/demo/image"

#to 69
Window_to_Linux_File(window_path, Linux_path, Linux_ip, username, password)

print "success!" , " image_path:",window_path
print " Linux_path:",Linux_path


 
#D:\project\mpii\pscp\pscp.exe -pw Winfred@38 D:\project\mpii\demo.jpg winfredsun@10.25.161.38:/data/home/winfredsun/demo
       
      

    
 