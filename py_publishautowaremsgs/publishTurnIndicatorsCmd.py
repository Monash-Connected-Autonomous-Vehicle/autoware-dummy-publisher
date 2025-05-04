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


def publishTurnIndicatorsCmd():
    rclpy.init()

    node = rclpy.create_node("dummy_autoware_node")
    publisher = node.create_publisher(
        TurnIndicatorsCommand, "/control/command/turn_indicators_cmd", 10
    )
    msg = TurnIndicatorsCommand()

    while True:
        try:
            value = int(
                input(
                    "Value to publish (0 = no change, 1 = off, 2 = left, 3 = right): "
                )
            )
            msg.command = value

            timestamp = Time()
            timestamp.sec, timestamp.nanosec = (
                rclpy.clock.Clock().now().seconds_nanoseconds()
            )
            msg.stamp = timestamp

            publisher.publish(msg)
            print(f"Published: command = {msg.command}")
        except:
            print("Closing publisher.")
            break
