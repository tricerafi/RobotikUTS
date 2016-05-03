# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 01:11:23 2015

@author: anwar.maxsum
"""

#simExtRemoteApiStart(19999)

import vrep
import numpy
import matplotlib
import sys

import kalman

print 'Python program : V-Rep'
vrep.simxFinish(-1)
clientID=vrep.simxStart('127.0.0.1',19999,True,True,5000,5)
if clientID!=-1:
    print 'Coonect to remote API Server'
else:
    print 'Connection not successful'
    sys.exit('Could not connect')
    
    
i = 0
v = 0.05

offSetX = 0
offsetY = 0
initX = 0.5
initY = -2.0

mu_t = 2.0
sigma_t = 0.01

#Get motor handle
errorCode,left_motor=vrep.simxGetObjectHandle(clientID,'Pioneer_p3dx_leftMotor',vrep.simx_opmode_oneshot_wait)
errorCode,right_motor=vrep.simxGetObjectHandle(clientID,'Pioneer_p3dx_rightMotor',vrep.simx_opmode_oneshot_wait)    

# Get ultrasound sensors handle
errorCode,usensor1=vrep.simxGetObjectHandle(clientID,'Pioneer_p3dx_ultrasonicSensor8',vrep.simx_opmode_oneshot_wait)           

# Get camera sensors handle
errorCode,cam_handle=vrep.simxGetObjectHandle(clientID,'Camera',vrep.simx_opmode_oneshot_wait)           
errorCode,resolution,image=vrep.simxGetVisionSensorImage(clientID,cam_handle,0,vrep.simx_opmode_oneshot_wait)

pX = pY = 0.0
for i in range (1,30) :
    errorCode,gpsX=vrep.simxGetFloatSignal(clientID,'gpsX',vrep.simx_opmode_oneshot_wait);
    errorCode,gpsY=vrep.simxGetFloatSignal(clientID,'gpsY',vrep.simx_opmode_oneshot_wait);
    pX += gpsX
    pY += gpsY
    
offSetX = (pX/30) - initX
offSetY = (pY/30) - initY
    

for i in range(1,11):
#while True :
    print 'Iteration : ', i
    
    # Get ultrasound sensors handle
    #errorCode,usensor1=vrep.simxGetObjectHandle(clientID,'Pioneer_p3dx_ultrasonicSensor8',vrep.simx_opmode_oneshot_wait)           
    # Read ultrasound sensor
    #errorCode,detectionState,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,usensor1,vrep.simx_opmode_buffer)
    #errorCode,detectionState,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,usensor1,vrep.simx_opmode_oneshot_wait)
    #print errorCode,detectionState,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector
    
     
    #Set motor
    vrep.simxSetJointTargetVelocity(clientID,left_motor,2,vrep.simx_opmode_oneshot_wait)
    vrep.simxSetJointTargetVelocity(clientID,right_motor,2,vrep.simx_opmode_oneshot_wait)
    
    # Read ultrasound sensor
    errorCode,detectionState,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,usensor1,vrep.simx_opmode_oneshot_wait)
    #errorCode,detectionState,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,usensor1,vrep.simx_opmode_oneshot_wait)
    # print errorCode,detectionState,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector
        
    #Read GPS Sensor
    errorCode,gpsX=vrep.simxGetFloatSignal(clientID,'gpsX',vrep.simx_opmode_oneshot_wait);
    errorCode,gpsY=vrep.simxGetFloatSignal(clientID,'gpsY',vrep.simx_opmode_oneshot_wait);
    gpsX = gpsX - offSetX
    gpsY = gpsY - offSetY
   
    [mu_temp, sigma_temp]=kalman.kalman_prediction(i, mu_t, sigma_t, 2, gpsY)    
    mu_t = mu_temp
    sigma_t =  sigma_temp    
    
    print 'iteration : ', i, 'mu = ', mu_t, 'sigma = ', sigma_t, '\n'
    i=i+1

    
vrep.simxSetJointTargetVelocity(clientID,left_motor,0,vrep.simx_opmode_oneshot_wait)
vrep.simxSetJointTargetVelocity(clientID,right_motor,0,vrep.simx_opmode_oneshot_wait)    
print 'Done....'
    