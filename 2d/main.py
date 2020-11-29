import cv2
import numpy as np
from PIL import Image

# if __name__ == '__main__':
# print("opencv main")

# 最大框框+它的中心
max_x = 0
max_y = 0
max_w = 0
max_h = 0
center_x = 320
center_y = 240

# # 神奇寶貝球
# pokemon_ball = 'image/pokemon_ball.png'
# ball = Image.open(pokemon_ball)
# ball = ball.resize((64, 64))

# # 皮卡丘耳朵
# pikachu_ear = 'image/ear.png'
# ear = Image.open(pikachu_ear)


faceCascade = cv2.CascadeClassifier(
    "./haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
cap.set(3, 640)   # 寬
cap.set(4, 480)   # 高
cap.set(10, 100)  # 亮度

while True:
    _x = 0
    _y = 0
    _w = 0
    _h = 0

    # 神奇寶貝球
    pokemon_ball = 'image/pokemon_ball.png'
    ball = Image.open(pokemon_ball)
    ball = ball.resize((100, 100))

    # 皮卡丘耳朵
    pikachu_ear = 'image/ear.png'
    ear = Image.open(pikachu_ear)

    # Read = Grab + Retrieve + Buffer (Block diagram)
    success, frame = cap.retrieve(cap.grab())
    # print(success)
    frame = cv2.flip(frame, 1)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # blurred = cv2.GaussianBlur(gray, (11, 11), 0)
    # binary = cv2.Canny(blurred, 20, 160)

    faces = faceCascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        if w * h > _w * _h:
            _x = x
            _y = y
            _w = w
            _h = h

    if _w * _h > 15000:
        max_x = _x
        max_y = _y
        max_w = _w
        max_h = _h
        center_x = max_x + max_w / 2
        center_y = max_y + max_h / 2
    # print(self.max_w * self.max_h)  # 臉的框框大小

    # webcam畫面
    frame = cv2.rectangle(
        frame, (max_x, max_y), (max_x+max_w, max_y+max_h), (255, 0, 0), 2)
    # frame = cv2.rectangle(
    #     frame, (int(center_x)-5, int(center_y)-5), (int(center_x)+5, int(center_y)+5), (255, 0, 0), -1)  # 中點
    frame = cv2.rectangle(frame, (max_x, max_y), (max_x+max_w,
                                                  max_y+20), (0, 0, 255), -1)  # 頭頂

    # 分數
    cv2.putText(frame, "score: ", (10, 25),
                cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)

    # OpenCV轉PIL
    frame = Image.fromarray(cv2.cvtColor(
        frame, cv2.COLOR_BGR2RGB))

    # 神奇寶貝球
    compose = Image.new('RGBA', (640, 480), (0, 0, 0, 0))
    compose.paste(frame, (0, 0))
    compose.paste(ball, (0, 0), mask=ball)

    # 耳朵
    ear = ear.resize(
        (int(max_w * 2), int(max_w * 2 / 851 * 475)), Image.ANTIALIAS)
    ear_x = int(max_x - ear.size[1] * 0.15)
    ear_y = max_y - ear.size[1]
    if(ear_y >= 0):
        compose.paste(ear, (ear_x, ear_y), mask=ear)

    # PIL轉OpenCV
    compose = cv2.cvtColor(np.asarray(
        compose), cv2.COLOR_RGB2BGR)

    cv2.imshow("video", compose)

    # 臉的框框
    # face = np.zeros((480, 640, 3), np.uint8)
    # face = cv2.rectangle(
    #     face, (self.max_x, self.max_y), (self.max_x+self.max_w, self.max_y+self.max_h), (255, 0, 0), 2)
    # cv2.imshow("face", face)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite('captest.jpg', frame)
        break

cap.release()
cv2.destroyAllWindows()


# cv2.imshow("gray", gray)
# cv2.imshow("blurred", blurred)
# cv2.imshow("binary", binary)

# text = np.zeros((480, 320, 3), np.uint8)
# cv2.putText(text, "test", (50, 50),
#             cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)
# imgStack = np.hstack((frame, text))

# add_ball = cv2.addWeighted(frame[0:64, 0:64, :],
#                            0.1, ball[0:64, 0:64, :], 0.9, 0)
# frame[0:64, 0:64, :] = add_ball
