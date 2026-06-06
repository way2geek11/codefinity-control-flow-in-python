heart_rate = 135
zone = ""

if heart_rate >= 150:
    zone = "Max Zone"
elif 100 <=heart_rate < 150:
    zone = "Cardio Zone"
elif 60 <= heart_rate < 100:
    zone = "Fat-Burning Zone"
else:
    zone = "Resting Zone"

# Testing
print("Your heart rate level is:", zone)