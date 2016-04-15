import vrep
import sys

print 'Python program : v-rep'
vrep.simxFinish(-1)
clientID=vrep.simxStart('127.8.8.1',19999,True,True,5000,5)
if clientID != 1:
	print 'Connect to remote API server'
else:
	print 'Connection not successfull'
	sys.exit('Could not connect')
	
#get motor handle
errorCode,left_motor=vrep.simxGetObjectHandle(clientID,'Pioneer_p3dx_leftMotor',vrep.simx_opmode_oneshot_wait)
errorCode,right_motor=vrep.simxGetObjectHandle(clientID,'Pioneer_p3dx_rightMotor',vrep.simx_opmode_oneshot_wait)

errorCode,sensor16=vrep.simxGetObjectHandle(clientID,'Pioneer_p3dx_ultrasonicSensor16',vrep.simx_opmode_oneshot_wait)
errorCode,sensor5=vrep.simxGetObjectHandle(clientID,'Pioneer_p3dx_ultrasonicSensor5',vrep.simx_opmode_oneshot_wait)

for i in range(1,10):
	vrep.simxSetJointTargetVelocity(clientID,left_motor,2,vrep.simx_opmode_oneshot_wait)
	vrep.simxSetJointTargetVelocity(clientID,right_motor,2,vrep.simx_opmode_oneshot_wait)


for i in range(1,10000):
	vrep.simxSetJointTargetVelocity(clientID,left_motor,0,vrep.simx_opmode_oneshot_wait)
	vrep.simxSetJointTargetVelocity(clientID,right_motor,0,vrep.simx_opmode_oneshot_wait)
	
	#error_code,det_state, det_point, det_handle, det_vec = vrep.simxReadProximitySensor(clientID, sensor16, vrep.simx_opmode_oneshot_wait)
	#print 'Iteration : 16 det_state : ', det_state, ' det_point : ', det_point[2]
	error_code,det_state, det_point, det_handle, det_vec = vrep.simxReadProximitySensor(clientID, sensor5, vrep.simx_opmode_oneshot_wait)
	print 'Iteration : 5 det_state : ', det_state, ' det_point : ', det_point[2]
	
	while det_point[2] > 0.5:
		error_code,det_state, det_point, det_handle, det_vec = vrep.simxReadProximitySensor(clientID, sensor5, vrep.simx_opmode_oneshot_wait)
		print 'Iteration : 5 det_state : ', det_state, ' det_point : ', det_point[2]
		vrep.simxSetJointTargetVelocity(clientID,left_motor,2,vrep.simx_opmode_oneshot_wait)
		vrep.simxSetJointTargetVelocity(clientID,right_motor,2,vrep.simx_opmode_oneshot_wait)
		
	
	vrep.simxSetJointTargetVelocity(clientID,left_motor,10,vrep.simx_opmode_oneshot_wait)
	vrep.simxSetJointTargetVelocity(clientID,right_motor,-10,vrep.simx_opmode_oneshot_wait)

