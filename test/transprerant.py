from PIL import Image
import os

pokemon_ball = 'image/pokemon_ball.png'
ball = Image.open(pokemon_ball)
filename1 = 'image/未命名.png'
bg = Image.open(filename1)
text_img = Image.new('RGBA', (500, 300), (0, 0, 0, 0))
text_img.paste(bg, (0, 0))
text_img.paste(ball, (0, 0), mask=ball)
text_img.save("ball.png", format="png")

# OpenCV轉PIL
# image = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
# PIL轉OpenCV
# img = cv2.cvtColor(numpy.asarray(image), cv2.COLOR_RGB2BGR)
