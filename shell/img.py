from PIL import Image

img = Image.open('image.jpg')
watermark = Image.open('watermark.png')

# img.paste(watermark, (round(img.size[0]/2)-150, round(img.size[1]/2)-200),  watermark)
# img.save("img_with_watermark.png")
# print(img.size[0]/2, ' ', img.size[1]/2)
# print(img.size[0], ' ', img.size[1])
#
# im = Image.open(fullname)
img.transpose(Image.ROTATE_90).save('image.jpg')