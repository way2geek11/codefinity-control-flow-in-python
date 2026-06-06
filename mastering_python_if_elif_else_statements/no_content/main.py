exercise_time = 8  # Example value for total exercise time in hours
title = ""

if exercise_time>10:
    title = "Super Achiever"
elif 6<=exercise_time<=10:
    title = "Hard Worker"
elif 3>=exercise_time<6:
    title = "Getting There"
else:
    title = "Needs Improvement"

# Testing
print("Your fitness level:", title)