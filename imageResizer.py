import cv2

src = cv2.imread('windows-11.jpg', cv2.IMREAD_UNCHANGED)

# percent by which the image is resized
scale_percent = 50

# calculate the 50 percent of original dimensions
width = int(src.shape[1] * scale_percent / 100)
height = int(src.shape[0] * scale_percent / 100)

# dsize
dsize = (width, height)

# resize image
output = cv2.resize(src, dsize)

cv2.imwrite('new_img.jpg', output)