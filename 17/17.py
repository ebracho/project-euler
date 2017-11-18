ones = {
	0: '',
	1: 'one',
	2: 'two',
	3: 'three',
	4: 'four',
	5: 'five',
	6: 'six',
	7: 'seven',
	8: 'eight',
	9: 'nine',
}

teens = {
	0: 'ten',
	1: 'eleven',
	2: 'twelve',
	3: 'thirteen',
	4: 'fourteen',
	5: 'fifteen',
	6: 'sixteen',
	7: 'seventeen',
	8: 'eighteen',
	9: 'nineteen',
}

tens = {
	1: 'ten',
	2: 'twenty',
	3: 'thirty',
	4: 'forty',
	5: 'fifty',
	6: 'sixty',
	7: 'seventy',
	8: 'eighty',
	9: 'ninety',
}

def int_to_english(i):
	if i < 10:
		return ones[i]
	elif i < 20: 
		return teens[i-10]
	elif i < 100:
		return tens[i/10] +  int_to_english(i%10)
	elif i < 1000:
		return ones[i/100] + 'hundred' + ('and' + int_to_english(i%100) if i%100 else '')
		

print(sum(map(len,map(int_to_english,range(1,1000))))) + len('onethousand')

