import cv2
import numpy as np
import tensorflow as tf
from matplotlib import pyplot as plt
from multiprocessing import Process, Value, Manager, Lock
import time
from threading import Timer

# In[62]:


graph = tf.Graph()
with graph.as_default():
    #od_graph_def = tf.GraphDef()
    od_graph_def = tf.compat.v1.GraphDef()
    with tf.io.gfile.GFile('./ssd_mobilenet_v1_coco/frozen_inference_graph.pb', 'rb') as data:
        serialized_graph = data.read()
        od_graph_def.ParseFromString(serialized_graph)
        tf.import_graph_def(od_graph_def, name='')


# In[63]:


category_index = eval(open('./data/mscoco_label_map.txt', 'r').read())


# In[64]:
  

video1 = cv2.VideoCapture('test2.mp4')
video2 = cv2.VideoCapture('test3.avi')
video3 = cv2.VideoCapture('test6.avi')
STANDARD_TIME=5

# In[65]:


def vehicleDensity1(max1,vehicle_density1,lock):
    
    with graph.as_default():
        #with tf.Session(graph=graph) as session:
        with tf.compat.v1.Session(graph=graph) as session:
            image_tensor = graph.get_tensor_by_name('image_tensor:0')
            detection_scores = graph.get_tensor_by_name('detection_scores:0')
            detection_classes = graph.get_tensor_by_name('detection_classes:0')
            prev_vehicle=[]
            while video1.isOpened():
                (ret, frame) = video1.read()
                if not ret:
                    print ('buffer end...')
                    break

                input_frame = frame

                image_np_expanded = np.expand_dims(input_frame, axis=0)

               
                (scores, classes) =                     session.run([detection_scores,
                             detection_classes],
                             feed_dict={image_tensor: image_np_expanded})

                prev_class_name=""
                tclasses=np.squeeze(classes).astype(np.int32)
                
                vehicle=[]
                vehicles_label=["car","bus","bicycle"]
                for i in range(len(scores[0])):
                    
                    if scores[0][i]>0.5 :
                        if tclasses[i] in category_index.keys():
                            class_name = category_index[tclasses[i]]['name']
                            if class_name in vehicles_label:
                                if class_name=="boat":
                                    class_name="truck"
                                vehicle.append(class_name)
                                  
                if (vehicle!=prev_vehicle):
                    vehicle_density1.append(len(vehicle))
                    prev_vehicle=vehicle
                       
                cv2.imshow('vehicle map1', input_frame)
                if len(vehicle_density1):
                    max1.value=max(vehicle_density1)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    
                    break
                
            video1.release()
            cv2.destroyAllWindows()
            
def vehicleDensity2(max2,vehicle_density2,lock):
    
    with graph.as_default():
        #with tf.Session(graph=graph) as session:
        with tf.compat.v1.Session(graph=graph) as session:
            image_tensor = graph.get_tensor_by_name('image_tensor:0')
            detection_scores = graph.get_tensor_by_name('detection_scores:0')
            detection_classes = graph.get_tensor_by_name('detection_classes:0')
            prev_vehicle=[]
            while video2.isOpened():
                (ret, frame) = video2.read()
                if not ret:
                    print ('buffer end...')
                    break

                input_frame = frame

                image_np_expanded = np.expand_dims(input_frame, axis=0)

               
                (scores, classes) =                     session.run([detection_scores,
                             detection_classes],
                             feed_dict={image_tensor: image_np_expanded})

                prev_class_name=""
                tclasses=np.squeeze(classes).astype(np.int32)
                
                vehicle=[]
                vehicles_label=["car","bus","bicycle"]
                for i in range(len(scores[0])):
                    
                    if scores[0][i]>0.5 :
                        if tclasses[i] in category_index.keys():
                            class_name = category_index[tclasses[i]]['name']
                            if class_name in vehicles_label:
                                if class_name=="boat":
                                    class_name="truck"
                                vehicle.append(class_name)
                                  
                if (vehicle!=prev_vehicle):
                    vehicle_density2.append(len(vehicle))
                    prev_vehicle=vehicle
                       
                cv2.imshow('vehicle map2', input_frame)
                if len(vehicle_density2):
                    max2.value=max(vehicle_density2)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    
                    break
                
            video2.release()
            cv2.destroyAllWindows()

def vehicleDensity3(max3,vehicle_density3,lock):
    
    with graph.as_default():
        #with tf.Session(graph=graph) as session:
        with tf.compat.v1.Session(graph=graph) as session:
            image_tensor = graph.get_tensor_by_name('image_tensor:0')
            detection_scores = graph.get_tensor_by_name('detection_scores:0')
            detection_classes = graph.get_tensor_by_name('detection_classes:0')
            prev_vehicle=[]
            while video3.isOpened():
                (ret, frame) = video3.read()
                if not ret:
                    print ('buffer end...')
                    break

                input_frame = frame

                image_np_expanded = np.expand_dims(input_frame, axis=0)

               
                (scores, classes) =                     session.run([detection_scores,
                             detection_classes],
                             feed_dict={image_tensor: image_np_expanded})

                prev_class_name=""
                tclasses=np.squeeze(classes).astype(np.int32)
                
                vehicle=[]
                vehicles_label=["car","bus","bicycle"]
                for i in range(len(scores[0])):
                    
                    if scores[0][i]>0.5 :
                        if tclasses[i] in category_index.keys():
                            class_name = category_index[tclasses[i]]['name']
                            if class_name in vehicles_label:
                                if class_name=="boat":
                                    class_name="truck"
                                vehicle.append(class_name)
                                  
                if (vehicle!=prev_vehicle):
                    vehicle_density3.append(len(vehicle))
                    prev_vehicle=vehicle
                       
                cv2.imshow('vehicle map3', input_frame)
                if len(vehicle_density3):
                    max3.value=max(vehicle_density3)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    
                    break
                
            video3.release()
            cv2.destroyAllWindows()

def trigger_green_lane1(delay,density2,density3):
    print("Traffic at lane 1 will be moving for :"+str(delay+STANDARD_TIME)+" seconds")
    time.sleep(delay+STANDARD_TIME)
    print("Red signal at lane 1")
    trigger_green_lane2(density2,density3)
    
def trigger_green_lane2(density2,density3):
    print("green signal at lane2")
    if density2>4 :
        print("Traffic at lane 2 will be moving for :"+str((density2/2)+STANDARD_TIME)+" seconds")
        time.sleep((density2/2)+STANDARD_TIME)
    else:
        print("Traffic at lane 2 will be moving for :"+str(density2)+" seconds")
        time.sleep(density2)
    print("Red signal at lane 2")
    trigger_green_lane3(density3) 
        
def trigger_green_lane3(density3):
    print("green signal at lane3")
    if density3>4 :
        print("Traffic at lane 3 will be moving for :"+str((density3/2)+STANDARD_TIME)+" seconds")
        time.sleep((density3/2)+STANDARD_TIME)
    else:
        print("Traffic at lane 3 will be moving for :"+str(density3)+" seconds")
        time.sleep(density3)
    print("Red signal at lane 3")        
            
def traffic(max1,max2,max3,vehicle_density1, vehicle_density2,vehicle_density3,lock):
    time.sleep(7)
    while True :
        td1=max1.value
        td2=max2.value
        td3=max3.value
        print("vehicle density at lane1: "+str(td1))
        print("vehicle density at lane2: "+str(td2))
        print("vehicle density at lane3: "+str(td3))
        vehicle_density1[:] = [] 
        vehicle_density2[:] = []
        vehicle_density3[:] = []
        print("green signal at lane1")
        if td1>4 :
            trigger_green_lane1(td1/2,td2,td3)
        else:
            print("Traffic at lane 1 will be moving for :"+str(td1)+" seconds")
            time.sleep(td1)
            print("Red signal at lane 1")    
            trigger_green_lane2(td2,td3)
        


# In[66]:

if __name__ == '__main__':

    manager = Manager()
    
    vehicle_density1 = manager.list([])
    vehicle_density2 = manager.list([])
    vehicle_density3 = manager.list([])
    max1= Value('i',0)
    max2= Value('i',0)
    max3= Value('i',0)
    lock=Lock()
    procs = [Process(target=vehicleDensity1, args=(max1,vehicle_density1, lock)),Process(target=vehicleDensity2, args=(max2,vehicle_density2, lock)),Process(target=vehicleDensity3, args=(max3,vehicle_density3, lock)),Process(target=traffic, args=(max1,max2,max3,vehicle_density1, vehicle_density2,vehicle_density3, lock))]
    for p in procs:
        p.start()
    for p in procs:
        p.join()
