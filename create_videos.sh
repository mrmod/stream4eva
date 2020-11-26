#!/bin/bash

TCP_STREAM=tcp://raspberrypi:8500
HTTP_VIDEO_URL=http://localhost:9201/

# To receive input from raspberrypi instead
if [ $1 == "LIVE" ] ; then
  echo "Doing it live"
  ffmpeg \
    -i $TCP_STREAM \
  -codec copy \
  -y \
  -f segment \
  -segment_time 30 \
  -segment_list "./videos/live.m3u8" \
  -segment_list_entry_prefix "$HTTP_VIDEO_URL" \
  videos/live%d.ts

  exit 0
fi


rm -rf videos
mkdir videos
  #-vf format=yuv420p \

# Framerate: Input FPS (max 30fps)
# R: FPS of video segments
python3 create_image.py True | ffmpeg \
  -f image2pipe \
  -framerate 25 \
  -r 24 \
  -i - \
  -c:v libx264 \
  -movflags +faststart \
  -y \
  -f segment \
  -segment_time 30 \
  -segment_list "./videos/live.m3u8" \
  -segment_list_type m3u8 \
  -segment_list_entry_prefix "$HTTP_VIDEO_URL" \
  videos/live%d.ts

