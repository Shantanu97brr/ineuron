# Q1.1

class Triangle:
	def __init__(self):
		self.a = int(input("Enter a side length: "))
		self.b = int(input("Enter b side length: "))
		self.c = int(input("Enter c side length: "))
		self.s = (self.a + self.b + self.c) / 2


class AreaOfTraingle(Triangle):
	def area(self):
		ar = ((self.s * (self.s - self.a) * (self.s - self.b) * (self.s - self.c)) ** (0.5))
		return ar


o2 = AreaOfTraingle()
print(o2.area())

# Q1.2

list_of_words = ['Drake', 'NarutoShippuden', 'Shawn', 'Jimmyer', 'Seth']
n = 5
l1 = []


def filter_long_words():
	for word in list_of_words:
		if len(word) > n:
			l1.append(word)


filter_long_words()
print(l1)

# Q2.1

l2 = []


def words_to_integers():
	for word in list_of_words:
		a = len(word)
		l2.append(a)


words_to_integers()
print(l2)

# Q2.2

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
char = str(input('Please Enter a single alphabet: '))


def vowel():
	if char in vowels:
		print('True')
	else:
		print('False')


vowel()

