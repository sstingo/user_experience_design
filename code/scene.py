from vpython import *
import numpy as np


class Scene:
    W = 9                 # 地板寬度
    L = 18                # 地板長度
    g = 9.8               # 重力加速度 9.8 m/s^2

    scene = canvas(title="皮卡丘打排球", width=800, height=500, x=0, y=0,
                   center=vec(0, 5, 0), background=vec(0, 0.6, 0.6))
    floor = box(pos=vec(0, 0, 0), size=vec(
        W, 0.01, L), texture=textures.metal)
    net = box(pos=vec(0, 1.5, 0), size=vec(
        W, 3, 0.01), texture=textures.metal)


class Ball:
    W = 9                 # 地板寬度
    L = 18                # 地板長度
    g = 9.8               # 重力加速度 9.8 m/s^2

    def __init__(self, floor, net):
        self.floor = floor
        self.net = net

    def throwBall(self):
        size = 1.5            # 小球半徑
        v0 = 10               # 小球初速
        theta = radians(60)   # 小球抛射仰角, 用 radians 將單位轉為弧度
        t = 0                 # 時間
        dt = 0.001            # 時間間隔
        i = 0                 # 小球撞地板次數

        ball = sphere(pos=vec(0, 5, self.L/4), radius=size, color=color.red, make_trail=True,
                      v=vec(0, v0 * sin(theta), -v0 * cos(theta)), a=vec(0, -self.g, 0))

        while(ball.pos.z > -self.L/2):
            rate(1000)
            ball.v += ball.a * dt
            ball.pos += ball.v * dt

            if(ball.pos.y - self.floor.pos.y <= size + 0.5 * self.floor.height and ball.v.y < 0):
                i += 1
                print(i, t, ball.pos.z)
                ball.v.y = -ball.v.y

            t += dt


if __name__ == '__main__':
    print("test import")
#print(t, ball.pos.y)
