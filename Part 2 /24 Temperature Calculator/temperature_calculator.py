cel = float(input("Enter the temperature in Celsius : "))

fht_o = (cel * (9 / 5)) + 32

print("The temperature in Fahrenheit is %.2f°F" % (fht_o))

fht = float(input("Enter the temperature in Fahrenheit : "))

cel_o = (fht - 32) * (5 / 9)

print("The temperature in Celsius is %.2f°C" % (cel_o))
