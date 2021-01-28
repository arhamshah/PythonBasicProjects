def convertTemperature(temp, mode):
    if mode == "C":
        answer = (temp - 32)*(5/9)
        return answer
    elif mode == "F":
        answer = (temp * (9/5))+32
        return answer
    else:
        print("Exception Occurred !")


userInput = input("Write Celsius or Fahrenheit to which you want to convert:-")
if userInput.capitalize() == "Celsius":
    userInputTemperature = float(input("Enter Temperature in Fahrenheit:-"))
    result = round(convertTemperature(userInputTemperature, "C"), 2)
    print(f"{result}°C")
elif userInput.capitalize() == "Fahrenheit":
    userInputTemperature = float(input("Enter Temperature in Celsius:-"))
    result = round(convertTemperature(userInputTemperature, "F"), 2)
    print(f"{result}°F").format()
else:
    print("Enter Valid Input")

# Here we first created a function convertTemperature(), where two arguments are the temperature and unit to which it is to be converted
# Later we ask the user about unit they wanted temperature to be and store it in userInput. userInputTemperature variable has the temperature given by the user
# We call the function convertTemperature() and round the result to 2 decimal places
