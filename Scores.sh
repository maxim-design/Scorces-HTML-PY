#!/bin/bash

# Launch first Flask script
nohup python3.8 Leaderboard.py &

# Launch second Flask script
nohup python3.8 form.py &

# Print the process IDs
echo "First script running with PID: $!"
echo "Second script running with PID: $!"
