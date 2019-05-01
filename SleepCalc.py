import sqlite3
import datetime

dbconn = sqlite3.connect('sleep.db')
c = dbconn.cursor()

c.execute('''SELECT Date, WakeTime, BedOut, BedTime, ApproximateSleepTime, 
             TotalEA FROM SleepCycle ORDER BY date DESC LIMIT 2''')
info = c.fetchall()

RecentDate = info[0][0]
print(RecentDate)

RecentWakeTime = datetime.datetime.strptime("{0} {1}".format(info[0][0],info[0][1]), "%m/%d/%Y %I:%M %p")
RecentBedOut = datetime.datetime.strptime("{0} {1}".format(info[0][0],info[0][2]), "%m/%d/%Y %I:%M %p")
RecentTotalEA = info[0][5]

PriorBedTime = datetime.datetime.strptime("{0} {1}".format(info[1][0],info[1][3]), "%m/%d/%Y %I:%M %p")
PriorApproximateSleepTime = datetime.datetime.strptime("{0} {1}".format(info[1][0],info[1][4]), "%m/%d/%Y %I:%M %p")

def TimeInBedCalc(bt, bo):
    TimeInBed = bo - bt
    TimeInBed = str(TimeInBed)
    print("Time In Bed: {}".format(TimeInBed[0:-3]))
    return TimeInBed[0:-3]


def TimeAsleepCalc(ast, wt, ea):
    TimeAsleep = (wt - ast) - datetime.timedelta(minutes = ea)
    TimeAsleep = str(TimeAsleep)
    print("Time Asleep: {}".format(TimeAsleep[0:-3]))
    return TimeAsleep[0:-3]


TimeInBedCalc(PriorBedTime, RecentBedOut)
TimeAsleepCalc(PriorApproximateSleepTime, RecentWakeTime, RecentTotalEA)

c.execute("SELECT * FROM SleepCycle WHERE date='{0}'".format(RecentDate))


# TODO Do something with this return variable
newvar = c.fetchall()
print(newvar[0])
dbconn.close()
