from vpython import *
import numpy as np


class Scene:
    W = 12                # 地板寬度
    L = 24                # 地板長度
    g = 9.8               # 重力加速度 9.8 m/s^2

    view = canvas(title="皮卡丘打排球", width=800, height=500, x=0, y=0,
                  center=vec(0, 5, 0), background=vec(0, 0.6, 0.6))
    floor = box(pos=vec(0, 0, 0), size=vec(
        W, 0.01, L), texture=textures.metal)
    net = box(pos=vec(0, 2.5, 0.1), size=vec(
        W, 5, 0.2), texture=textures.metal)
    player = box(pos=vec(0, 1.5, 9), size=vec(2, 3, 2), texture=textures.wood)

    # 原點
    dot = sphere(pos=vec(0, 0, 0), radius=1, color=color.blue)

    # 小球移動(呼叫玩家)
    def throwBall(self):
        size = 1.5            # 小球半徑
        v0 = 10.0             # 小球初速
        theta = radians(60)   # 小球抛射仰角, 用 radians 將單位轉為弧度
        t = 0.0               # 時間
        dt = 0.001            # 時間間隔
        i = 0                 # 小球撞地板次數

        ball = sphere(pos=vec(0, 5, self.L/4), radius=size,
                      color=color.red, make_trail=True,)
        ball_v = vec(0, v0 * sin(theta), -v0 * cos(theta))      # 小球速度(向量)
        ball_a = vec(0, -self.g, 0)                             # 小球加速度(向量)

        while(1):
            scene.playerMove()

            rate(1000)
            ball_v += ball_a * dt
            ball.pos += ball_v * dt

            if(ball.pos.y - self.floor.pos.y <= size + 0.5 * self.floor.height and ball_v.y < 0):
                i += 1
                # print(i, t, ball.pos.z)
                ball_v.y = -ball_v.y

            if(ball.pos.z > self.L/2 or ball.pos.z < -self.L/2):  # 測試
                ball_v.y = -ball_v.y
                ball_v.z = -ball_v.z

            t += dt

    # 玩家移動
    def playerMove(self):
        v = 5.0  # 玩家速度
        dt = 0.001
        center_x = 320
        center_y = 240

        f = open("./data.txt", mode="r")
        t_x = f.readline()
        t_y = f.readline()
        f.close()
        if(t_x != ''):
            center_x = float(t_x)
        if(t_y != ''):
            center_y = float(t_y)
        print(center_x)
        print(center_y)
        if(self.player.pos.x < -6 or self.player.pos.x > 6):
            pass
        elif(center_x == 320):
            pass
        elif(center_x < 320):
            self.player.pos.x -= v * dt
        else:
            self.player.pos.x += v * dt


if __name__ == '__main__':
    print("window main")
    scene = Scene()
    scene.throwBall()
    # scene.playerMove()
