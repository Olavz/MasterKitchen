#!/bin/python

from datetime import date

weekNumber = date.today().isocalendar()[1]

users = [
  "Sofie",
  "Anders",
  "Martin",
  "Per",
  "Olav",
"Lill",
"Julie",
"Lise",
"Magnus",
]

startWeek = 35
ulen = len(users)
for week in range(startWeek,52):

  print("Week " + str(weekNumber)+ " - "+ users[weekNumber % ulen])
  weekNumber+=1
  
