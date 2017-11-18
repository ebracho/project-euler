months = [31,28,31,30,31,30,31,31,30,31,30,31]
day = 1
sundays = 0
for i in range(1900,2001):
	for month in months:
		month = month + ((month == 28) and (i%4 == 0) and not (i%400 == 0))
		day += month
		print(day%7
		sundays += (day%7) == 6
print(sundays)
