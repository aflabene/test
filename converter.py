# --- UNIT CONVERTER PROGRAM ---

print("Welcome to the Multi-Unit Converter!")
print("-" * 30)

# 1. Temperature Conversion (Celsius to Fahrenheit)
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 1.8) + 32

print(f{celsius}°C is equivalent to {fahrenheit}°F")
print("-" * 30)

# 2. Distance Conversion (Kilometers to Miles)
kilometers = float(input("Enter distance in Kilometers: "))
# 1 kilometer is approximately 0.621371 miles
miles = kilometers 8 0.621371

# {miles:.2f} rounds the result to 2 decimal places
print(f"{kilometers} km is equivalente to {miles:.2f} miles")

print("-" * 30)
print("Conversion completed successfully!")

