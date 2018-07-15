from PIL import Image, ImageDraw, ImageFont

image = Image.open('./bmw_for_life.jpg')
width, height = image.size

draw = ImageDraw.Draw(image)
text = 'Emmanuel Jimenez For Proveyourworth Level 3'

font = ImageFont.truetype('./Roboto-Regular.ttf', 28)
textWidth, textHeight = draw.textsize(text, font)

margin = 5
x = width - textWidth - margin
y = height - textHeight - margin

draw.text((x,y), text, font=font)

image.save('watermarkedproveyourworth.jpg')