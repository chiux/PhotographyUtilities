# Focal length analyzer
# 2023.12.02
# Author: Yang Hsu

import PIL.Image
import os
import matplotlib.pyplot as plt

path = "D://Yang//photo//2022winterOB//new//"

dir_list = os.listdir(path)
# print(dir_list)

FL = {}
count = len(dir_list)

# 37386  focal length

for files in dir_list:
    img = PIL.Image.open(path+files)
    exif_data = img._getexif()
    focal_length = exif_data[37386]
    if focal_length not in FL:
        FL[focal_length] = 0
    else:
        FL[focal_length] = FL[focal_length] + 1



FLs = list(FL.keys())
nums = list(FL.values())

fig = plt.figure(figsize = (10, 5))

plt.bar(FLs, nums, color ='maroon', 
        width = 0.4)
 
plt.xlabel("Focal Length")
plt.ylabel("Num of photos")
plt.title("Focal Length used")
plt.show()