import vrep
import sys
import time

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
errorCode,usensor1=vrep.simxGetObjectHandle(clientID,'Pioneer_p3dx_ultrasonicSensor1',vrep.simx_opmode_oneshot_wait)
errorCode,usensor2=vrep.simxGetObjectHandle(clientID,'Pioneer_p3dx_ultrasonicSensor2',vrep.simx_opmode_oneshot_wait)
errorCode,usensor3=vrep.simxGetObjectHandle(clientID,'Pioneer_p3dx_ultrasonicSensor3',vrep.simx_opmode_oneshot_wait)
errorCode,usensor4=vrep.simxGetObjectHandle(clientID,'Pioneer_p3dx_ultrasonicSensor4',vrep.simx_opmode_oneshot_wait)
errorCode,usensor5=vrep.simxGetObjectHandle(clientID,'Pioneer_p3dx_ultrasonicSensor5',vrep.simx_opmode_oneshot_wait)
errorCode,usensor6=vrep.simxGetObjectHandle(clientID,'Pioneer_p3dx_ultrasonicSensor6',vrep.simx_opmode_oneshot_wait)
errorCode,usensor7=vrep.simxGetObjectHandle(clientID,'Pioneer_p3dx_ultrasonicSensor7',vrep.simx_opmode_oneshot_wait)
errorCode,usensor8=vrep.simxGetObjectHandle(clientID,'Pioneer_p3dx_ultrasonicSensor8',vrep.simx_opmode_oneshot_wait)
errorCode,usensor9=vrep.simxGetObjectHandle(clientID,'Pioneer_p3dx_ultrasonicSensor9',vrep.simx_opmode_oneshot_wait)
errorCode,usensor10=vrep.simxGetObjectHandle(clientID,'Pioneer_p3dx_ultrasonicSensor10',vrep.simx_opmode_oneshot_wait)
errorCode,usensor11=vrep.simxGetObjectHandle(clientID,'Pioneer_p3dx_ultrasonicSensor11',vrep.simx_opmode_oneshot_wait)
errorCode,usensor12=vrep.simxGetObjectHandle(clientID,'Pioneer_p3dx_ultrasonicSensor12',vrep.simx_opmode_oneshot_wait)
errorCode,usensor13=vrep.simxGetObjectHandle(clientID,'Pioneer_p3dx_ultrasonicSensor13',vrep.simx_opmode_oneshot_wait)
errorCode,usensor14=vrep.simxGetObjectHandle(clientID,'Pioneer_p3dx_ultrasonicSensor14',vrep.simx_opmode_oneshot_wait)
errorCode,usensor15=vrep.simxGetObjectHandle(clientID,'Pioneer_p3dx_ultrasonicSensor15',vrep.simx_opmode_oneshot_wait)
errorCode,usensor16=vrep.simxGetObjectHandle(clientID,'Pioneer_p3dx_ultrasonicSensor16',vrep.simx_opmode_oneshot_wait)

#for i in range(1,100):
#
#	vrep.simxSetJointTargetVelocity(clientID,left_motor,2,vrep.simx_opmode_oneshot_wait)
#	vrep.simxSetJointTargetVelocity(clientID,right_motor,2,vrep.simx_opmode_oneshot_wait)

for i in range(1,10000):

	vrep.simxSetJointTargetVelocity(clientID,left_motor,0,vrep.simx_opmode_oneshot_wait)
	vrep.simxSetJointTargetVelocity(clientID,right_motor,0,vrep.simx_opmode_oneshot_wait)

	#Sensor Depan
	error_code, det_state, det_point, det_handle, det_vec = vrep.simxReadProximitySensor(clientID, usensor1,vrep.simx_opmode_oneshot_wait)
	print 'Nomor Sensor : 1 det state: ', det_state,' det point : ', det_point[2]
	time.sleep(5);
	error_code, det_state, det_point, det_handle, det_vec = vrep.simxReadProximitySensor(clientID, usensor2,vrep.simx_opmode_oneshot_wait)
	print 'Nomor Sensor : 2 det state: ', det_state,' det point : ', det_point[2]
	time.sleep(5);
	error_code, det_state, det_point, det_handle, det_vec = vrep.simxReadProximitySensor(clientID, usensor3,vrep.simx_opmode_oneshot_wait)
	print 'Nomor Sensor : 3 det state: ', det_state,' det point : ', det_point[2]
	time.sleep(5);
	error_code, det_state, det_point, det_handle, det_vec = vrep.simxReadProximitySensor(clientID, usensor4,vrep.simx_opmode_oneshot_wait)
	print 'Nomor Sensor : 4 det state: ', det_state,' det point : ', det_point[2]
	time.sleep(5);
	error_code, det_state, det_point, det_handle, det_vec = vrep.simxReadProximitySensor(clientID, usensor5,vrep.simx_opmode_oneshot_wait)
	print 'Nomor Sensor : 5 det state: ', det_state,' det point : ', det_point[2]
	time.sleep(5);
	error_code, det_state, det_point, det_handle, det_vec = vrep.simxReadProximitySensor(clientID, usensor6,vrep.simx_opmode_oneshot_wait)
	print 'Nomor Sensor : 6 det state: ', det_state,' det point : ', det_point[2]
	time.sleep(5);
	error_code, det_state, det_point, det_handle, det_vec = vrep.simxReadProximitySensor(clientID, usensor7,vrep.simx_opmode_oneshot_wait)
	print 'Nomor Sensor : 7 det state: ', det_state,' det point : ', det_point[2]
	time.sleep(5);
	error_code, det_state, det_point, det_handle, det_vec = vrep.simxReadProximitySensor(clientID, usensor8,vrep.simx_opmode_oneshot_wait)
	print 'Nomor Sensor : 8 det state: ', det_state,' det point : ', det_point[2]
	time.sleep(5);
	
	#Sensor Belakang
	error_code, det_state, det_point, det_handle, det_vec = vrep.simxReadProximitySensor(clientID, usensor9,vrep.simx_opmode_oneshot_wait)
	print 'Nomor Sensor : 9 det state: ', det_state,' det point : ', det_point[2]
	time.sleep(5);
	error_code, det_state, det_point, det_handle, det_vec = vrep.simxReadProximitySensor(clientID, usensor10,vrep.simx_opmode_oneshot_wait)
	print 'Nomor Sensor : 10 det state: ', det_state,' det point : ', det_point[2]
	time.sleep(5);
	error_code, det_state, det_point, det_handle, det_vec = vrep.simxReadProximitySensor(clientID, usensor11,vrep.simx_opmode_oneshot_wait)
	print 'Nomor Sensor : 11 det state: ', det_state,' det point : ', det_point[2]
	time.sleep(5);
	error_code, det_state, det_point, det_handle, det_vec = vrep.simxReadProximitySensor(clientID, usensor12,vrep.simx_opmode_oneshot_wait)
	print 'Nomor Sensor : 12 det state: ', det_state,' det point : ', det_point[2]
	time.sleep(5);	
	error_code, det_state, det_point, det_handle, det_vec = vrep.simxReadProximitySensor(clientID, usensor13,vrep.simx_opmode_oneshot_wait)
	print 'Nomor Sensor : 12 det state: ', det_state,' det point : ', det_point[2]
	time.sleep(5);
	error_code, det_state, det_point, det_handle, det_vec = vrep.simxReadProximitySensor(clientID, usensor14,vrep.simx_opmode_oneshot_wait)
	print 'Nomor Sensor : 14 det state: ', det_state,' det point : ', det_point[2]
	time.sleep(5);
	error_code, det_state, det_point, det_handle, det_vec = vrep.simxReadProximitySensor(clientID, usensor15,vrep.simx_opmode_oneshot_wait)
	print 'Nomor Sensor : 15 det state: ', det_state,' det point : ', det_point[2]
	time.sleep(5);
	error_code, det_state, det_point, det_handle, det_vec = vrep.simxReadProximitySensor(clientID, usensor16,vrep.simx_opmode_oneshot_wait)
	print 'Nomor Sensor : 16 det state: ', det_state,' det point : ', det_point[2]
	time.sleep(5);
	
	
	
			

