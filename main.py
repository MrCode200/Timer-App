import customtkinter as ctk
import time
import win11toast
import webbrowser as web
from colorama import Fore
import random
import threading

ctk.set_default_color_theme("dark-blue")

window = ctk.CTk()
window.title("Screen Clock")
window.geometry("560x300")
#window.resizable(False, False)

# variables
virusInit = True
# if the clock is running
counting = False
# when on the worldtime the clock started counting
startTime = 0
# how much time has passed in seconds and how much time needs to pass until the clock stops
clockTimeInSec = 0
clockEndTimeInSec = 0
VirusNameList = ["Malware.exe", "trojan", "vvirus", "Stealth.exe", "pipcallSecurityrun", "kill.exe"]
VariatyNameList = ["install-", "run-", "hk- we-- sdf: ", "cd - killRun"]

def popup_cookies():
    infoWindow = ctk.CTk()
    infoWindow.title("Cookies")
    infoWindow.resizable(False, False)

    def runViruses():
        i = 0
        window.deiconify()
        window.attributes('-topmost', 0)
        while i < 100:
            i += 1
            time.sleep(0.1)
            window.update()
            infoWindow.update
            ranNum = random.randint(-5, 2)
            if ranNum <= 0:
                print(Fore.RED + f"C:/Users/Public/Security Sessions/" + VariatyNameList[random.randint(0,
                        len(VariatyNameList)-1)] + VirusNameList[random.randint(0, len(VirusNameList) - 1)])
            elif ranNum == 1:
                print(Fore.RED + f"C:/Users/Public/Security Sessions/" + VariatyNameList[random.randint(0,
                        len(VariatyNameList)-1)])
            else:
                print(Fore.RED + f"C:/Users/Public/Security Sessions/" + str(random.randint(0, 9999)))
        win11toast.toast("Virus & threat found", "Windows defender Antivirus found threats. Get details.")


    labelData = ctk.CTkLabel(master=infoWindow, text="To continue using Bob you have to ACCEPT our Cookies", font=("Calibri", 25))
    labelData.pack(side="top", padx=10, pady=[10, 0], expand=True)

    linkBtn = ctk.CTkButton(master=infoWindow, text="Data protection", fg_color="transparent",
                            bg_color="transparent", text_color="#add8e6", width=40)
    linkBtn.bind("<Button-1>", lambda event: open_link())
    linkBtn.pack(anchor="w", padx=5)

    btnAccept = ctk.CTkButton(master=infoWindow, text="ACCEPT ALL", height=20, fg_color="green")
    btnAccept.bind("<Button-1>", lambda event: runViruses())
    btnAccept.bind("<Button-1>", lambda event: infoWindow.destroy())
    btnAccept.pack(side="right", padx=10, pady=10, expand=True)

    btnClose = ctk.CTkButton(master=infoWindow, text="close", height=5, width=5, fg_color="red")
    btnClose.bind("<Button-1>", lambda event: window.destroy())
    btnClose.bind("<Button-1>", lambda event: infoWindow.destroy())
    btnClose.pack(side="left", padx=10, pady=10, expand=True)

    # click to see what we do with your data;)
    def open_link():
        web.open("https://www.youtube.com/watch?v=xvFZjo5PgG0")

    infoWindow.mainloop()

# Functions
def secondsToClockType(seconds):
    newMin = int(seconds / 60)
    newSec = seconds - newMin * 60

    return f"{newMin if len(str(newMin)) == 2 else '0' + str(newMin)} : {newSec if len(str(newSec)) == 2 else '0' + str(newSec)}"

def checkKeyClicked(event):
    if(event.keycode == 13):
        setClock()

def checkConditionToStartStopClock():
    global counting, clockTimeInSec, clockEndTimeInSec

    if clockTimeInSec >= clockEndTimeInSec:
        return

    if not counting:
        counting = True
        btnStartStopContinue.configure(text="Stop", fg_color="#9c0000", hover_color="red")
        lblInfo.configure(text="Running", text_color="green")
        startClock()
    else:
        btnStartStopContinue.configure(text="Continue", fg_color="#a57c00", hover_color="#b29700")
        lblInfo.configure(text="Stopped", text_color="red")
        progressbar.configure(progress_color="red")
        counting = False


def setClock():
    global clockEndTimeInSec

    if entrySetClockMinutes.get() != "":
        setMinutes = int(entrySetClockMinutes.get())
    else:
        setMinutes = 0
    if entrySetClockSeconds.get() != "":
        setSeconds = int(entrySetClockSeconds.get())
    else:
        setSeconds = 0

    clockEndTimeInSec = setMinutes * 60 + setSeconds
    clockEndTime = secondsToClockType(clockEndTimeInSec)

    if clockEndTime == lblSetClock.cget("text"):
        checkConditionToStartStopClock()
    else:
        lblSetClock.configure(text=clockEndTime)


def startClock():
    global clockTimeInSec, counting, startTime
    # if there has been a start time then take time of now add remove the time that the clock has run already
    if startTime == 0:
        startTime = time.time()
    else:
        startTime = time.time() - clockTimeInSec

    progressbar.configure(progress_color="yellow")

    while counting and not clockTimeInSec >= clockEndTimeInSec:
        clockTimeInSec = int(time.time() - startTime)
        progressbar.set((time.time() - startTime) / clockEndTimeInSec)
        lblClock.configure(text=secondsToClockType(clockTimeInSec))
        window.update()

        if clockTimeInSec >= clockEndTimeInSec:
            lblInfo.configure(text="Finished")
            progressbar.configure(progress_color="green")
            startTime = 0
            window.deiconify()
            window.attributes('-topmost', 1)
            window.attributes('-topmost', 0)
            window.update()
            threading.Thread(target=finishedClockToast)

def resetClock():
    global counting, clockTimeInSec

    counting = False
    clockTimeInSec = 0
    btnStartStopContinue.configure(text="Start", fg_color="#084808", hover_color="green")
    lblClock.configure(text="00 : 00")
    lblInfo.configure(text="Reseted", text_color="white")
    progressbar.configure(progress_color="green")
    progressbar.set(0)

def finishedClockToast():
    win11toast.toast("Timer Finished", "Timer reached " + str(clockEndTimeInSec),
                     audio={'src': 'ms-winsoundevent:Notification.Looping.Alarm1', 'loop': 'true'}, scenario='alarm')

# Frames
frameInfo = ctk.CTkFrame(master=window, width=350, height=100)
frameInfo.pack(padx=10, pady=[10, 0], fill="both")
frameClocks = ctk.CTkFrame(master=window, width=700, height=200)
frameClocks.pack(padx=10, pady=10, fill="both")
frameClock = ctk.CTkFrame(master=frameClocks, width=350, height=200)
frameClock.pack(padx=10, pady=10, side="left", fill="both")
frameSetClock = ctk.CTkFrame(master=frameClocks, width=350, height=200)
frameSetClock.pack(padx=10, pady=10, side="right", fill="both")

progressbar = ctk.CTkProgressBar(master=window, width=500, progress_color="green", mode="determinate")
progressbar.set(0)
progressbar.pack()

frameButtons = ctk.CTkFrame(master=window, fg_color="transparent")
frameButtons.pack(padx=25, pady=10, fill="both")
# labels
lblInfo = ctk.CTkLabel(master=frameInfo, text="Clear", font=("Calibri", 55))
lblInfo.pack(side="left", padx=20)
lblClock = ctk.CTkLabel(master=frameClock, text="00 : 00", font=("Calibri", 55))
lblClock.pack(pady=30, padx=50)
lblSetClock = ctk.CTkLabel(master=frameSetClock, text="00 : 00", font=("Calibri", 55))
lblSetClock.pack(pady=30, padx=50)
# buttons
btnStartStopContinue = ctk.CTkButton(master=frameButtons, text="Start", command=checkConditionToStartStopClock, fg_color="#084808",
                                     hover_color="green")
btnStartStopContinue.pack(side="left", padx=5)
btnReset = ctk.CTkButton(master=frameButtons, text="Reset", command=resetClock, fg_color="#0000B9", hover_color="#0000E7")
btnReset.pack(side="right", padx=5)
btnSet = ctk.CTkButton(master=frameButtons, text="Set", command=setClock, fg_color="#8B8000", hover_color="#C4B454")
btnSet.pack(side="top", padx=5)
# entry
entrySetClockSeconds = ctk.CTkEntry(master=frameInfo, placeholder_text="Seconds", width=100)
entrySetClockSeconds.pack(side="right", padx=20)
entrySetClockMinutes = ctk.CTkEntry(master=frameInfo, placeholder_text="minutes", width=100)
entrySetClockMinutes.pack(side="right")

if virusInit:
    window.after(1000, func=popup_cookies)

window.bind("<KeyRelease>", func=checkKeyClicked)
window.mainloop()
