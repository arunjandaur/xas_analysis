#!/bin/bash

#gnuplot -p
#plot "./relationships" using 1:2, '' using 1:3, '' using 1:4, '' using 1:5, '' using 1:6, '' using 1:7, '' using 1:8, '' using 1:9, '' using 1:10, '' using 1:11, '' using 1:12, '' using 1:13, '' using 1:14, '' using 1:15, '' using 1:16, '' using 1:17, '' using 1:18, '' using 1:19, '' using 1:20, '' using 1:21, '' using 1:22, '' using 1:23, '' using 1:24, '' using 1:25, '' using 1:26, '' using 1:27, '' using 1:28, '' using 1:29, '' using 1:30, '' using 1:31
#plot "<(sed -n '91,108p' ./relationships)" using 1:2 with lines

output="plot"

for file_name in "$@"
	do
		output="$output \"$file_name\" with lines,"
	done

echo ${output%?} | gnuplot -p

#echo 'plot "./1" with lines, "./2" with lines, "./3" with lines, "./4" with lines, "./5" with lines, "./6" with lines' | gnuplot -p
