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

# State			Frequency range		State of mind
# Delta			0.5Hz–4Hz			Deep sleep
# Theta			4Hz–8Hz				Drowsiness (also first stage of sleep)
# Alpha			8Hz–14Hz			Relaxed but alert
# Beta			14Hz–30Hz			Highly alert and focused

# Morning: 7am - 12pm
# Afternoon: 12pm - 6pm
# Night: 6pm - 11pm
# Midnight 11pm - 3am
# Sleep 3am - 7am

# Preparation
def prepareVal():
	date = str(datetime.datetime.now())
	hour = int(date[11:13])
	minute = int(date[14:16])
	# print("Time: " + str(datetime.datetime.now()))
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
	if hour > 3 and hour <= 7:
		SEED = 25
		tiredness = 5
	return hour, SEED, tiredness

# Old Main Loop
# for line in fileinput.input():
# 	line = line[:len(line)-1]
# 	if len(line)==0 or line.isdigit() != True:
# 		print("Please enter valid input!")
# 		continue
# 	number = int(line)
# 	print("this is output: " + line)
# 	#time.sleep(1)
# 	num = random.randrange(SEED)
# 	print("Random: " + str(num))
# 	print("length of output: " + str(len(line)))

# Main Loop
while True:
	hour, SEED, tiredness = prepareVal()
	num = random.randrange(SEED)
	num2 = random.uniform(0.5, 4.0)
	num2 = float("{0:.2f}".format(num2))
	print("Random: " + str(num))
	print("Random2: " + str(num2))
	print("Tiredness: " + str(tiredness))
	time.sleep(3)
	# print("You are focused!")
	# print("You are tired!")








