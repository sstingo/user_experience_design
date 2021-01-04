import cv2
import numpy as np
from PIL import Image
import math

# if __name__ == '__main__':
# print("opencv main")

# 畫面
scene = 0

# 神奇寶貝球
ball_x = 320                   # 中心x
ball_y = 50                    # 中心y
ball_v_x = 0                   # 球的速度(x)
ball_v_y = 7                   # 球的速度(y)
# ball_theta = math.radians(90)  # 球的抛射仰角(弧度)

# 最大框框+它的中心
max_x = 0
max_y = 0
max_w = 5
max_h = 0
center_x = 320
center_y = 240

faceCascade = cv2.CascadeClassifier(
    "./haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
cap.set(3, 640)   # 寬
cap.set(4, 480)   # 高
cap.set(10, 100)  # 亮度

score = 0  # 分數

touch_flag = 0     # 玩家是否碰的到球標示(1:可以)
gameover_flag = 0  # 遊戲結束標示(1:遊戲結束)

while True:
    _x = 0
    _y = 0
    _w = 0
    _h = 0

    # 神奇寶貝球
    pokemon_ball = 'image/pokemon_ball.png'
    ball = Image.open(pokemon_ball)
    ball = ball.resize((120, 120))

    # 皮卡丘耳朵
    pikachu_ear = 'image/ear.png'
    ear = Image.open(pikachu_ear)

    # Read = Grab + Retrieve + Buffer (Block diagram)
    success, frame = cap.retrieve(cap.grab())
    # print(success)
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

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
    # frame = cv2.rectangle(
    #     frame, (max_x, max_y), (max_x+max_w, max_y+max_h), (255, 0, 0), 2)
    # frame = cv2.rectangle(
    #     frame, (int(center_x)-5, int(center_y)-5), (int(center_x)+5, int(center_y)+5), (255, 0, 0), -1)  # 中點
    frame = cv2.rectangle(frame, (max_x, max_y-5), (max_x+max_w,
                                                    max_y+5), (0, 255, 255), 1)  # 頭頂 #黃

    # 分數# 黑
    cv2.putText(frame, "score: " + str(score), (10, 30),
                cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 1, cv2.LINE_AA)

    # 邊界
    frame = cv2.line(frame, (0, 0), (640, 0),
                     (0, 255, 255), 3)  # 上
    frame = cv2.line(frame, (0, 0), (0, 480),
                     (0, 255, 255), 3)  # 左
    frame = cv2.line(frame, (640, 0), (640, 480),
                     (0, 255, 255), 3)  # 右
    frame = cv2.line(frame, (0, 480), (640, 480),
                     (0, 0, 255), 3)  # 下

    # OpenCV轉PIL
    frame = Image.fromarray(cv2.cvtColor(
        frame, cv2.COLOR_BGR2RGB))
    compose = Image.new('RGBA', (640, 480), (0, 0, 0, 0))
    compose.paste(frame, (0, 0))

    # 耳朵
    ear = ear.resize(
        (int(max_w * 2), int(max_w * 2 / 851 * 475)), Image.ANTIALIAS)
    ear_x = int(max_x - ear.size[1] * 0.15)
    ear_y = max_y - ear.size[1]
    if(ear_y >= 0):
        compose.paste(ear, (ear_x, ear_y), mask=ear)
        touch_flag = 1
    else:
        touch_flag = 0

    # 神奇寶貝球
    compose.paste(ball, (ball_x-60, ball_y-60), mask=ball)
    if(max_y-5 <= ball_y+60 and ball_y+60 <= max_y+5 and ball_v_y > 0 and touch_flag == 1):  # 碰到玩家 #下降->上升
        if(max_x <= ball_x and ball_x <= max_x + max_w*0.1):                 # 左 0~0.1
            ball_v_x = -3
            ball_v_y = -5
            score += 1
        elif(max_x + max_w*0.1 <= ball_x and ball_x <= max_x + max_w*0.45):  # 偏左 0.1~0.45
            ball_v_x = -2
            ball_v_y = -6
            score += 1
        elif(max_x + max_w*0.45 <= ball_x and ball_x <= max_x + max_w*0.55):  # 中 0.45~0.55
            ball_v_x = 0
            ball_v_y = -7
            score += 1
        elif(max_x + max_w*0.55 <= ball_x and ball_x <= max_x + max_w*0.9):  # 偏右 0.55~0.9
            ball_v_x = 2
            ball_v_y = -6
            score += 1
        elif(max_x + max_w*0.9 <= ball_x and ball_x <= max_x + max_w):       # 右 0.9~1
            ball_v_x = 3
            ball_v_y = -5
            score += 1
    if(ball_x <= 60 or ball_x >= 640-60):     # 碰到左右 #反彈
        ball_v_x = -ball_v_x
        ball_x += ball_v_x
    elif(ball_y >= 480-60):  # 碰到下框 #遊戲結束
        ball_v_x = 0
        ball_v_y = 0
        gameover_flag = 1
    elif(ball_v_y < 0 and ball_y <= 70):  # 碰到上框 # 上升->下降
        ball_v_y = -ball_v_y
        ball_y += ball_v_y
    else:
        ball_y += ball_v_y
        ball_x += ball_v_x

    # PIL轉OpenCV
    compose = cv2.cvtColor(np.asarray(
        compose), cv2.COLOR_RGB2BGR)

    # 遊戲結束
    if(gameover_flag == 1):
        cv2.putText(compose, "Game over", (65, 200),
                    cv2.FONT_HERSHEY_COMPLEX_SMALL, 4, (0, 0, 255), 4, cv2.LINE_AA)

    cv2.imshow("video", compose)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        # cv2.imwrite('captest.jpg', frame)
        break

cap.release()
cv2.destroyAllWindows()


# add_ball = cv2.addWeighted(frame[0:64, 0:64, :],
#                            0.1, ball[0:64, 0:64, :], 0.9, 0)
# frame[0:64, 0:64, :] = add_ball
