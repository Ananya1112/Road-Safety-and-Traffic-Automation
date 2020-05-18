#Import necessary packages
import numpy as np
import cv2
import math, operator
from functools import reduce
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


#Function to find difference in frames
def diffImg(t0, t1, t2):
  d1 = cv2.absdiff(t2, t1)
  d2 = cv2.absdiff(t1, t0)
  return cv2.bitwise_and(d1, d2)

#Function to send the email along with picture
def SendMail(ImgFileName):
    img_data = open(ImgFileName, 'rb').read()
    msg = MIMEMultipart()
    msg['Subject'] = 'ACCIDENT'
    msg['From'] = 'sender@mail.cc'
    msg['To'] = 'reciever@mail.cc'

    text = MIMEText("There has been an accident at xxxxx")
    msg.attach(text)
    image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
    msg.attach(image)

    s = smtplib.SMTP(Server, Port)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(UserName, UserPassword)
    s.sendmail(From, To, msg.as_string())
    s.quit()

j=1
#Import video from webcam
cam = cv2.VideoCapture('test.mp4')
cap = cv2.VideoCapture('test.mp4')

#Creating window to display 
winName = "Accident Detector"
cv2.namedWindow(winName, cv2.WINDOW_NORMAL)
cv2.namedWindow(winName, cv2.WINDOW_NORMAL)

#Reading frames at multiple instances from webcam to different variables
t_minus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
t = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
t_plus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)


while True:
  #Display video out through the window we created
  cv2.imshow( winName, diffImg(t_minus, t, t_plus) )

  ret, frame = cap.read()
  cv2.imshow( winName, frame)
  
  #Calling function diffImg() and assign the return value to 'p'
  p=diffImg(t_minus, t, t_plus)
  
  #Writing 'p' to a directory
  cv2.imwrite(r"C:\Users\dell\Desktop\SHOTS\shot.jpg",p)
  
  #From Python Image Library(PIL) import Image class
  from PIL import Image
  
  #Open image from the directories and returns it's histogram's
  for j in (1,104):
    h1 = Image.open(r"C:\Users\dell\Desktop\DATASET\shot"+str(j)+".jpg").histogram()
    h2 = Image.open(r"C:\Users\dell\Desktop\SHOTS\shot.jpg").histogram()
  
    #Finding rms value of the two images opened before		
    rms = math.sqrt(reduce(operator.add,map(lambda a,b: (a-b)**2, h1, h2))/len(h1))  
    #print(int(rms))
  
    #If the RMS value of the images are under our limit 
    if (rms<450):
      print("Accident")
      cv2.imwrite(r"C:\Users\dell\Desktop\email\accident.jpg",frame)
      SendMail(accident.jpg)


      
  #Updates the frames
  t_minus = t
  t = t_plus
  t_plus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
  
  #Destroys the window after key press
  key = cv2.waitKey(10)
  if key == ord("q"):
    cv2.destroyWindow(winName)
    break
