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

