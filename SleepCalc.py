import sqlite3
import datetime

#dbconn = sqlite3.connect("/Users/mwhites/programming/python/SleepLog/sleep.db")
dbconn = sqlite3.connect('C:\Users\Andrew\Documents\Programming\Python\SleepDB\sleep.db')
c = dbconn.cursor()
# dateOne = '04/26/2019'
# dateTwo = '04/24/2019'

c.execute('''SELECT Date, WakeTime, BedOut, BedTime, ApproximateSleepTime, 
                    TotalEA FROM SleepCycle ORDER BY date DESC LIMIT 2''')
info = c.fetchall()

dbconn.close()

# print(info[0])
# print(info[1])

print("Here is the Info: " + info[0][0])

# RecentDate = datetime.datetime.strptime("{0} {1}".format(info[0][0]))
# print(RecentDate)
RecentWakeTime = datetime.datetime.strptime("{0} {1}", "%m/%d/%Y %I:%M %p")#.format(info[0][0],info[0][1]))
RecentBedOut = datetime.datetime.strptime("{0} {1}".format(info[0][0],info[0][2]), "%m/%d/%Y %I:%M %p")
RecentTotalEA = info[0][5]

# print(RecentWakeTime)
# print(RecentBedOut)
# print(RecentTotalEA)

PriorBedTime = datetime.datetime.strptime("{0} {1}".format(info[1][0],info[1][3]), "%m/%d/%Y %I:%M %p")
PriorApproximateSleepTime = datetime.datetime.strptime("{0} {1}".format(info[1][0],info[1][4]), "%m/%d/%Y %I:%M %p")

# print(PriorBedTime)
# print(PriorApproximateSleepTime)

def TimeInBedCalc(bt, bo):
    TimeInBed = bo - bt
    TimeInBed = str(TimeInBed)
    #print(TimeInBed[0:-3])
    return TimeInBed[0:-3]


def TimeAsleepCalc(ast, wt, ea):
    TimeAsleep = (wt - ast) - datetime.timedelta(minutes = ea)
    TimeAsleep = str(TimeAsleep)
    #print(TimeAsleep[0:-3])
    return TimeAsleep[0:-3]


TimeInBedCalc(PriorBedTime, RecentBedOut)
TimeAsleepCalc(PriorApproximateSleepTime, RecentWakeTime, RecentTotalEA)

#x = TimeAsleepCalc(PriorApproximateSleepTime, RecentWakeTime, RecentTotalEA)
#print("x=: " + x)

# c.execute("SELECT Date From SeleepCycle WHERE  ")