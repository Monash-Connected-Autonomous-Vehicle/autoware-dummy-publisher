"""
message format: command (uint8)
0 = no command
1 = disable
2 = enable
"""

import rclpy
from autoware_vehicle_msgs.msg import HazardLightsCommand
from builtin_interfaces.msg import Time


def publishHazardLightsCmd(node):
    publisher = node.create_publisher(
        HazardLightsCommand, "/control/command/hazard_lights_cmd", 5
    )
    msg = HazardLightsCommand()

    while True:
        try:
            value = int(input("Command value (0 = no change, 1 = off, 2 = on): "))
            if not (0 <= value <= 2):
                print("Invalid command value")
                continue

            msg.command = value

            timestamp = Time()
            timestamp.sec, timestamp.nanosec = (
                rclpy.clock.Clock().now().seconds_nanoseconds()
            )
            msg.stamp = timestamp

            publisher.publish(msg)
            print(f"Published: command = {msg.command}")
        except:
            node.destroy_publisher(publisher)
            print("Cleaning up and closing publisher")
            break
