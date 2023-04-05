#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64
from sensor_msgs import Image

# algorithm which processes image and returns distance from garbage
def algorithm(image):
    return Float64

def offtrack_detector(data):
    Float64 offtrack_number = algorithm(data)
    rospy.loginfo(offtrack_number)
    lane_dtn.publish(offtrack_number)
    rate.sleep()

def lane_detection():
    rospy.init_node('lane_detection', anonymous=True)

    lane_dtn = rospy.Publisher('image_value', Float64, queue_size=10)
    rate = rospy.Rate(10)

    rospy.Subscriber("image", Image, offtrack_detector)
    # image topic is placeholder for now
    # actual is rosserial

    rospy.spin()

if __name__ == '__main__':
    try:
        lane_detection()
    except rospy.ROSInterruptException:
        pass