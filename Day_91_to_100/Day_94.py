#Drnke Water Reminder
#Write a Pythone Program which reminds you of drinking water every houror two. your program can either beep or send desktop notification for secific operationg system

from win11toast import toast
import time

REMINDER_INTERVAL = 10  # 10 seconds

while True:
    toast(
        "💧 Drink Water Reminder",
        "Time to drink water! Stay hydrated 😊",
        duration="short"  # short = 5 sec (Windows limit)
    )
    time.sleep(REMINDER_INTERVAL)
