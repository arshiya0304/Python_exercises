import pandas as pd

temps = list(map(float, input("Enter temperatures in Celsius separated by space: ").split()))
celsius_series = pd.Series(temps)

fahrenheit_series = celsius_series * 9/5 + 32

print("\nCelsius Series:")
print(celsius_series)

print("\nFahrenheit Series:")
print(fahrenheit_series)