#!/bin/bash

# Navigate to the directory with the .m3u8 files
cd /Users/bryanlee/Desktop/Mediacorp_Archives

# Loop through the .m3u8 files and convert them to .mp4
# TODO: Update the range in the for loop to match the number of episodes downloaded
for i in {1..40}; do
    # TODO: Customize the input file name to match the format from the Python script
    input_file="ItTakesTwo_E${i}_master.m3u8"  # Change 'ItTakesTwo' to your specific series title

    output_file="${input_file%.m3u8}.mp4"
    
    # Check if the input file exists before trying to convert
    if [ -f "$input_file" ]; then
        ffmpeg -protocol_whitelist file,http,https,tcp,tls,crypto -i "$input_file" -bsf:a aac_adtstoasc -vcodec copy -c copy -crf 50 "$output_file"
    else
        echo "File ${input_file} does not exist."
    fi
done
