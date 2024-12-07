#!/bin/bash

# Array of URLs and their corresponding custom filenames
declare -A scripts=(
    ["https://update.greasyfork.org/scripts/459541/YouTube%E5%8E%BB%E5%B9%BF%E5%91%8A.user.js"]="YouTube_Advertisement_Remover.user.js"
    ["https://update.greasyfork.org/scripts/421610/Youtube%20Speed%20Up.user.js"]="Youtube_Speed_Up.js"
    ["https://raw.githubusercontent.com/NullDev/YT-Anti-Anti-Adblock/refs/heads/master/yt-anti-anti-adblock.user.js"]="yt-anti-anti-adblock.user.js"
    # Add more URLs and filenames here if needed
)

# Function to download a script with a custom filename
download_script() {
    local url="$1"
    local filename="$2"
    echo "Downloading script from $url..."
    
    # Download the file and save it with the custom filename in the current directory
    curl -s -L "$url" -o "$filename"

    if [[ $? -eq 0 ]]; then
        echo "Script saved as $filename"
    else
        echo "Failed to download $url"
    fi
}

# Iterate over the URLs and filenames, and download each script
for url in "${!scripts[@]}"; do
    filename="${scripts[$url]}"
    download_script "$url" "$filename"
done

echo "Download process completed!"
