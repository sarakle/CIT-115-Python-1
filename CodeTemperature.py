print("Welcome to Sarak's Temperature Converter")

temp = float(input("Enter a temperature: "))
degree = input("Was the temperature in F or C? ")


if degree == "F":
    if temp < 212:
        nCelsius = (5.0/9)*(temp - 32)
        print("The Celsius equivalent is:", round(nCelsius, 1))
    else:
        print("Temp can not be > 212")
elif degree == "C":
    if temp < 100:
        nFahrenheit = (9.0/5.0) * temp + 32
        print("The Fahrenheit equivalent is:", round(nFahrenheit, 1))
    else:
        print("Temp can not be > 100")
else:
    print("You must enter 'F' for Fahrenheit or 'C' for Celsius.")



            
    




