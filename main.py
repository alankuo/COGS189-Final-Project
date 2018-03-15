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

for line in fileinput.input():
	line = line[:len(line)-1]
	if len(line)==0 or line.isdigit() != True:
		print("Please enter valid input!")
		continue
	number = int(line)
	print("this is output: " + line)
	#time.sleep(1)
	print("Time: " + str(datetime.datetime.now()))
	#time.sleep(1)
	num = random.randrange(10)
	print("Random: " + str(num))
	print("length of output: " + str(len(line)))