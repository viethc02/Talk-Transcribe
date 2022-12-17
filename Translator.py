#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np
import os
import threading
from threading import Thread
from matplotlib import pyplot as plt
import mediapipe as mp
from tensorflow.keras.models import load_model
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import tensorflow as tf
import playsound
import gtts
from gtts import gTTS


# In[2]:


import unidecode
 
def remove_accent(text):
    return unidecode.unidecode(text)


# In[3]:


def texttospeech(text, lang1):
    language = gtts.lang.tts_langs()
    if lang1 in language.keys():
        output = gTTS(text, lang=lang1, slow=False)
        output.save("output.mp3")
        playsound.playsound("output.mp3", True)
        os.remove("output.mp3")

    else:
        text = "Please choose correct languages you want"
        output = gTTS(text, lang="en", slow=False)
        playsound.playsound("output1.mp3", True)
        os.remove("output1.mp3")


# In[4]:


cv2.__version__


# In[5]:


mp_hands = mp.solutions.holistic # Holistic model
mp_drawing = mp.solutions.drawing_utils # Drawing utilities


# In[6]:


def mediapipe_detection(image, model):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # COLOR CONVERSION BGR 2 RGB
    image.flags.writeable = False                  # Image is no longer writeable
    results = model.process(image)                 # Make prediction
    image.flags.writeable = True                   # Image is now writeable 
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR) # COLOR COVERSION RGB 2 BGR
    return image, results


# In[7]:


def draw_landmarks(image, results):
    mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_hands.HAND_CONNECTIONS) # Draw left hand connections
    mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_hands.HAND_CONNECTIONS) # Draw right hand connections


# In[8]:


def draw_styled_landmarks(image, results):
    mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_hands.HAND_CONNECTIONS, 
                             mp_drawing.DrawingSpec(color=(121,22,76), thickness=2, circle_radius=4), 
                             mp_drawing.DrawingSpec(color=(121,44,250), thickness=2, circle_radius=2)
                             ) 
    # Draw right hand connections  
    mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_hands.HAND_CONNECTIONS, 
                             mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=4), 
                             mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2)
                             ) 


# In[9]:


def extract_keypoints(results):
    lh = np.array([[res.x, res.y, res.z] for res in results.left_hand_landmarks.landmark]).flatten() if results.left_hand_landmarks else np.zeros(21*3)
    rh = np.array([[res.x, res.y, res.z] for res in results.right_hand_landmarks.landmark]).flatten() if results.right_hand_landmarks else np.zeros(21*3)
    return np.concatenate([lh, rh])


# In[10]:


actions = os.listdir(os.path.join(os.getcwd(), 'Sign-Language-Translator/Data'))


# In[11]:


actions


# In[12]:


model = load_model('Sign-Language-Translator/action.h5')


# In[13]:


model.summary()


# In[14]:


import cv2   
# 1. New detection variables
def cam():
    sequence = []
    sentence = []
    threshold = 0.8

    cap = cv2.VideoCapture(0)
    # Set mediapipe model
    with mp_hands.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
        while cap.isOpened():

            # Read feed
            ret, frame = cap.read() # đọc video từ camera
            if frame is None:
                continue
            #print(frame)
            #plt.imshow(frame)
            # Make detections
            image, results = mediapipe_detection(frame, holistic) # gọi biến image và result = giá trị RGB của ảnh
            print(results)
        
            # Draw landmarks
            draw_styled_landmarks(image, results) # nhận diện cơ thể
        
            # 2. Prediction logic
            keypoints = extract_keypoints(results) # xuất ra array các keypoints cơ thể (mấy cái đốt í)
            #print(keypoints)
            #sequence.insert(0,keypoints)
            #check = True
            values = np.array(keypoints)
            #values = map(list, int(values))
            #print(keypoints.all() == 0)
            #if (all(values) != 0):
            sequence.append(keypoints)
 
            sequence = sequence[-60:] # Đưa các frame thu đc vào mảng sequence, ở đây t để là 60 frame cuối
        
            if len(sequence) == 60:
                res = model.predict(np.expand_dims(sequence, axis=0))[0]
                print(actions[np.argmax(res)]) # Nếu thu đủ số frame của câu, đưa các array đấy vào model rồi ước lượng
                                           # ra kết quả chính xác nhất trong dữ liệu
            
            
            #3. Viz logic
                if res[np.argmax(res)] > threshold:
                    if len(sentence) > 0:
                        if actions[np.argmax(res)] != sentence[-1]:
                            sentence.append(actions[np.argmax(res)])
                    else:
                        sentence.append(actions[np.argmax(res)])

                if len(sentence) > 1:
                    sentence = sentence[-1:]

                # Viz probabilities
                # image = prob_viz(res, actions, image, colors)
        
            cv2.rectangle(image, (0,0), (640, 40), (245, 117, 16), -1)
            print(keypoints)
            print(len(sequence))
            if len(sentence) > 0:
                cv2.putText(image, remove_accent(sentence[0]), (3,30),
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
                if len(sequence) == 60:
                    texttospeech(sentence[0], 'vi')
                    #thread = Thread(target=texttospeech(sentence[0], 'vi'))
                    #thread.start()
                    sequence = []
            # Show to screen
            cv2.imshow('OpenCV Feed', image)

        # Break gracefully
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()


# In[ ]:





# In[ ]:





# In[ ]:




