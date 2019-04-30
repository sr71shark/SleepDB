# import datetime
import sqlite3

dbconn = sqlite3.connect("/Users/mwhites/programming/python/SleepLog/sleep.db")

c = dbconn.cursor()

ApproxSleepTime = ""
EveningAwake = ""
TotalEA = ""
WakeTime = ""
Out_of_Bed = ""
Comments = ""
Quality_of_Sleep = ""
AffectingSubstances = ""
Naps = ""
Exercise = ""
SleepAid = ""
WindDown = ""
BedTime = ""

date = raw_input("What date are you logging? MM/DD/YYYY:\t")

am_or_pm = raw_input("Morning or Night:\t")


# Morning questions
if am_or_pm == "Morning":
    ApproxSleepTime = raw_input("About what time did you fall asleep?\t")
    EveningAwake = raw_input("How many times did you wake up for more than 15 minutes?\t")
    TotalEA = raw_input("How many minutes total were you awake?\t")
    WakeTime = raw_input("What time did you wake up for the day?\t")
    Out_of_Bed = raw_input("What time did you get out of bed?\t")
    Comments = raw_input("Comments about last night's sleep? Anything that might have affected it? How do you feel?\t")
    Quality_of_Sleep = raw_input("On a scale of 1-5, what was the quality of your sleep?\t")

# Evening Questions

elif am_or_pm == "Night":
    AffectingSubstances = raw_input("Have you had any Alcohol, Caffeine, Nicotine, or medications today? How much?\t")
    Naps = raw_input("What was the length of any naps you had?\t")
    Exercise = raw_input("how much exercise did you get today? ")
    SleepAid = raw_input("Did you use any type ofd sleep aid tonight? How much?\t")
    WindDown = raw_input("What did you do to wind down? How long before bed?\t")
    BedTime = raw_input("What time did you get into bed?\t")

else:
    print("Please type 'Morning' or 'Night'.\t")


c.execute("""INSERT INTO SleepCycle VALUES('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}',
    '{12}','{13}')""".format(date, ApproxSleepTime, EveningAwake, TotalEA, WakeTime, Out_of_Bed, Comments, Quality_of_Sleep,
    AffectingSubstances, Naps, Exercise, SleepAid, WindDown, BedTime))

dbconn.commit()

dbconn.close()