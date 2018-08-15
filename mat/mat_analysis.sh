#!/bin/bash
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <path to heapdump>"
    exit
fi

# read -p "Have you set the heap to 2/3 of heapdump in MAT.ini and started this in a screen session?"
for report in org.eclipse.mat.api:suspects org.eclipse.mat.api:overview org.eclipse.mat.api:top_components;
  do
     /mat/ParseHeapDump.sh -keep_unreachable_objects $1 "$report"
  done

