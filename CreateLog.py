import sqlite3


dbconn = sqlite3.connect("sleep.db")
c = dbconn.cursor()

c.execute("""CREATE TABLE SleepCycle (Date datetime_int, ApproximateSleepTime timestamp, EveningAwake int, TotalEA int, 
WakeTime datetime_int, BedOut datetime_int, Comments text, SleepQual int, SubsAffect text, naps int, Exercise text, 
WindDown text, sleepAid text, BedTime datetime_int)""")

dbconn.commit()
dbconn.close()

