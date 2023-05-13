import calendar
inputCalendar=[int(item) for item in input().split(' ')]
days_of_week = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
dayofweek=calendar.weekday(inputCalendar[2],inputCalendar[0],inputCalendar[1])
dayofweekstr=days_of_week[dayofweek]
print(dayofweekstr)