from PIL import Image

img = Image.open("DSC04371.jpg")
print(img.size)
x = img.size[0]
y = img.size[1]
print(x)
print(y)
grid_size = (int)(x/3)
y_num = (int)(y/grid_size)
print(3, y_num)

count = 3*y_num
for j in range(y_num):
    for i in range(3):
        start_x = i*grid_size
        start_y = j*grid_size
        end_x = (i+1)*grid_size - 1
        end_y = (j+1)*grid_size - 1
        # print(start_x, start_y, end_x, end_y)
        new_img = img.crop( (start_x, start_y, end_x, end_y) )
        new_img.save(str(count) + ".jpg")
        count = count - 1

