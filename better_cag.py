import random, string
fullstr = ""
length = random.randint(16,64)
for i in range(length):
	if random.randint(1, 2) == 1:
		fullstr += random.choice(string.ascii_uppercase)
	else:
		fullstr += random.choice(string.ascii_uppercase)
	if random.randint(1, 10) == 2:
		fullstr += random.choice(string.digits)
	if random.randint(1, 10) == 5:
		fullstr += random.choice(".=-_,")
print("Address: "+fullstr)
