import fileinput
import time
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import datetime
import random

#plt.switch_backend('Qt4Agg')
#print(plt.get_backend())
# Fs = 8000
# f = 5
# sample = 8000
# x = np.arange(sample)
# y = np.sin(2 * np.pi * f * x / Fs)
# plt.ion()
# plt.plot(x, y)
# plt.xlabel('sample(n)')
# plt.ylabel('voltage(V)')
# plt.show()
# plt.pause(3)
# plt.close(plt.figure())
#input("Hit Enter To Close")
#plt.close()

# Morning: 7am - 12pm
# Afternoon: 12pm - 6pm
# Night: 6pm - 11pm
# Midnight 11pm - 3am
# Sleep 3am - 7am

# Preparation
date = str(datetime.datetime.now())
hour = int(date[11:13])
minute = int(date[14:16])
print("Time: " + str(datetime.datetime.now()))
print("Hour: " + str(hour))
print("Minute: " + str(minute))
SEED = 1
tiredness = 1
# Student 1
# Morning: most energetic
# Afternoon: energetic
# Night: less energetic
# Midnight: tired
if hour > 7 and hour <= 12:
	SEED = 10
	tiredness = 1
if hour > 12 and hour <= 18:
	SEED = 15
	tiredness = 2
if hour > 18 and hour <= 23:
	SEED = 20
	tiredness = 3
if hour > 23 or hour <= 3:
	SEED = 25
	tiredness = 4
if hour > 3 or hour <= 7:
	SEED = 25
	tiredness = 5

# Student 2
# Morning: most energetic
# Afternoon: energetic
# Night: less energetic
# Midnight: tired
if hour > 7 and hour <= 12:
	SEED = 10
	tiredness = 1
if hour > 12 and hour <= 18:
	SEED = 15
	tiredness = 2
if hour > 18 and hour <= 23:
	SEED = 20
	tiredness = 3
if hour > 23 or hour <= 3:
	SEED = 25
	tiredness = 4
if hour > 3 or hour <= 7:
	SEED = 25
	tiredness = 5


# Main Loop
for line in fileinput.input():
	line = line[:len(line)-1]
	if len(line)==0 or line.isdigit() != True:
		print("Please enter valid input!")
		continue
	number = int(line)
	print("this is output: " + line)
	#time.sleep(1)
	num = random.randrange(SEED)
	print("Random: " + str(num))
	print("length of output: " + str(len(line)))













