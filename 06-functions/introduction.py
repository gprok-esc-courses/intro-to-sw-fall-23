
def add(a: int, b: int) -> int:
    x = a + b
    return x 

def fahrenheit_to_celcius(t: float) -> float:
    c = 5 / 9 * (t - 32)
    return c

def celcius_to_fahrenheit(c: float) -> float:
    f = c * 9 / 5 + 32
    return f



total = add(4, 5)

temperature = float(input("Give temperature: "))
type = input("Give type (C or F): ")

if type == "C":
    print(celcius_to_fahrenheit(temperature))
elif type == "F":
    print(fahrenheit_to_celcius(temperature))
else:
    print("Wrong type")