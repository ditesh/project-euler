# Can't seem to get right answer
import euler

suma = []
ilen = 0
numbers = {}
numbers["1"] = "one"
numbers["2"] = "two"
numbers["3"] = "three"
numbers["4"] = "four"
numbers["5"] = "five"
numbers["6"] = "six"
numbers["7"] = "seven"
numbers["8"] = "eight"
numbers["9"] = "nine"
numbers["10"] = "ten"
numbers["11"] = "eleven"
numbers["12"] = "twelve"
numbers["13"] = "thirteen"
numbers["14"] = "fourteen"
numbers["15"] = "fifteen"
numbers["16"] = "sixteen"
numbers["17"] = "seventeen"
numbers["18"] = "eighteen"
numbers["19"] = "nineteen"
numbers["20"] = "twenty"
numbers["30"] = "thirty"
numbers["40"] = "forty"
numbers["50"] = "fifty"
numbers["60"] = "sixty"
numbers["70"] = "seventy"
numbers["80"] = "eighty"
numbers["90"] = "ninety"
numbers["1000"] = "onethousand"
numbers["00"] = ""
numbers["0"] = ""
keys = numbers.keys()

for i in range(1, 1001):

	istr = str(i)
	digits = euler.digits(i)

	if  i <= 20:
		suma.append(len(numbers[istr]))
		continue

	elif digits == 2:

		if istr in keys:
			suma.append(len(numbers[istr]))
			continue

		else:
			suma.append(len(numbers[istr[0]+'0']) + len(numbers[istr[1]]))
			continue

	elif digits == 4:
		suma.append(len(numbers[istr]))
		continue

	else:
		tmp = len(numbers[istr[0]]) + 7

		if i % 100 != 0:
			tmp += 3

			try: 
				tmp += len(numbers[istr[1:]])

			except:
				tmp += len(numbers[istr[1]+'0'])
				tmp += len(numbers[istr[2]])

		suma.append(tmp)
		continue
i=0
for number in suma:
	i += 1
	print str(i) + ", " + str(number)

print sum(suma)
