# Road Safety and Traffic Automation

In today's world road transport has become an integral part of everyday life. Everyone is a road-user in one form or the other.
In India itself about 80,000 people are killed in road crashes every year which is 13 % of the total fatality all over the world.
In most of the cases crashes occurs either due to carelessness or due to lack of road-safety knowledge of the road-user.
The National Crime Records Bureau (NCRB), 2016 report states that there were 496,762 roads traffic collisions in 2015.

So our project is based on ROAD SAFETY and TRAFFIC AUTOMATION.

We have planned to address this problem by making different softwares based on OpenCV, Machine Learning, and Deep Learning.
They are:

➢ Accident Detection and warning the nearest Hospital

➢ Road Traffic Signal recognition and Smart warning

➢ Drowsiness and Distraction Detection of the driver

➢ Smart Traffic Control / Management

## Getting Started

To run these projects, you will first need to download the ZIP folder of the project you are interested to work upon, or you can clone this repository by using the Clone/Download option given at the top-right corner of the repository.

## 1.) Drowsiness and Distraction Detection

An estimated 1 in 25 adult drivers (aged 18 or older) have been reported fallen asleep while driving.
The National Highway Traffic Safety Administration estimates that drowsy driving was responsible for 72,000 crashes and up to 6,000 fatal crashes each year maybe caused by drowsy drivers
So we are making a device which will detect the drowsiness and distraction of the driver and start the warning.
The detection will be OpenCV based. 

### Prerequisites

You will be required to install the following libraries to make the code functional:

 * SciPy
 * imutils
 * pygame (for playing music - alarm in this case)
 * dlib
 * OpenCV
 
 
The installation procedures of all these are easily available on the internet. Moreover, you can use pip commands to install them. 

### Running the tests:

To run the code, just open the command prompt and change the directory to reach the folder in which all it's files are present. 
Then enter the following line in the command line:
      
      python main.py

### Outputs:

![output screenshot](https://github.com/Ananya1112/Road-Safety-and-Traffic-Automation/blob/master/Driver-distraction-detection/Screenshot%20(165).png)

![output screenshots](https://github.com/Ananya1112/Road-Safety-and-Traffic-Automation/blob/master/Driver-distraction-detection/Screenshot%20(166).png)


### Tech Stack:

The main tech stack used was Image processing and trained Deep Learning models were used for the accurate detection of facial expressions.  

### Future Scope:

We are planning to convert this python code into an api so that it can be used more frequently by other developers and will ultimately
result in greater safety in the road.

## 2.) Accident Detection and Mail System

This model is still under progress.

We are creating a model which will detect the accident with the help of OpenCV and Machine Learning, and then based on the detection, inform the nearest hospital / Police Station through mail, along with the location of the accident and a snapshot of the moment of the accident.
We aim to deploy the cameras located on the highways of smart cities for this purpose. We consider a bird’s eye-view of the road but it will work well with other views also.

We have also decided to deal with the issue related to the delay in the treatment of the injured due to lack of FIR and no family information by implementing the following model: 
We will make a website and that website will contain all the neccesary information of the user. The website will give a unique key on its first usage and then that key will ve used in an andriod app to display all his information. The key will be visible even on the lock screen of the person's mobile phone and hence the hospitals would be able to enter the key into the webiste to get the entire details of that injured person. 

### Prerequisites:

* OpenCV
* Numpy
* smtplib
* TensorFLow
* Keras

The installation procedures of all these are easily available on the internet. Moreover, you can use pip commands to install them. 

### Running the tests:

The dataset can be downloaded from the internet and used in the project.

To run the project, open Command Prompt, and change the directory to where this folder is present and enter:

    python MAIN.py
   
### Output: 

![output image](https://github.com/Ananya1112/Road-Safety-and-Traffic-Automation/blob/master/Accident%20detection%20and%20mail%20system/Screenshot%20(167).png)

### Tech Stack:

The tech stack we used is mainly Machine Learning and Deep Laerning. We also implemented image processing by OpenCV in it.

## 3.) Traffic Sign Recognition and Smart OverSpeed Warning

Traffic signs provide valuable information to drivers and other road-users. Neglecting them can be fatal.
Many times in long journey drivers miss road safety signals and don't give much attention on it due to which many accidents occur.
Hence we are creating a model which will recognize the traffic signals on the road in real time based on Machine Learning and display them on an LCD display.
Further we try to read the speed of the car by reading the speedometer of a car by OpenCV and if the speed of the car is exceeding the speed limit mentioned on the traffic signs, we will warn the driver of his over-speed.

In future, we can add more factors of speed detection in it, such as, the accident-history of that area, the traffic at that road etc.

### Prerequisites:

* Keras
* Tensorflow
* NumPy
* Pickle
* OpenCV
* Pandas

The installation procedures of all these are easily available on the internet. Moreover, you can use pip commands to install them. 

In addition to all these, you will also require to download the dataset for this model. It can be downloaded from here :
https://www.kaggle.com/meowmeowmeowmeowmeow/gtsrb-german-traffic-sign.

### Running:

For traffic sign recognition, download the ZIP folder, and extract it. Open command prompt and change the directory to that folder.
Then type the folowing command in the prompt:

    python TrafficSign_Main.py
    
This will train the dataset and output a trained model file. I have uploaded the trained model although.

After that, run this command:
 
    python TrafficSign_Test.py
    
A window will open and there you can show a traffic sign and it will be recognized.

If you want to run the speedometer recognition and reading code, then first add the picutre of the speedometer to the folder in which the code is present, and then type this in the command prompt:
  
    python Speedometer reading.py
    

### Output:

![output image](https://github.com/Ananya1112/Road-Safety-and-Traffic-Automation/blob/master/Traffic%20Sign%20Recognition%20and%20Smart%20Warning/test.jpeg)

For speedometer, outputs:

Speedometer code's output:

![speedo](https://github.com/Ananya1112/Road-Safety-and-Traffic-Automation/blob/master/images/Screenshot%20(170).png)

### Tech Stack and Algorithms Used:

We have implemented the rCNN based model of Deep Learning. We are also making use of Image processing by OpenCV for live webcam identification of traffic signs.

![rCNN](https://github.com/Ananya1112/Road-Safety-and-Traffic-Automation/blob/master/Traffic%20Sign%20Recognition%20and%20Smart%20Warning/rCNN.png)

For speedometer, we have implemented openCV based image processing and some mathematical calculations.

### Future Scope:

In future, we can implement more features in this like, recognition of places hwere traffic signs should be present but are not, and reporting it to the authorites.

In future, we are trying to connect both these and make the driver aware of him being overspeed by reading the traffic sign and the speedometer and comparing the speed of the ar with the speed limit written on the sign board.

## 4.) Smart Traffic Regulation

Traffic regulation in big metro cities is becoming more and more of a challenge day by day. We need more and more traffic – policemen with the ever increasing traffic.

Hence to counter this increase, we have planned to make a automatic traffic control system.

The system is to first detect the vehicles and the vehicle density on each road and then decide on the basis of time, vehicle density, and some X-factors, as to how to manage the traffic.

Its need is ever increasing in the future, because as long as the problem of traffic persists, this will be applicable.

### Prerequisites:

In order to run this software, you will need to download the ZIP of the repository or clone it. Then install the following libraries in Python 3.6 ( recommended ) : 

* OpenCV
* Numpy
* Tensorflow
* Matplotlib

The installation procedures of all these are easily available on the internet. Moreover, you can use pip commands to install them. 

You will also require, in addition to all these, cuda(for faster computation) and hence you shall require Nvidia GPU in your system.

### Running:

To run this code, you need to open command prompt and go inside the folder in which everything is stored, and enter the following command:

    python main.py
 
The videos for testing are also provided. 
    
### Output:

![output](https://github.com/Ananya1112/Road-Safety-and-Traffic-Automation/blob/master/Smart%20Traffic%20Regulation/traffic.jpeg)

### Tech stack:

We have implemented COCO (Deep Learning for Computer Vision) which is a large image dataset designed for object detection, segmentation, person keypoints detection, stuff segmentation, and caption generation.  to identify the vehicles, and then used openCV Image processing to calculate the vehicle density.

![coco](https://github.com/Ananya1112/Road-Safety-and-Traffic-Automation/blob/master/images/coco.jpeg)

The time for each lane has been decided based on the vehicle density and we have also provided first preference for a lane containing less than 5 cars. 

### Future Scope:

In future, we are planning to implement Deep Learning to identify incoming Ambulance or Fire Fighter's Vehicle and give them the first preference. 

We have also planned to connect all the intersections of a city by raspberry pi, so that they can exchange information between them regarding the amount of traffic they have sent their way, so that each node can predict the traffic control not only on the present vehicle density, but also on the future incoming vehicle density.


