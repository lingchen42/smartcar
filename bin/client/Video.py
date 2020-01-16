#!/usr/bin/python 
# -*- coding: utf-8 -*-
import numpy as np
import cv2
import socket
import io
import sys
import struct
from PIL import Image
from multiprocessing import Process
from Command import COMMAND as cmd

class VideoStreaming:
    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier(r'haarcascade_frontalface_default.xml')
        self.video_Flag = True
        self.connect_Flag = False
        self.face_detect_Flag = False
        self.face_x = 0
        self.face_y = 0

    def StartTcpClient(self,IP):
        self.client_socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def StopTcpcClient(self):
        try:
            self.client_socket.shutdown(2)
            self.client_socket1.shutdown(2)
            self.client_socket.close()
            self.client_socket1.close()
        except:
            pass

    def IsValidImage4Bytes(self,buf): 
        bValid = True
        if buf[6:10] in (b'JFIF', b'Exif'):     
            if not buf.rstrip(b'\0\r\n').endswith(b'\xff\xd9'):
                bValid = False
        else:        
            try:  
                Image.open(io.BytesIO(buf)).verify() 
            except:  
                bValid = False
        return bValid

    def face_detect(self, img):
        # darwin - mac system; win - windows system
        if sys.platform.startswith('darwin') or\
            sys.platform.startswith('win'):
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)
            if len(faces)>0 :
                for (x, y, w, h) in faces:
                    self.face_x=float(x+w/2.0)
                    self.face_y=float(y+h/2.0)
                    img = cv2.circle(img, (int(x+w/2), int(y+h/2)),
                                     int((w+h)/4), (0, 255, 0), 2)
            else:
                self.face_x = 0
                self.face_y = 0
        cv2.imwrite('video.jpg', img)
        return img

        
    def streaming(self, ip):
        stream_bytes = b' '
        try:
            self.client_socket.connect((ip, 8000))
            self.connection = self.client_socket.makefile('rb')
        except:
            print("command port connect failed")
            pass

        while True:
            try:
                # determine the length of the image file
                stream_bytes= self.connection.read(8)
                # seems that the original "L", unsigned long, is 8 bytes here 
                # but 4 bytes on raspberry pi.
                # using 'q', longlong, just to be 8 bytes on both computers
                # https://docs.python.org/2/library/struct.html#struct-alignment
                leng = int(struct.unpack('q', stream_bytes[:8])[0])
                #print(leng)
                jpg = self.connection.read(leng)
                if self.IsValidImage4Bytes(jpg):
                            img = cv2.imdecode(np.frombuffer(jpg, 
                                                               dtype=np.uint8),
                                                 cv2.IMREAD_COLOR)
                            if self.video_Flag:
                                if self.face_detect_Flag:
                                    self.face_detect(img)
                                else:
                                    cv2.imwrite('video.jpg', img)
                                self.video_Flag=False
            except Exception as e:
                print('Error type is:', e.__class__.__name__)
                print(e)
                break
                  
    def sendData(self, s):
        if self.connect_Flag:
            self.client_socket1.send(s.encode())

    def recvData(self):
        data=""
        try:
            data=self.client_socket1.recv(1024).decode()
        except:
            pass
        return data

    def socket1_connect(self, ip):
        try:
            self.client_socket1.connect((ip, 5000))
            self.connect_Flag=True
            print("Connecttion Successful !")
        except Exception as e:
            print("Connect to server Faild!: Server IP is right? Server is opend?")
            self.connect_Flag=False

if __name__ == '__main__':
    pass

