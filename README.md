# Autoware Dummy Publisher
ROS2 package to simulate autoware command messages from the command line.

## Requirements

[SD-VehicleInterface](https://github.com/Monash-Connected-Autonomous-Vehicle/SD-VehicleInterface/tree/ackermann) and [autoware_msgs](https://github.com/autowarefoundation/autoware_msgs.git) must be available in the `<workspace>/src` directory to receive these messages.

## Usage

1. In workspace root, run `colcon build` to build both `SD-VehicleInterface` and `py_publishautowaremsgs` packages
2. In 2 separate terminals, run `source ./install/setup.bash`
3. Start SD-vehicle interface in one terminal
    - `ros2 launch sd_vehicle_interface sd_vehicle_interface.launch.xml sd_simulation_mode:=true`
4. Run the autoware dummy publisher in the other terminal
    - `ros2 run py_publishautowaremsgs controller`
5. Follow instructions in dummy publisher terminal to send commands
6. Debug messages are printed to the sd_vehicle_interface terminal when the program terminates (Ctrl+C)

