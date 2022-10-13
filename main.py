TemperatureType = str(input("Enter Temperature Type: C or F: "))

if  TemperatureType.upper() == 'F':
    F = float(input("Enter Temperature in Fahrenheit: "))
    Celsius = (F - 32) * 5 / 9
    print(Celsius)

elif TemperatureType.upper() == 'C':
    C = float(input("Enter Temperature in Celsius: "))
    Fahrenheit = (C * 9 / 5) + 32
    print(Fahrenheit)


else:
    print("Try Again, Something is Wrong!")
