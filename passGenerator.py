import random 
import string

def passwordGenerator(N):
	"""
	Generate N range password including numbers, 
	lowercases, uppercases and punctions
	"""
	password = ""
	for i in range(0,N//4):
		#In every iterate 4 chars gonna add so needed to divide by 4 
		password += "".join(random.choice(string.ascii_lowercase)+
			random.choice(string.ascii_uppercase)+
			random.choice(string.digits)+
			random.choice(string.punctuation))
	print(password)
	print(len(password))


if __name__ == '__main__':
	digitsNum = int(input("How many digits gonna be in password??"))
	passwordGenerator(digitsNum)

