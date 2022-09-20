"""
Pillow imported as PIL is an image processing module 
manipulate photos with filters or size and even format

""" 
from PIL import Image, ImageFilter


# open an image from a folder.  use or convert to .png files if planning on using filters
img = Image.open('pics/valley.jpg')

# Functions that will give you info about the photo
# 
print(img.size) # this gives size of photo
print(img.format) # this gives the format of photo
print(img.mode) # this gives the color mode of photo
# print(dir(img)) # gives us the all the available methods for use. check docs for more info

# Converts image to a different format. ie.. this example is greyscale
filtered = img.convert('L')

# This uses tools from ImageFilter to add filters such as blur, sharpen, smoothe etc. check docs
filtered = img.filter(ImageFilter.SMOOTH)
# Saves pic and sets image type by using the .save() function
filtered.save('grey.png', 'png')

# Rotate pics using .rotate
crooked = img.rotate(0)
crooked.save('grey.png', 'png')

# Resize an image using the .resize()
resize = img.resize(200,400)
resize.save('grey.png', 'png')

# Cropping a pic using 4 points of the pic
box = (100,100,300,300) # size of crop window
region = img.crop(box)
region.save('grey.png', 'png')

# Create a thumbnail using the .thumbnail(()) thumbnail must use double parenthesis
img.thumbnail((200,200))
img.save('thumbnail.jpg', 'jpg')

# To view the pic in a window use the .show()
# img.show()
filtered.show()