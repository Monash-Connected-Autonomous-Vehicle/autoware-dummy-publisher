import rclpy
from autoware_control_msgs.msg import Control   

def publishAckermannCmd(node):
    """Interactive Ackermann controller publisher"""
    DEG_TO_RAD = 0.01745329252
    publisher = node.create_publisher(Control, "/control/command/control_cmd", 10)
    msg = Control()

    last_speed = 0.0
    last_angle = 0.0

    print("\nAckermann Controller Publisher")
    print("Enter speed (m/s) and steering angle (deg, +left).")
    print("Blank = reuse last value, Ctrl+C to exit.\n")

    try:
        while rclpy.ok():
            speed = input("Enter speed: ")
            angle = input("Enter angle: ")

            if speed.strip() == "":
                speed = last_speed
            if angle.strip() == "":
                angle = last_angle

            try:
                speed = float(speed)
                angle = float(angle)

                msg.longitudinal.velocity = speed
                msg.lateral.steering_tire_angle = angle * DEG_TO_RAD
                msg.stamp = node.get_clock().now().to_msg()

                publisher.publish(msg)
                print(f"Published Control: speed={speed}, angle={angle}°")

                last_speed, last_angle = speed, angle
            except ValueError:
                print("Invalid input, enter numeric values")

    except KeyboardInterrupt:
        print("Stopping Ackermann publisher\n")
        return