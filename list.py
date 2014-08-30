#! /usr/bin/python
print 'Content-type: text/html\n'
print '<style>.selected { color:#C30; font-weight:bold; }</style>'

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
  if week == weekNumber:
    print("<span class='selected'>Week " + str(week)+ " - "+ users[week % ulen] + "</span></br>")
  else:
    print("<span>Week " + str(week)+ " - "+ users[week % ulen] + "</span></br>")