# Subscribe video from topic '/cam/image_raw' and '/cam/image_raw' and save to bag file.
# Press Ctrl + C to terminate.

CAM_NAME=$1      # Camera name.
RESULT_DIR=$2    # Path to result directory.

if [ $# != 2 ]; then
    echo usage: ./record.sh CAM_NAME PATH_TO_RESULT_DIR
    exit
fi

mkdir --parents $RESULT_DIR/$CAM_NAME/
rosbag record rosout /camera/image_raw /cam/image_raw --output-name=$RESULT_DIR/$CAM_NAME/video
