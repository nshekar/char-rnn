import os
foldername = "austencv"
count = 0;
for file in os.listdir(foldername):
    if file.endswith(".t7"):
        os.system("../torch/install/bin/th sample.lua " + foldername + "/" +file+" -gpuid -1 > "+foldername+"/output"+str(count)+".txt")
        count += 1
