from .publishHazardLightsCmd import publishHazardLightsCmd
from .publishTurnIndicatorsCmd import publishTurnIndicatorsCmd
from .publishGearCmd import publishGearCmd
import rclpy


def main():
    rclpy.init()

    node = rclpy.create_node("dummy_autoware_node")

    # create messages and publishers
    opts = {
        "/control/command/hazard_lights_cmd": publishHazardLightsCmd,
        "/control/command/turn_indicators_cmd": publishTurnIndicatorsCmd,
        "/control/command/gear_cmd": publishGearCmd,
    }

    while True:
        # print options
        print("Options:")
        for i, topic in enumerate(opts.keys(), start=1):
            print(f"{i}: {topic}")

        while True:
            try:
                choice = input(f"Topic to publish to (1-{len(opts)}, q to quit): ")

                # exit publisher
                if choice.lower() == "q":
                    node.destroy_node()
                    rclpy.shutdown()
                    return

                # get and validate choice
                choice = int(choice) - 1
                if 0 <= choice < len(opts):
                    break
            except:
                print("Invalid input.")

        # run the publisher
        topic = list(opts.keys())[choice]
        opts[topic](node)


if __name__ == "__main__":
    main()
