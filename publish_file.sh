# Publish video from file to topic '/camera/image_raw'.

VID_FILE=$1    # Path to video file.
FPS=${2:-5}    # Frame rate [fps] to publish. Default is 5.

roslaunch video_stream_opencv camera.launch fps:=$FPS video_stream_provider:=$(realpath $VID_FILE)
