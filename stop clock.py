import time
# Time Input
min = int(input("Enter Minutes: "))
sec = int(input("Enter Seconds: "))

# We are Checking for valid Seconds input
if(sec >60):
    print("Seconds cannot be more than 60")
elif(sec == 60):
    sec = 0
    min +=1

# Converting minutes to seconds
sec = min*60 + sec
s = 0

# Running Loop every Seconds
for i in range(sec):
    m = int(i/60)
    s= s + 1
    if(s>= 60):
        m = m + 1
        s = 0
    print(f"{m} Minutes, {s} Seconds")
    time.sleep(1)

print("Time Up")