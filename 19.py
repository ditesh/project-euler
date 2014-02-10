import euler

j=0
i = 1

months = [31] * 12
months[3] = 30
months[5] = 30
months[8] = 30
months[10] = 30

for year in range(1900,2001):

	months[1] = 28

	if year % 4 == 0 and year != 1900:
		months[1] = 29

	for month in range(0, 12):

		for day in range(0, months[month]):

			if i > 7:
				i = 1

			if year >= 1901 and i == 7 and day == 0:
				j += 1

			i += 1

print j
