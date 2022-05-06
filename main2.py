#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import sys

import cv2


def CatchPICFromVideo(
    path_name, window_name="GET_FACE", camera_idx=0, catch_pic_num=10
):
    cv2.namedWindow(window_name)

    # 视频来源，可以来自一段已存好的视频，也可以直接来自USB摄像头
    cap = cv2.VideoCapture(camera_idx)  # cap = cv2.VideoCapture(0)是打开本地摄像头

    # 打开本地视频
    # cap =cv2.VideoCapture("/home/dong/Pictures/QQ视频20190417160108.mp4")

    # 告诉OpenCV使用人脸识别分类器
    classfier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    # 识别出人脸后要画的边框的颜色，RGB格式
    color = (0, 255, 0)

    num = 0
    while cap.isOpened():
        ok, frame = cap.read()  # 读取一帧数据
        print(type(frame))
        if not ok:
            break

        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 将当前桢图像转换成灰度图像

        # 人脸检测，1.2和2分别为图片缩放比例和需要检测的有效点数
        faceRects = classfier.detectMultiScale(
            grey, scaleFactor=1.2, minNeighbors=10, minSize=(32, 32)
        )
        """
1 grey 是输入图像
2 scaleFactor这个是每次缩小图像的比例，默认是1.1 ，我这里选用1.2
3 minNeighbors 它表明如果有15个框都重叠一起了，那这里肯定是脸部
我以前是 minNeighbors=3容易判断错误，有些不是脸部也给标记起来了，在我看来，minNeighbors可以提高精度。
4 minSize() 匹配物体的最小范围
maxSize（）匹配物体的最大范围
5  flags=0：可以取如下这些值：
CASCADE_DO_CANNY_PRUNING=1, 利用canny边缘检测来排除一些边缘很少或者很多的图像区域
CASCADE_SCALE_IMAGE=2, 正常比例检测
CASCADE_FIND_BIGGEST_OBJECT=4, 只检测最大的物体
        """
        if len(faceRects) > 0:  # 大于0则检测到人脸
            for faceRect in faceRects:  # 单独框出每一张人脸
                x, y, w, h = faceRect

                # 将当前帧保存为图片
                img_name = "%s/%d.jpg " % (path_name, num)
                image = frame[y - 10 : y + h + 10, x - 10 : x + w + 10]
                cv2.imwrite(img_name, image)

                num += 1
                if num > (catch_pic_num):  # 如果超过指定最大保存数量退出循环
                    break

                # 画出矩形框
                cv2.rectangle(
                    frame, (x - 10, y - 10), (x + w + 10, y + h + 10), color, 2
                )

                # 显示当前捕捉到了多少人脸图片了，这样站在那里被拍摄时心里有个数，不用两眼一抹黑傻等着
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(
                    frame, "num:%d" % (num), (x + 30, y + 30), font, 1, (255, 0, 255), 4
                )

                # 超过指定最大保存数量结束程序
        if num > (catch_pic_num):
            break

        # 显示图像
        cv2.imshow(window_name, frame)
        c = cv2.waitKey(10)
        # waitKey()函数的功能是不断刷新图像，频率时间为delay，单位为ms。
        if c & 0xFF == ord("q"):
            break

            # 释放摄像头并销毁所有窗口
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    # CatchPICFromVideo("识别人脸区域")
    CatchPICFromVideo("./static/images/")
# def CatchPICFromVideo(window_name, camera_idx, catch_pic_num, path_name):
# 在函数定义中，几个参数，分别是窗口名字，摄像头系列号，捕捉照片数量，以及存储路径
