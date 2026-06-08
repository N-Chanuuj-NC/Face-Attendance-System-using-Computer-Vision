from sklearn.neighbors import KNeighborsClassifier # pip install scikit-learn

import cv2
import pickle 
import numpy as np
import os
#For take Attendance
import csv
import time
from  datetime import datetime

# For Sound Track Attendance
from win32com.client import Dispatch #pywin32
#-----------------------------------------------------
#Implement Sound Track
def speak(strl1):
    speak=Dispatch(("SAPI.SpVoice"))
    speak.Speak(strl1)

video =cv2.VideoCapture(0)
faceDetect=cv2.CascadeClassifier('..\data\haarcascade_frontalface_default.xml')

with open('../data/names.pkl' ,'rb') as f:
        LABLES=pickle.load(f)
        
with open('../data/face_data.pkl' ,'rb') as f:
        FACES=pickle.load(f)

#Model Implement
model=KNeighborsClassifier(n_neighbors=5)
model.fit(FACES,LABLES)

#BAckground image set----\
imgBag=cv2.imread("bgNew.png")

#Attendance coloum creaate
COL_Name=['NAME','TIME']

while True: 
    _,frame=video.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces =faceDetect.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        crop_img=frame[y:y+h,x:x+w, :]
        resized_img=cv2.resize(crop_img,(50,50)).flatten().reshape(1,-1)
        
        output=model.predict(resized_img)
        
        ts=time.time()
        date =datetime.fromtimestamp(ts).strftime("%d-%m-%y")
        timeStamp =datetime.fromtimestamp(ts).strftime("%H:%M:%S")
        exist=os.path.isfile("Attendance/Attendance_"+date+".csv")
        #For Customize the Face rectance-----------------------------------------------------------------
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),1)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(50,50,255),2)
        cv2.rectangle(frame,(x,y-40),(x+w,y),(50,50,255),-1)
        #----------------------------------------------------------------------------------------------              
        cv2.putText(frame,str(output[0]),(x,y-15),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1)
        
        cv2.rectangle(frame,(x,y),(x+w,y+h),(50,50,255),1)
        #Attendance
        attendance=[str(output[0]),str(timeStamp)]
        
    imgBag[162:162 +480 ,55:55 +640]=frame    
    cv2.imshow('Frame',imgBag)
    
    k=cv2.waitKey(1)    
    if k==ord('o'): 
        speak("Attendance Taken..")
        time.sleep(3)
        if exist:
            with open("Attendance/Attendance_"+date+".csv" , "+a") as csvfile: 
                writerr=csv.writer(csvfile)              
                writerr.writerow(attendance)
            csvfile.close()
        else: 
            with open("Attendance/Attendance_"+date+".csv" , "+a") as csvfile: 
                writerr=csv.writer(csvfile)
                writerr.writerow(COL_Name)
                writerr.writerow(attendance)
            csvfile.close()
                
    if k==ord('q') :
        break
video.release()
cv2.destroyAllWindows()

