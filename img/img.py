from PIL import Image

# 打开图像
image = Image.open('1.jpg')
#image.show()


# 图像属性
print(f'{image.format} , {image.size}, {image.mode}')


# 裁剪
rect = 80, 20, 310, 360
# image.crop(rect).show()


# 缩略图
size = 128, 128
image.thumbnail(size)
image.show()
