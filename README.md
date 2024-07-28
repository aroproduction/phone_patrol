# Mobile Phone Detection in No-Mobile Zones

## Team Details

*Team Name:* HackHounds

*College/University:* Heritage Institute of Technology

*Team Members:*
- Aritra Dutta Banik
- Trisagni Mandal
- Anubhab Mukherjee
- Sharnabho Chatterjee

## Project Overview

This project outlines the development of a cutting-edge system designed to detect individuals using mobile phones in restricted areas. The system utilizes a combination of hardware and software to automatically identify and alert authorities about unauthorized mobile phone usage. This innovative solution addresses the growing need for robust security measures in locations where mobile phone usage is prohibited, ensuring a secure and controlled environment.

## The Need for Detection

1. *Preserving Confidentiality:*
   Sensitive information is often handled in restricted areas such as hospitals, government offices, and examination halls. Detecting unauthorized mobile phone usage helps maintain confidentiality and prevent the potential misuse of sensitive data.

2. *Enhancing Security:*
   Mobile phones can be used to capture images, record audio, or transmit information. Detecting mobile phone usage in restricted areas helps prevent potential security breaches and ensures a safe environment.

3. *Maintaining Focus:*
   In certain locations like classrooms, conference rooms, and religious institutions, mobile phone usage can be disruptive and hinder concentration. Detecting mobile phone usage helps promote a focused and productive environment.

4. *Preventing Interference:*
   Mobile phones can interfere with sensitive equipment such as medical devices and security systems. Detecting mobile phone usage helps mitigate potential interference and ensure the proper functioning of critical systems.

## Solution Approach

1. *Image Capture:*
   A Raspberry Pi 5 board equipped with a USB camera captures images of the designated area at regular intervals. The camera can be a standard webcam or a specialized wireless camera module.

2. *Object Detection:*
   The captured images are then analyzed by a pre-trained YOLO model, a powerful object detection algorithm which identifies objects within the image. In this case, the YOLO model is trained to specifically identify mobile phones.

3. *Face Recognition:*
   If a mobile phone is detected, a second YOLO model is deployed to detect the face of the individual using the phone. This facial recognition step helps identify the specific individual violating the no-mobile zone policy.

4. *Alert Generation:*
   Based on the detected mobile phone and the identified individual, an alert is generated. The alert can include the timestamp, the captured image, and the identified individual's details. This alert is then sent to the designated authorities.

## limitations

1. for face recognition model it can only recognise four of us , if user train with different images or goverment gives us the access of the aadhar data ,then we can racognize faces and get their contact number

2. it only genrates warning messages to whoever violates the no mobile zone rule


## how to run

1. clone this repo

2. pip -r requirment.txt

3. python live-detect.py
