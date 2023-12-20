#!/usr/bin/env python3



import unittest
import rclpy
import time
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from safety_monitoring_SMACH  import MonitorBatteryAndCollision, RotateBase, StopBase

class TestStateMachine(unittest.TestCase):

    def setUp(self):
        rclpy.init()

    def tearDown(self):
        rclpy.shutdown()

    def test_monitor_battery_and_collision_low_battery(self):
        node = rclpy.create_node('test_node')
        state = MonitorBatteryAndCollision(node, battery_threshold=90, collision_threshold_distance=1, timeout=5)

        low_battery_msg = String()
        low_battery_msg.data = '100.0' 
        state.battery_callback(low_battery_msg)

        outcome = state.execute(None)
        
        self.assertEqual(outcome, 'low_battery_level')

    def test_monitor_battery_and_collision_possible_collision(self):
        node = rclpy.create_node('test_node')
        state = MonitorBatteryAndCollision(node, battery_threshold=90, collision_threshold_distance=1, timeout=5)

        collision_msg = LaserScan()
        collision_msg.ranges = [0.4, 0.6, 0.7] 
        state.laser_scan_callback(collision_msg)


        outcome = state.execute(None)

        self.assertEqual(outcome, 'possible_collision')

    def test_rotate_base(self):
        node = rclpy.create_node('test_node')
        state = RotateBase(node)


        outcome = state.execute(None)

        self.assertEqual(outcome, 'succeeded')

    def test_stop_base(self):
        node = rclpy.create_node('test_node')
        state = StopBase(node)

        outcome = state.execute(None)

        self.assertEqual(outcome, 'succeeded')

if __name__ == '__main__':
    unittest.main()

