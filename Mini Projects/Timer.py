import time
a = int(input("Enter the number of seconds you want the timer to run: "))

for x in range(a, 0, -1):
     sec = x%60
     min = int(x / 60) % 60
     hour = int(x / 3600) 
     print(f"{hour:02}:{min:02}:{sec:02}")
     time.sleep(1)
print("TIME'S UPP!!")