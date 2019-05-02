import os
import sys
import sqlite3
import datetime
import xlwings as xw

dbconn = sqlite3.connect('sleep.db')
c = dbconn.cursor()

c.execute('''SELECT * FROM SleepCycle ORDER BY date DESC LIMIT 7''')
info = c.fetchall()
wb = xw.Book('SleepDiaryTemplate.xlsx')
sht = wb.sheets['Sheet1']
alpha = 'BCDEFGHIJKLMNOPQRSTUVWXYZ'


def convertdatetoweekday(nf):
    year = int(nf[-4:])
    month = int(nf[:2])
    day = int(nf[3:5])
    return datetime.date(year, month, day).strftime("%A")


for i in range(0, len(info), 1):
    nf = str(info[i][0])
    sht.range('{}1'.format(alpha[i])).value = info[i][0]
    sht.range('{}2'.format(alpha[i])).value = info[i][8]
    sht.range('{}3'.format(alpha[i])).value = info[i][9]
    sht.range('{}4'.format(alpha[i])).value = info[i][10]
    sht.range('{}5'.format(alpha[i])).value = info[i][11]
    sht.range('{}6'.format(alpha[i])).value = info[i][12]
    sht.range('{}7'.format(alpha[i])).value = info[i][13]
    sht.range('{}8'.format(alpha[i])).value = info[i][14]
    sht.range('{}9'.format(alpha[i])).value = info[i][3]
    sht.range('{}10'.format(alpha[i])).value = info[i][4]
    sht.range('{}11'.format(alpha[i])).value = info[i][5]
    sht.range('{}12'.format(alpha[i])).value = info[i][6]
    sht.range('{}13'.format(alpha[i])).value = info[i][7]
    sht.range('{}14'.format(alpha[i])).value = info[i][14]
    sht.range('{}15'.format(alpha[i])).value = info[i][15]
if sys.platform == 'win32':
    wb.save(os.getcwd() + r'\Excel-Files\{}.xlsx'.format(datetime.datetime.now().strftime('%m-%d-%Y')))
else:
    wb.save(os.getcwd() + '/Excel-Files/{}.xlsx'.format(datetime.datetime.now().strftime('%m-%d-%Y')))
wb.close()
# print(convertdatetoweekday(nf))
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
