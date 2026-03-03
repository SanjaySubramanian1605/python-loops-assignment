# Name: Sanjay S
# Roll Number:IITP_AIMLTN_2602594
# Assignment: Python Loops & Automation - Subjective Question

print("===== Task 1: Find Maximum and Minimum =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]

max_temp = temperatures[0]
min_temp = temperatures[0]

for num in temperatures:
  if num > max_temp:
    max_temp = num
  if num < min_temp:
    min_temp = num
print("Highest Temperature:", max_temp, "°C")
print("Lowest Temperature:", min_temp, "°C")


print("\n===== Task 2: Count Hot Days =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]


hot_days = 0

for temp in temperatures:
    if temp <= 30:
        continue   # Skip non-hot days
    
    hot_days += 1

print("Hot Days (>30°C):", hot_days)

print("\n===== Task 3: Alert System =====")
temperatures = [28, 32, 35, 40, 31, 33, 30]

hot_days = 0

for day in range(len(temperatures)):
    temp = temperatures[day]
    
    if temp >= 40:
        print("Alert! Extreme temperature", temp, "°C detected on Day", day + 1)
        break
    
    if temp > 30:
        hot_days += 1

print("Hot Days before alert:", hot_days)