import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Celsius to Kelvin using a lambda function
celsius_to_kelvin = lambda c: c + 273.15

# Step 2: Sample list of Celsius temperatures
celsius_values = list(range(-20, 41, 10))  # From -20°C to 40°C

# Step 3: Convert Celsius to Kelvin using the lambda
kelvin_values = list(map(celsius_to_kelvin, celsius_values))

# Step 4: Create a pandas DataFrame (tabular format)
df = pd.DataFrame({
    'Celsius (°C)': celsius_values,
    'Kelvin (K)': kelvin_values
})

# Step 5: Display the DataFrame
print(df)

# Step 6: Plotting the data
plt.plot(df['Celsius (°C)'], df['Kelvin (K)'], marker='o', linestyle='-')
plt.title("Celsius to Kelvin Conversion")
plt.xlabel("Temperature in Celsius (°C)")
plt.ylabel("Temperature in Kelvin (K)")
plt.grid(True)
plt.show()
