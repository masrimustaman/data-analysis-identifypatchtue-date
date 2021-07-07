import calendar

c = calendar.Calendar()
year = 2021
day = 1

for month in range(1, 13):
    secondLastTues = list(filter(lambda d:d[3] == day and d[1] == month, 
                                 c.itermonthdays4(year, month)))[1]
    print(secondLastTues)