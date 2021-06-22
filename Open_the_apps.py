import os
import webbrowser
import pyautogui
from time import sleep

braze = 'https://dashboard-03.braze.com/auth?email=daraksha.iram%40glu.com&origin=%2Fdashboard%2Fapp_usage'
singular = 'https://app.singular.net/login?redir=%2F#/dashboard'
EST = 'https://analytics-stream.glu.com/stream'
firebase = 'https://console.firebase.google.com/?hl=en&pli=1'

links = [braze,singular,EST,firebase]

for i in links:
    webbrowser.open_new_tab(i)

    if i == braze:
        sleep(5)
        pyautogui.click(780,539)  # sign-in

    elif i == singular:
        sleep(5)
        pyautogui.click(782,567)   # sign-in

    else:
        pass

os.startfile('C:\\Users\\daraksha.iram\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Slack Technologies Inc\\Slack.lnk')
os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Outlook.lnk')
os.startfile('cmd')
os.startfile('C:\\Users\\daraksha.iram\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Zoom\\Zoom.lnk')
os.startfile('C:\\Users\\daraksha.iram\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk')

