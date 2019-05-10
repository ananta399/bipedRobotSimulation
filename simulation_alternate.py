import sys
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math

#################What if Baseplane is streched?????????#########################

def initializeRobot():
	global leftMotor
	global rightMotor
	global basePlateWidth
	global legLength
	leftMotor = [-basePlateWidth/2, 0, legLength, 0]
	rightMotor = [basePlateWidth/2, 0,  legLength, 0]


def turnRightMotor(degrees,ax,ax2):
	global leftMotor
	global rightMotor
	global basePlateWidth
	global legLength
	rads = np.radians(degrees)

	#Get the position of left and right foot
	leftFootX = leftMotor[0]
	rightFootX = rightMotor[0]
	leftFootY = leftMotor[1] + np.sin(leftMotor[3]) * legLength
	rightFootY = rightMotor[1] + np.sin(rightMotor[3]) * legLength
	leftFootZ = leftMotor[2] - np.cos(leftMotor[3]) * legLength
	rightFootZ = rightMotor[2] - np.cos(rightMotor[3]) * legLength


	for x in range (0, 100):
		gravityHappens()
		if (rads<0 and rightFootZ <= 0):	##Heel movement
			#Rotation
			leftMotor[3] += rads/100
			rightMotor[3] += rads/100

			#Forward movement
			
		else:								##Lift movement
			rightMotor[3] += rads/100
		drawRobot(ax,ax2)


def turnLeftMotor(degrees,ax,ax2):
	global leftMotor
	global rightMotor
	global basePlateWidth
	global legLength
	rads = np.radians(degrees)

	#Get the position of left and right foot
	leftFootX = leftMotor[0]
	rightFootX = rightMotor[0]
	leftFootY = leftMotor[1] + np.sin(leftMotor[3]) * legLength
	rightFootY = rightMotor[1] + np.sin(rightMotor[3]) * legLength
	leftFootZ = leftMotor[2] - np.cos(leftMotor[3]) * legLength
	rightFootZ = rightMotor[2] - np.cos(rightMotor[3]) * legLength

	for x in range (0, 100):
		leftMotor[3] += rads/100
		gravityHappens()
		drawRobot(ax,ax2)


#Left is Blue
#Right is Red
#Baseplate is green

def drawRobot(ax, ax2):
	global leftMotor
	global rightMotor
	global basePlateWidth
	global legLength


	#Get the position of left and right foot
	leftFootX = leftMotor[0]
	rightFootX = rightMotor[0]
	leftFootY = leftMotor[1] + np.sin(leftMotor[3]) * legLength
	rightFootY = rightMotor[1] + np.sin(rightMotor[3]) * legLength
	leftFootZ = leftMotor[2] - np.cos(leftMotor[3]) * legLength
	rightFootZ = rightMotor[2] - np.cos(rightMotor[3]) * legLength

	#############SideView####################
	#Initialize
	ax.set_xlabel("Y")
	ax.set_ylabel("Z")
	ax.set_xlim( [-10, 10] )
	ax.set_ylim( [0, 20] )
	# Turn off tick labels
	ax.set_yticklabels([])
	ax.set_xticklabels([])

	#Plot
	leftm, = ax.plot(leftMotor[1],leftMotor[2], 'bo')
	rightm, = ax.plot(rightMotor[1],rightMotor[2], 'ro')
	leftleg, = ax.plot([ leftMotor[1],   leftFootY ], [ leftMotor[2] , leftFootZ], color = 'blue')
	rightleg, = ax.plot([ rightMotor[1], rightFootY ], [rightMotor[2] , rightFootZ], color = 'red')
	basep, = ax.plot([ rightMotor[1], leftMotor[1] ], [rightMotor[2] , leftMotor[2]],color = 'green')

	#############FrontView####################
	#Initialize
	ax2.set_xlabel("X")
	ax2.set_ylabel("Z")
	ax2.set_xlim( [-10, 10] )
	ax2.set_ylim( [0, 20] )
	# Turn off tick labels
	ax2.set_yticklabels([])
	ax2.set_xticklabels([])

	#Plot
	leftm2, = ax2.plot(leftMotor[0],leftMotor[2], 'bo')
	rightm2, = ax2.plot(rightMotor[0],rightMotor[2], 'ro')
	leftleg2, = ax2.plot([ leftMotor[0],   leftFootX ], [ leftMotor[2] , leftFootZ],color = 'blue' )
	rightleg2, = ax2.plot([ rightMotor[0], rightFootX ], [rightMotor[2] , rightFootZ], color = 'red' )
	basep2, = ax2.plot([ rightMotor[0], leftMotor[0] ], [rightMotor[2] , leftMotor[2]],color = 'green')




	plt.pause(0.01)
	leftm.remove()
	rightm.remove()
	leftleg.remove()
	rightleg.remove()
	leftm2.remove()
	rightm2.remove()
	leftleg2.remove()
	rightleg2.remove()
	basep.remove()
	basep2.remove()



def gravityHappens():
	global leftMotor
	global rightMotor
	global basePlateWidth
	global legLength

	#Get the position of left and right foot
	leftFootX = leftMotor[0]
	rightFootX = rightMotor[0]
	leftFootY = leftMotor[1] + np.sin(leftMotor[3]) * legLength
	rightFootY = rightMotor[1] + np.sin(rightMotor[3]) * legLength
	leftFootZ = leftMotor[2] - np.cos(leftMotor[3]) * legLength
	rightFootZ = rightMotor[2] - np.cos(rightMotor[3]) * legLength

	# if (leftFootZ > rightFootZ):
	# 	heightAboveGround = rightFootZ
	# else:
	# 	heightAboveGround = leftFootZ

	leftMotor[2] -= leftFootZ
	rightMotor[2] -= rightFootZ

#######MAIN################
state = 0	#0 means start, 1 means stance

dt = 0.01;	
g = 10 #gravitaional constant
legLength = 10 #Leg Length
basePlateWidth = 5

leftMotor = [0,0,0,0] #x,y,z,angle
rightMotor = [0,0,0,0] 

fig = plt.figure()
fig.suptitle("SideView")
fig2 = plt.figure()
fig2.suptitle("FrontView")
ax = fig.add_subplot(111, aspect='equal')
ax2 = fig2.add_subplot(111, aspect='equal')


initializeRobot()

turnRightMotor(30,ax,ax2)

turnLeftMotor(-30,ax,ax2)

turnRightMotor(-30,ax,ax2)

turnLeftMotor(60,ax,ax2)


turnRightMotor(30,ax,ax2)

turnLeftMotor(-30,ax,ax2)

turnRightMotor(-30,ax,ax2)

turnLeftMotor(60,ax,ax2)