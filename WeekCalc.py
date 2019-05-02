import sqlite3
import datetime
import xlwings as xw

dbconn = sqlite3.connect('sleep.db')
c = dbconn.cursor()

c.execute('''SELECT Date, WakeTime, BedOut, BedTime, ApproximateSleepTime, 
             TotalEA FROM SleepCycle ORDER BY date DESC LIMIT 14''')
info = c.fetchall()

def convertdatetoweekday(nf):
    year = int(nf[-4:])
    month = int(nf[:2])
    day = int(nf[3:5])
    return datetime.date(year, month, day).strftime("%A")
# print(info)
# print(info[0][0])
for i in range(0, len(info), 1):
    nf = str(info[i][0])
    print(convertdatetoweekday(nf))
    # if convertdatetoweekday(nf) == "Wedneday":

# print(nf)
# print(nf[3:5])
# print type(nf[3:5])



# for i in info:
#     print(convertdatetoweekday(nf))
#     if datetime.datetime.now().strftime("%A") == "Sunday":
#         print("The Stuff")

# dt = datetime.date(year, month, day).isocalendar()[1]
# print("Current Week: {}".format(dt))
# print(datetime.datetime.now().strftime("%A"))
# if datetime.datetime.now().strftime("%A") == "Sunday":
#     print("The Stuff")
# print(datetime.date(2019, 04, 29).isocalendar()[1])

dbconn.close()
