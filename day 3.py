# Excersice 2: Good Morning Sir
# Create a python program capable of greeting you with Good Morning, Good Afternoon and Good Evening. Your program should use time module to get the current hour.
import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = int(time.strftime('%H'))
print(timestamp)
timestamp = int(time.strftime('%M'))
print(timestamp)
timestamp = int(time.strftime('%S'))
print(timestamp)
if(timestamp<12):
  print("Good Morning Sir")
elif(timestamp>12 and timestamp<16):
  print("good afternoon sir")
elif(timestamp>16 and timestamp<20):
  print("good evening sir")
else:
  print("good night sir")