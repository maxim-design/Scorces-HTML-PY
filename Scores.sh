#!/bin/bash

# Launch first Flask script
nohup python3 script1.py &

# Launch second Flask script
nohup python3 script2.py &

# Print the process IDs
echo "First script running with PID: $!"
echo "Second script running with PID: $!"
