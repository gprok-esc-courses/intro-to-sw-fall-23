# Ask user for a value representing a temperature. 
# Then ask a letter indicating the type,
# C for Celsius or F for Fahrenheit. 
# Then convert if C convert to F 
# [formula: F = (C * 9/5) + 32], 
# or from F to C [formula: C = 5 / 9 * (F - 32)].

temperature = float(input("Give temperature: "))
type = input("Give type (C or F): ")

if type == "C":
    f = temperature * 9 / 5 + 32
    print("Temperature in Fahrenheit:", f)
elif type == "F":
    c = 5 / 9 * (temperature - 32)
    print("Tempreature in Celcius:", c)
else:
    print("Wrong type")
