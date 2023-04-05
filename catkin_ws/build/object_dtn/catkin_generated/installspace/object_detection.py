#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64
from sensor_msgs import Image

# algorithm which processes image and returns offtrack number
def algorithm(image):
    return Float64

def object_detector(data):
    Float64 obj_distance = algorithm(data)
    rospy.loginfo(obj_distance)
    obj_dtn.publish(obj_distance)
    rate.sleep()

def object_detection():
    rospy.init_node('object_detection', anonymous=True)

    obj_dtn = rospy.Publisher('distance', Float64, queue_size=10)
    rate = rospy.Rate(10)

    rospy.Subscriber("image", Image, object_detector)
    # image topic is placeholder for now
    # actual is rosserial

    rospy.spin()

if __name__ == '__main__':
    try:
        object_detection()
    except rospy.ROSInterruptException:
        pass