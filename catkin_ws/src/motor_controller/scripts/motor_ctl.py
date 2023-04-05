#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64

# algorithm which processes image and returns distance from garbage
def algorithm(image):
    return Float64

def velocity_calculator(current_vel):
    # pid bw generated and actual velocity
    # store new velocity in new_vel
    rospy.loginfo(new_vel)
    mot_vel_ctl.publish(new_vel)
    rate.sleep()

def steer_calculator(offtrack_num):
    # p controller
    # store new steer angle in new_str
    rospy.loginfo(new_str)
    mot_str_ctl.publish(new_str)
    rate.sleep()

def vel_profile_calculator(dist):
    # generate velocity profile as per distance  and current velocity
    # trapezium profile
    rate.sleep()

def motor_ctl():
    rospy.init_node('motor_ctl', anonymous=True)

    mot_vel_ctl = rospy.Publisher('velocity', Float64, queue_size=10)
    rate = rospy.Rate(10)

    mot_str_ctl = rospy.Publisher('steer', Float64, queue_size=10)
    rate = rospy.Rate(10)

    rospy.Subscriber("image_value", Float64, steer_calculator)
    rospy.Subscriber("distance", Float64, vel_profile_calculator)
    
    rospy.Subscriber("curr_vel", Float64, velocity_calculator)
    # curr_vel is a placeholder
    # actual will be rosserial
    # gives current velocity of bot

    rospy.spin()

if __name__ == '__main__':
    try:
        motor_ctl()
    except rospy.ROSInterruptException:
        pass