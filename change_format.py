import json
import os.path as path
import yaml


def change(src_file: str) -> None:
    with open(src_file) as f:
        cam = yaml.safe_load(f)["cam0"]

    with open(path.splitext(src_file)[0] + ".json", mode="w") as f:
        json.dump({
            "value0": {
                "intrinsics": [{
                    "camera_type": cam["camera_model"],
                    "intrinsics": {
                        "fx": cam["intrinsics"][2],
                        "fy": cam["intrinsics"][3],
                        "cx": cam["intrinsics"][4],
                        "cy": cam["intrinsics"][5],
                        "xi": cam["intrinsics"][0],
                        "alpha": cam["intrinsics"][1]
                    }
                }],
                "resolution": [cam["resolution"]]
            }
        }, f, indent=2)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--src_file", required=True, help="specify source file", metavar="PATH_TO_SRC_FILE")    # yaml format for kalibr

    change(parser.parse_args().src_file)
