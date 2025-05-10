"""
message format: command (uint8)
0 = none
1 = neutral
2 = drive
3 = drive_2
4 = drive_3
5 = drive_4
6 = drive_5
7 = drive_6
8 = drive_7
9 = drive_8
10 = drive_9
11 = drive_10
12 = drive_11
13 = drive_12
14 = drive_13
15 = drive_14
16 = drive_15
17 = drive_16
18 = drive_17
19 = drive_18
20 = reverse
21 = reverse_2
22 = park
23 = low
24 = low_2
"""

import rclpy
from autoware_vehicle_msgs.msg import GearCommand
from builtin_interfaces.msg import Time


def publishGearCmd(node):
    publisher = node.create_publisher(GearCommand, "/control/command/gear_cmd", 5)

    while True:
        try:
            value = int(
                input(
                    """Command value
            0     = none
            1     = neutral
            2-19  = drive 1-18
            20-21 = reverse 1-2
            22    = park
            23-24 = low 1-2
            : """
                )
            )
            if not (0 <= value <= 24):
                print("Invalid command value")
                continue

            msg = GearCommand()
            msg.command = value

            msg.stamp = rclpy.clock.Clock().now().to_msg()

            publisher.publish(msg)
            print(f"Published: command = {msg.command}")
        except:
            node.destroy_publisher(publisher)
            print("Cleaning up and closing publisher")
            break
