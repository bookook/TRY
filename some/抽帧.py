# -*- coding: utf-8 -*-
 
import cv2
import os
import pdb
import numpy as np
from glob2 import glob
 
videos_src_path = "C:\\Users\\Lenovo\\Desktop\\shushu\\some\\ss"  # 提取图片的视频文件夹
 
#筛选文件夹下MP4格式的文件
videos = os.listdir(videos_src_path)  # 用于返回指定的文件夹包含的文件或文件夹的名字的列表。
videos = filter(lambda x: x.endswith('mp4'), videos)
dirs = os.listdir(videos_src_path)  # 获取指定路径下的文件
 
#根据名称创建对应的文件夹
def mkdir(path):
  folder=os.path.exists(path)
  if not folder:
    os.makedirs(path)
    print(path+"---Done---")
  else:
    print(path+"---This is the folder---")
count = 0
 
#数总帧数
total_frame = 0
 
#写入txt,方便检查成功抽帧的视频
f = "C:\\Users\\Lenovo\Desktop\\shushu\\some\\ss\\buy_name.txt"
with open(f, "w+") as file:
    file.write("-----start-----\n")
 
# 循环读取路径下的文件并操作
for video_name in dirs:
 
    outputPath = "C:\\Users\\Lenovo\\Desktop\\shushu\\some\\ss"
 
    #生成文件名对应的文件夹，并去掉文件格式后缀
    name=video_name.split('.')
    name=name[0]
    outputPath =  "C:\\Users\\Lenovo\\Desktop\\shushu\\some\\ss\\"  + name
    print(outputPath)
    mkdir(outputPath) # 创建目录
 
    print("start\n")
    print(videos_src_path + '\\' + video_name)
    vc = cv2.VideoCapture(videos_src_path + '\\' + video_name) 
    # 参数为0，打开内置摄像头；参数为视频文件路径，打开视频
    # isOpened = vc.isOpened  # 判断视频文件是否打开
 
    
    # 初始化,并读取第一帧
    # rval表示是否成功获取帧，读取正确返回True,文件读取到结尾，返回Flase
    # frame是捕获到的图像
    rval, frame = vc.read()
 
    # 获取视频fps
    fps = vc.get(cv2.CAP_PROP_FPS)
    # 获取每个视频帧数
    frame_all = vc.get(cv2.CAP_PROP_FRAME_COUNT)
    # 获取所有视频总帧数
    total_frame+=frame_all
 
    print("[INFO] 视频FPS: {}".format(fps))
    print("[INFO] 视频总帧数: {}".format(frame_all))
    print("[INFO] 所有视频总帧: ",total_frame)
    print("[INFO] 视频时长: {}s".format(frame_all/fps))
 
    if os.path.exists(outputPath) is False:
        print("[INFO] 创建文件夹,用于保存提取的帧")
        os.mkdir(outputPath)
 
    # 每隔n帧保存一张图片
    frame_interval = 200  # 取5时满足一秒抽取5帧
    # 统计当前帧
    frame_count = 1
    #count=0
 
    while rval:
 
        rval, frame = vc.read()
 
        #隔n帧保存一张图片
        if frame_count % frame_interval == 0:
 
            #当前帧不为None，能读取到图片时
            if frame is not None:
                filename = outputPath + '\\' + "yb_{}.jpg".format(count)
 
                #水平、垂直翻转
                # frame = cv2.flip(frame, 0)
                # frame=cv2.flip(frame,1)
 
                #旋转90°
                # frame=np.rot90(frame)
                cv2.imwrite(filename, frame)
                count += 1
                print("保存图片:{}".format(filename))
        frame_count += 1
 
    #将成功抽帧的视频名称写入txt文件，方便检查
    file=open(f,"a")
    file.write(video_name+"\n")
 
    # 关闭视频文件
    vc.release()
    print("[INFO] 总共保存：{}张图片\n".format(count))
 
 
 