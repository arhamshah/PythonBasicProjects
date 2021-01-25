userInput = input("Enter Email to retrive Username & Domain Name:-")
userInput = userInput.strip()
if "@" in userInput:
    index = userInput.index("@")
    userName = userInput[:index]
    domainName = userInput[index+1:]
    print(f'Username:-{userName}\nDomain:-{domainName}')
else:
    print("Please input valid Email address !!!")

# Here String entered by user is stored in userInput variable and Strip() trims all whitespaces if any
# We check that if there is "@" in userInput String, If true then we find index of "@" inside the string
# Later we use slicing and derive our desired outputs
