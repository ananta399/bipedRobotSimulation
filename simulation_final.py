#A simulation designed to test the stability of a biped Robot with respect to curvature of the foot
#For CS442 Final Project, Simulation is based on Physical Robot Design

import sys
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math
import matplotlib.patches as mpatches


def calculateMomentOfInertia():
	global motormass
	global legmass
	global legLength
	global basePlateLength

	if (theta <= np.pi/2):	#Right leg on ground
		contactPointWithGround_x = basePlateLength/2
		rightMotor_x = contactPointWithGround_x + legLength*np.cos(theta)
		rightMotor_y = legLength*np.sin(theta)

		leftMotor_x = rightMotor_x - basePlateLength*np.sin(theta)
		leftMotor_y = rightMotor_y + basePlateLength*np.cos(theta)

		COG_X = (leftMotor_x + rightMotor_x)/2
		COG_Y = (leftMotor_y + rightMotor_y)/2

		#The point of rotation also changes, so adjust for that
		COR_X = COG_X - contactPointWithGround_x

	else: #Left leg on ground
		contactPointWithGround_x = -basePlateLength/2
		leftMotor_x = contactPointWithGround_x + legLength*np.cos(theta)
		leftMotor_y = legLength*np.sin(theta)

		rightMotor_x = leftMotor_x + basePlateLength*np.sin(theta)
		rightMotor_y = leftMotor_y - basePlateLength*np.cos(theta)

		COG_X = (leftMotor_x + rightMotor_x)/2
		COG_Y = (leftMotor_y + rightMotor_y)/2

		#The point of rotation also changes, so adjust for that
		COR_X = COG_X - contactPointWithGround_x

	moi = math.sqrt(COR_X*COR_X + COG_Y*COG_Y)

	return moi

def getCOG_X():
	global motormass
	global legmass
	global legLength
	global basePlateLength

	if (theta <= np.pi/2):	#Right leg on ground
		contactPointWithGround_x = basePlateLength/2
		rightMotor_x = contactPointWithGround_x + legLength*np.cos(theta)
		rightMotor_y = legLength*np.sin(theta)

		leftMotor_x = rightMotor_x - basePlateLength*np.sin(theta)
		leftMotor_y = rightMotor_y + basePlateLength*np.cos(theta)

		COG_X = (leftMotor_x + rightMotor_x)/2
	else: #Left leg on ground
		contactPointWithGround_x = -basePlateLength/2
		leftMotor_x = contactPointWithGround_x + legLength*np.cos(theta)
		leftMotor_y = legLength*np.sin(theta)

		rightMotor_x = leftMotor_x + basePlateLength*np.sin(theta)
		rightMotor_y = leftMotor_y - basePlateLength*np.cos(theta)

		COG_X = (leftMotor_x + rightMotor_x)/2

	return COG_X

#Returns the x coordinate end point of Left curved Feet
def getEndPoint_left(theta):
	alpha = arc_length_of_curved_feet/radius_of_cylinder #Angular range of curved feet

	if (theta <= np.pi/2):	#Right leg on ground
		contactPointWithGround_x = basePlateLength/2
		rightMotor_x = contactPointWithGround_x + legLength*np.cos(theta)
		leftMotor_x = rightMotor_x - basePlateLength*np.sin(theta)
		leftFeet_x = leftMotor_x - legLength*np.cos(theta)
		rightFeet_x = rightMotor_x - legLength*np.cos(theta)

	else: #Left leg on ground
		contactPointWithGround_x = -basePlateLength/2
		leftMotor_x = contactPointWithGround_x + legLength*np.cos(theta)
		leftFeet_x = leftMotor_x - legLength*np.cos(theta)
		rightMotor_x = leftMotor_x + basePlateLength*np.sin(theta)
		rightFeet_x = rightMotor_x - legLength*np.cos(theta)

	leg_ratio = radius_of_cylinder/legLength
	xcenter_left_cylinder = leftFeet_x + leg_ratio*legLength*np.cos(theta)
	return xcenter_left_cylinder + radius_of_cylinder*np.cos(np.pi + theta - alpha/2)


#Returns the x coordinate end point of right curved Feet
def getEndPoint_right(theta):

	alpha = arc_length_of_curved_feet/radius_of_cylinder #Angular range of curved feet

	if (theta <= np.pi/2):	#Right leg on ground
		contactPointWithGround_x = basePlateLength/2
		rightMotor_x = contactPointWithGround_x + legLength*np.cos(theta)
		leftMotor_x = rightMotor_x - basePlateLength*np.sin(theta)
		leftFeet_x = leftMotor_x - legLength*np.cos(theta)
		rightFeet_x = rightMotor_x - legLength*np.cos(theta)

	else: #Left leg on ground
		contactPointWithGround_x = -basePlateLength/2
		leftMotor_x = contactPointWithGround_x + legLength*np.cos(theta)
		leftFeet_x = leftMotor_x - legLength*np.cos(theta)
		rightMotor_x = leftMotor_x + basePlateLength*np.sin(theta)
		rightFeet_x = rightMotor_x - legLength*np.cos(theta)

	leg_ratio = radius_of_cylinder/legLength
	xcenter_right_cylinder = rightFeet_x + leg_ratio*legLength*np.cos(theta)
	return xcenter_right_cylinder + radius_of_cylinder*np.cos(np.pi + theta + alpha/2)

def drawRobot(ax, theta, legLength):

	global dt
	global numSteps
	global basePlateLength
	global radius_of_curved_feet

	#############Actual View####################

	if (theta <= np.pi/2):	#Right leg on ground
		contactPointWithGround_x = basePlateLength/2
		rightMotor_x = contactPointWithGround_x + legLength*np.cos(theta)
		rightMotor_y = legLength*np.sin(theta)
		rightleg, = ax.plot([ contactPointWithGround_x, rightMotor_x], [0 , rightMotor_y],color = 'green')

		leftMotor_x = rightMotor_x - basePlateLength*np.sin(theta)
		leftMotor_y = rightMotor_y + basePlateLength*np.cos(theta)
		basePlate, = ax.plot([ rightMotor_x, leftMotor_x], [rightMotor_y , leftMotor_y],color = 'green')

		leftFeet_x = leftMotor_x - legLength*np.cos(theta)
		leftFeet_y = leftMotor_y - legLength*np.sin(theta)
		leftleg, = ax.plot([ leftMotor_x, leftFeet_x], [leftMotor_y , leftFeet_y],color = 'green')

		rightFeet_x = rightMotor_x - legLength*np.cos(theta)
		rightFeet_y = rightMotor_y - legLength*np.sin(theta)

	else: #Left leg on ground
		contactPointWithGround_x = -basePlateLength/2
		leftMotor_x = contactPointWithGround_x + legLength*np.cos(theta)
		leftMotor_y = legLength*np.sin(theta)
		leftleg, = ax.plot([ contactPointWithGround_x, leftMotor_x], [0 , leftMotor_y ],color = 'green')

		rightMotor_x = leftMotor_x + basePlateLength*np.sin(theta)
		rightMotor_y = leftMotor_y - basePlateLength*np.cos(theta)
		basePlate, = ax.plot([ rightMotor_x, leftMotor_x], [rightMotor_y , leftMotor_y],color = 'green')

		rightFeet_x = rightMotor_x - legLength*np.cos(theta)
		rightFeet_y = rightMotor_y - legLength*np.sin(theta)
		rightleg, = ax.plot([ rightMotor_x, rightFeet_x], [rightMotor_y , rightFeet_y],color = 'green')

		leftFeet_x = leftMotor_x - legLength*np.cos(theta)
		leftFeet_y = leftMotor_y - legLength*np.sin(theta)

	#Center of Gravity
	COG_X = (leftMotor_x + rightMotor_x)/2
	COG_Y = (leftMotor_y + rightMotor_y)/2
	center_of_g, = ax.plot(COG_X,COG_Y, 'bo')

	##Draw curved feet##### See Methods section for details

	leg_ratio = radius_of_cylinder/legLength
	xcenter_left_cylinder = leftFeet_x + leg_ratio*legLength*np.cos(theta)
	ycenter_left_cylinder = leftFeet_y + leg_ratio*legLength*np.sin(theta)
	#leftPoint = ax.plot(xcenter_left_cylinder,ycenter_left_cylinder, 'bo')
	alpha = arc_length_of_curved_feet/radius_of_cylinder #Angular range of curved feet
	leftFeet = mpatches.Arc((xcenter_left_cylinder, ycenter_left_cylinder), radius_of_cylinder*2, radius_of_cylinder*2,
                 angle= math.degrees(np.pi + theta + alpha/2),theta1 = math.degrees(- alpha), theta2 = math.degrees(0), linewidth=2, fill=False, zorder=2)
	ax.add_patch(leftFeet)

	xcenter_right_cylinder = rightFeet_x + leg_ratio*legLength*np.cos(theta)
	ycenter_right_cylinder = rightFeet_y + leg_ratio*legLength*np.sin(theta)
	#rightPoint = ax.plot(xcenter_right_cylinder,ycenter_right_cylinder, 'bo')
	alpha = arc_length_of_curved_feet/radius_of_cylinder #Angular range of curved feet
	rightFeet = mpatches.Arc((xcenter_right_cylinder, ycenter_right_cylinder), radius_of_cylinder*2, radius_of_cylinder*2,
                 angle= math.degrees(np.pi + theta + alpha/2),theta1 = math.degrees(- alpha), theta2 = math.degrees(0), linewidth=2, fill=False, zorder=2)

	ax.add_patch(rightFeet)


	#Draw End points
	leftEnd, = ax.plot([ getEndPoint_left(theta), getEndPoint_left(theta)], [-1 , 1],color = 'red')
	rightEnd, = ax.plot([ getEndPoint_right(theta), getEndPoint_right(theta)], [-1 , 1],color = 'red')

	#Initialize
	ax.set_xlabel("Y")
	ax.set_ylabel("Z")
	ax.set_xlim( [-(legLength + 0.1), legLength + 0.1] )
	ax.set_ylim( [-0.003, legLength + 0.1] )
	# Turn off tick labels
	ax.set_yticklabels([])
	ax.set_xticklabels([])

	# leg, = ax.plot([ contactPointWithGround_x, COG_X ], [0 , COG_Y ],color = 'green')

	#plt.pause(dt)
	# leg.remove()
	center_of_g.remove()
	leftleg.remove()
	rightleg.remove()
	basePlate.remove()
	leftFeet.remove()
	rightFeet.remove()
	leftEnd.remove()
	rightEnd.remove()

#######MAIN################
dt = 0.01

#Control Variable
radius_of_cylinder = 0.012

#constants
arc_length_of_curved_feet = 0.07

basePlateLength = 0.095
motormass = 0.15 #in kilograms, each motor is 60 grams, baseplaye is 30 grams
legLength = 0.26 #in meters
legmass = 0.01 
KE = 0 #Initial Kinetic Energy
KE_Gain_At_Each_Step = 0.01
timeBetweenSteps = 0.5  #time between steps
timeAfterLastStep = 0
numSteps = 0


#Display
fig = plt.figure()
fig.suptitle("FrontView")
ax = fig.add_subplot(111, aspect='equal')


theta = np.pi/2 #Angle in radians, starting angle

drawRobot(ax, theta, legLength)


#Main Loop
while (1):
	MOI = calculateMomentOfInertia()

	center_of_g_X = getCOG_X()

	#Falling condition
	if ( center_of_g_X < getEndPoint_left(theta) or center_of_g_X > getEndPoint_right(theta) ):
		print "Fell after: ", numSteps ," Steps"
		break


	#Check if step is taken
	timeAfterLastStep = timeAfterLastStep + dt
	if (timeAfterLastStep >= timeBetweenSteps):
		numSteps = numSteps + 1
		KE = KE + KE_Gain_At_Each_Step
		timeAfterLastStep = 0
		print "Step " ,numSteps


	#Calculate Angular Velocity
	AV = math.sqrt(2*abs(KE)) * (-1)**numSteps

	#Update Angular Position
	theta = theta + AV*dt

	drawRobot(ax, theta, legLength)

