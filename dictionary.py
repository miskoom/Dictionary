import json
from difflib import get_close_matches


#Loading the json data as python dictionary
data = json.load(open('data.json'))

#Function for retriving definition
def retrive_definition(word):
	word = word.lower()

	#Check for non existing words
	if word in data:
		return data[word]
	elif word.title() in data:
		return data[word.title()]
	elif word.upper() in data:
		return data[word.upper()]
	elif len(get_close_matches(word, data.keys())) > 0:
		action = f"input('Did you mean {get_close_matches(word, data.keys())}' instead? [y, or no]: )."

		#-- If the answers is yes, retrive definition of suggested word
		if (action == 'y'):
			return data[get_close_matches(word, data.keys())[0]]
		elif (action == 'n'):
			return ("The word doesn't exist, yet." )
		else:
			return ("We don't understand your entry. Apologies.")

#Input from the user
word_user = input("Enter a word: ")

#Retrive the definition using function and print the result
output = retrive_definition(word_user)

#If a word has more than one definition, print them recursively
if type(output) == list:
	for item in output:
		print("-", item)
	else:
		print("-", output)