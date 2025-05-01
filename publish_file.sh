# publish video from file to topic '/camera/image_raw'

VID_FILE=$1    # path to video file
FPS=${2:-5}    # frame rate [fps] to publish

roslaunch video_stream_opencv camera.launch fps:=$FPS video_stream_provider:=$(realpath $VID_FILE)
