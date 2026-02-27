import numpy as np
temps_celsius = np.array([22, 25, 28, 24, 26])
temps_fahrenheit = (temps_celsius * 1.8) + 32
average_fahrengeit = np.mean(temps_fahrenheit)
average_temp = np.mean(temps_celsius)

print(" Celsius: ", temps_celsius)
print("Fahrenheit: ", temps_fahrenheit)
print("Average Celsius: ", average_temp)
print("Average Fahrenheit: ", average_fahrengeit)