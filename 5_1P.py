from tkinter import *
import tkinter.font 
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

# LEDs setup
ledBlue = LED(17)
ledRed = LED(27)
ledYellow = LED(22)

# Window Setup
win = Tk()
win.title("3 RADIO LED")
myFont = tkinter.font.Font(family='Helvetica', size=12, weight="bold")

# Using a single variable to control the radio buttons
led_control = StringVar(value="None")

def updateLEDs():
    if led_control.get() == "Blue":
        ledBlue.on()
        ledRed.off()
        ledYellow.off()
    elif led_control.get() == "Red":
        ledBlue.off()
        ledRed.on()
        ledYellow.off()
    elif led_control.get() == "Yellow":
        ledBlue.off()
        ledRed.off()
        ledYellow.on()
    else:
        ledBlue.off()
        ledRed.off()
        ledYellow.off()

def close():
    ledBlue.off()
    ledRed.off()
    ledYellow.off()
    RPi.GPIO.cleanup()
    win.destroy()

# Radio Buttons
blueButton = Radiobutton(win, text="Turn Blue LED On", variable=led_control, value="Blue", command=updateLEDs, font=myFont, bg='blue', height=1, width=24)
redButton = Radiobutton(win, text="Turn Red LED On", variable=led_control, value="Red", command=updateLEDs, font=myFont, bg='red', height=1, width=24)
yellowButton = Radiobutton(win, text="Turn Yellow LED On", variable=led_control, value="Yellow", command=updateLEDs, font=myFont, bg='yellow', height=1, width=24)
exitButton = Button(win, text="Exit", font=myFont, command=close, bg='black', height=1, width=10)

# Button layout
blueButton.grid(row=0, column=0)
redButton.grid(row=1, column=0)
yellowButton.grid(row=2, column=0)
exitButton.grid(row=3, column=0)

win.mainloop()
