import vrep
import sys

print 'Python program : V-Rep'
vrep.simxFinish(-1)
clientID=vrep.simxStart('127.0.0.1',19999,True,True,5000,5)
if clientID!=1:
	print 'Connect to remote API Server'
else:
	print 'Connection not successful'
	sys.exit('Could not connect')

#Get motor handle
errorCode,left_motor=vrep.simxGetObjectHandle(clientID,'Pioneer_p3dx_leftMotor',vrep.simx_opmode_oneshot_wait)
errorCode,right_motor=vrep.simxGetObjectHandle(clientID,'Pioneer_p3dx_rightMotor',vrep.simx_opmode_oneshot_wait)

#Get sensor handle
errorCode,usensor16=vrep.simxGetObjectHandle(clientID,'Pioneer_p3dx_ultrasonicSensor16',vrep.simx_opmode_oneshot_wait)
errorCode,usensor4=vrep.simxGetObjectHandle(clientID,'Pioneer_p3dx_ultrasonicSensor4',vrep.simx_opmode_oneshot_wait)
errorCode,usensor3=vrep.simxGetObjectHandle(clientID,'Pioneer_p3dx_ultrasonicSensor3',vrep.simx_opmode_oneshot_wait)

#for i in range(1,100):
#
#	vrep.simxSetJointTargetVelocity(clientID,left_motor,2,vrep.simx_opmode_oneshot_wait)
#	vrep.simxSetJointTargetVelocity(clientID,right_motor,2,vrep.simx_opmode_oneshot_wait)

for i in range(1,10000):

	vrep.simxSetJointTargetVelocity(clientID,left_motor,0,vrep.simx_opmode_oneshot_wait)
	vrep.simxSetJointTargetVelocity(clientID,right_motor,0,vrep.simx_opmode_oneshot_wait)
	
	#if det_state == True:
	#	if det_point[2]<0.3:
	#		vrep.simxSetJointTargetVelocity(clientID,left_motor,1,vrep.simx_opmode_oneshot_wait)
	#		vrep.simxSetJointTargetVelocity(clientID,right_motor,1,vrep.simx_opmode_oneshot_wait)
	error_code, det_state, det_point, det_handle, det_vec = vrep.simxReadProximitySensor(clientID, usensor4,vrep.simx_opmode_oneshot_wait)
	print 'Iteration : 4 det state: ', det_state,' det point : ', det_point[2]
	if det_state == True:
		if det_point[2]<0.3:
			vrep.simxSetJointTargetVelocity(clientID,left_motor,3,vrep.simx_opmode_oneshot_wait)
			vrep.simxSetJointTargetVelocity(clientID,right_motor,0,vrep.simx_opmode_oneshot_wait)
		else:
			error_code, det_state, det_point, det_handle, det_vec = vrep.simxReadProximitySensor(clientID, usensor16,vrep.simx_opmode_oneshot_wait)
			print 'Iteration : 16 det state: ', det_state,' det point : ', det_point[2]
			if det_state == True:
				if det_point[2]<0.3:
					vrep.simxSetJointTargetVelocity(clientID,left_motor,1,vrep.simx_opmode_oneshot_wait)
					vrep.simxSetJointTargetVelocity(clientID,right_motor,1,vrep.simx_opmode_oneshot_wait)
				else:
					vrep.simxSetJointTargetVelocity(clientID,left_motor,0,vrep.simx_opmode_oneshot_wait)
					vrep.simxSetJointTargetVelocity(clientID,right_motor,1,vrep.simx_opmode_oneshot_wait)
			else:
				vrep.simxSetJointTargetVelocity(clientID,left_motor,1,vrep.simx_opmode_oneshot_wait)
				vrep.simxSetJointTargetVelocity(clientID,right_motor,1,vrep.simx_opmode_oneshot_wait)
	else:
		error_code, det_state, det_point, det_handle, det_vec = vrep.simxReadProximitySensor(clientID, usensor16,vrep.simx_opmode_oneshot_wait)
		print 'Iteration : 16 det state: ', det_state,' det point : ', det_point[2]
		if det_state == True:
			if det_point[2]<0.3:
				if det_point[2]<0.1:
					vrep.simxSetJointTargetVelocity(clientID,left_motor,1,vrep.simx_opmode_oneshot_wait)
					vrep.simxSetJointTargetVelocity(clientID,right_motor,0,vrep.simx_opmode_oneshot_wait)
				else:
					vrep.simxSetJointTargetVelocity(clientID,left_motor,1,vrep.simx_opmode_oneshot_wait)
					vrep.simxSetJointTargetVelocity(clientID,right_motor,1,vrep.simx_opmode_oneshot_wait)
			else:
				vrep.simxSetJointTargetVelocity(clientID,left_motor,-1,vrep.simx_opmode_oneshot_wait)
				vrep.simxSetJointTargetVelocity(clientID,right_motor,1,vrep.simx_opmode_oneshot_wait)
		else:
			vrep.simxSetJointTargetVelocity(clientID,left_motor,0,vrep.simx_opmode_oneshot_wait)
			vrep.simxSetJointTargetVelocity(clientID,right_motor,1,vrep.simx_opmode_oneshot_wait)
			

