import json
import os
import os.path as path
from glob import iglob
import yaml


def export(src_dir: str, tgt_dir: str) -> None:
    os.makedirs(tgt_dir, exist_ok=True)

    for cn in os.listdir(src_dir):
        for file in iglob(path.join(src_dir, cn, "log1-camchain.yaml")):
            with open(file) as f:
                cam = yaml.safe_load(f)["cam0"]

            with open(path.join(tgt_dir, f"camera{cn}.json"), mode="w") as f:
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
    parser.add_argument("-s", "--src_dir", required=True, help="specify source directory", metavar="PATH_TO_SRC_DIR")    # yaml format for kalibr
    parser.add_argument("-t", "--tgt_dir", required=True, help="specify target directory", metavar="PATH_TO_TGT_DIR")    # json format for trusco
    args = parser.parse_args()

    export(args.src_dir, args.tgt_dir)
