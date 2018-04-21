#!/bin/bash
rm -f transforms.trf
ffmpeg -i "$1" -vf vidstabdetect=shakiness=10:accuracy=15 -f null -
ffmpeg -i "$1" -vf vidstabtransform=smoothing=10:input="transforms.trf" "$1"-stabilized.mp4
ffmpeg -i "$1" -i "$1"-stabilized.mp4  -filter_complex hstack "$1"-merged.mp4
