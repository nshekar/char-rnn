from __future__ import division
import enchant
import os
foldername = "austencv"
d = enchant.Dict("en_US")
score = 0
count = 0
fileList = os.listdir(foldername)
fileList.sort()
for file in fileList:
	count = 0
	score = 0
	if file.endswith(".txt"):
		fileReader = open(foldername  + "/" + file)
		for line in fileReader:
			for word in line.split():
				count += 1
				if (d.check(word)):
					score += 1
		print file, ": ", score, "/", count, ": ", score/count * 100, "%"

