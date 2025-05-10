"""
message format: command (uint8)
0 = no command
1 = disable
2 = enable left
3 = enable right
"""

import rclpy
from autoware_vehicle_msgs.msg import TurnIndicatorsCommand
from builtin_interfaces.msg import Time


def publishTurnIndicatorsCmd(node):
    publisher = node.create_publisher(
        TurnIndicatorsCommand, "/control/command/turn_indicators_cmd", 5
    )
    msg = TurnIndicatorsCommand()

    while True:
        try:
            value = int(
                input("Command value (0 = no change, 1 = off, 2 = left, 3 = right): ")
            )
            if not (0 <= value <= 3):
                print("Invalid command value")
                continue

            msg.command = value
            msg.stamp = rclpy.clock.Clock().now().to_msg()

            publisher.publish(msg)
            print(f"Published: command = {msg.command}")
        except:
            node.destroy_publisher(publisher)
            print("Cleaning up and closing publisher")
            break
