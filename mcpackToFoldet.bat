#!/bin/bash

# Check if python is installed
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is not installed. Please install it first."
    exit 1
fi

# Run the python script
python3 mcpackToFolder.py

# Wait for user input before closing the terminal
read -n 1 -s -r -p "Press any key to continue..."
