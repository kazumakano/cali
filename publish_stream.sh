# publish video from RTSP stream to topic '/cam/image_raw'

URI=$1    # schemeless

roslaunch gstreamer_cv rtsp_single_stream.launch rtsp_url:=$1
