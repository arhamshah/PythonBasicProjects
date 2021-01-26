userInput = input("Enter the Text to generate Acronym:-")
inputList = userInput.split()
accr = ""
for i in inputList:
    accr += i[0].upper()

print(accr)

# Here String entered by user is stored in userInput variable and later using spilt function, stored in inputList(List of Strings)
# While iterating inside inputList[], We select First letter of each word in string and store it in accr variable.
