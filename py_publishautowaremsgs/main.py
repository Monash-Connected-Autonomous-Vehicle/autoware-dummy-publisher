from .publishHazardLightsCmd import publishHazardLightsCmd
from .publishTurnIndicatorsCmd import publishTurnIndicatorsCmd
from .publishGearCmd import publishGearCmd
import rclpy


def main():
    rclpy.init()

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
                if choice.lower() == "q":
                    exit(0)
                choice = int(choice) - 1
                if 0 <= choice < len(opts):
                    break
            except:
                print("Invalid input.")
                continue

        topic = list(opts.keys())[choice]
        opts[topic]()


if __name__ == "__main__":
    main()
