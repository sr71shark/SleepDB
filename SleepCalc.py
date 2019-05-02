import sqlite3
import datetime
import logging

def TimeInBedCalc(bt, bo):
    TimeInBed = bo - bt
    TimeInBed = str(TimeInBed)
    return TimeInBed[0:-3]


def TimeAsleepCalc(ast, wt, ea):
    TimeAsleep = (wt - ast) - datetime.timedelta(minutes=ea)
    TimeAsleep = str(TimeAsleep)
    return TimeAsleep[0:-3]


dbconn = sqlite3.connect('sleep.db')
c = dbconn.cursor()

c.execute('''SELECT Date, WakeTime, BedOut, BedTime, ApproximateSleepTime, 
             TotalEA FROM SleepCycle ORDER BY date DESC LIMIT 2''')
info = c.fetchall()
try:
    RecentDate = info[0][0]

    RecentWakeTime = datetime.datetime.strptime("{0} {1}".format(info[0][0], info[0][1]), "%m/%d/%Y %I:%M %p")
    RecentBedOut = datetime.datetime.strptime("{0} {1}".format(info[0][0], info[0][2]), "%m/%d/%Y %I:%M %p")
    RecentTotalEA = info[0][5]

    PriorBedTime = datetime.datetime.strptime("{0} {1}".format(info[1][0], info[1][3]), "%m/%d/%Y %I:%M %p")
    PriorApproximateSleepTime = datetime.datetime.strptime("{0} {1}".format(info[1][0], info[1][4]), "%m/%d/%Y %I:%M %p")

    tibc = TimeInBedCalc(PriorBedTime, RecentBedOut)
    tac = TimeAsleepCalc(PriorApproximateSleepTime, RecentWakeTime, RecentTotalEA)

    c.execute("SELECT * FROM SleepCycle WHERE date='{0}'".format(RecentDate))

    # TODO Assuming update the current database with current date.
    c.execute('UPDATE SleepCycle SET TimeInBed="{0}", TimeAsleep="{1}" WHERE date="{2}"'.format(tibc, tac, RecentDate))
    dbconn.commit()
except ValueError as e:
    print("Error found at:\t \033[91m{}\033[0m".format(e))
    print("Data missing from the database to do the calculations.")
except Exception:
    logging.basicConfig(level=logging.DEBUG, filename='errors.log')
    logging.exception("Exception Occurred:")

dbconn.close()
