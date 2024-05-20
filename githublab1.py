# Prompt user to enter the number of minutes

num = int(input("Please enter the number of minutes: "))

# Compute by converting the number of minutes into days
totalDay = num / (60 * 24)

# Calculate the total years using total days
totalYear = totalDay / 365

# Calculate the total remain days from the years
remain = totalDay % 365

# Print Output
print(f"{num} minutes is approximately {int(totalYear)} years and {int(remain)} days")

