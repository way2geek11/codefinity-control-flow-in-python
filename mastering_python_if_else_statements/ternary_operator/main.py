water_intake = 1.5  # Example value
true_message = "You've met your hydration goal!"
false_message = "Drink more water to reach your goal."

# Using ternary operator to check hydration goal
message = "You've met your hydration goal!" if water_intake>=2 else "Drink more water to reach your goal."

# Testing
print("Hydration Status:", message)