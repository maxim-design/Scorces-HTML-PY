echo off
python initialize.py
start "Flask" /min cmd /k "python Leaderboard.py"
start "Flask" /min cmd /k "python form.py"
start http://127.0.0.1:23789/
rem for /f "tokens=2 delims=," %%a in ('tasklist /fi "imagename eq cmd.exe" /v /fo:csv /nh ^| findstr /r /c:".*Flask[^,]*$" ') do taskkill /pid %%a
