from vpython import *
import numpy as np


class Scene:
    W = 12                # 地板寬度
    L = 24                # 地板長度
    g = 9.8               # 重力加速度 9.8 m/s^2

    player_v = 5.0               # 玩家速度

    size = 1.5            # 小球半徑
    ball_v0 = 10.0        # 小球初速
    theta = radians(60)   # 小球抛射仰角, 用 radians 將單位轉為弧度
    t = 0.0               # 時間
    dt = 0.001            # 時間間隔
    i = 0                 # 小球撞地板次數

    view = canvas(title="皮卡丘打排球", width=800, height=500, x=0, y=0,
                  center=vec(0, 5, 0), background=vec(0, 0.6, 0.6))
    floor = box(pos=vec(0, 0, 0), size=vec(
        W, 0.01, L), texture=textures.metal)
    net = box(pos=vec(0, 2.5, 0.1), size=vec(
        W, 5, 0.2), texture=textures.metal)
    player = box(pos=vec(0, 1.5, 9), size=vec(2, 3, 2), texture=textures.wood)

    ball = sphere(pos=vec(0, 5, L/4), radius=size,
                  color=color.red, make_trail=True)
    ball_v = vec(0, ball_v0 * sin(theta),
                 -ball_v0 * cos(theta))                      # 小球速度(向量)
    ball_a = vec(0, -g, 0)                                   # 小球加速度(向量)

    # x軸箭頭
    x_axis = arrow(axis=vec(1, 0, 0), shaftwidth=0.01)
    # y軸箭頭
    y_axis = arrow(axis=vec(0, 1, 0), shaftwidth=0.01)
    # z軸箭頭
    z_axis = arrow(axis=vec(0, 0, 1), shaftwidth=0.01)

    # 遊戲開始(小球、玩家移動)
    def start(self):
        center_x = 320
        center_y = 240

        while(1):
            rate(1000)

            # 玩家
            f = open("./data.txt", mode="r")
            t_x = f.readline()
            t_y = f.readline()
            f.close()
            if(t_x != ''):
                center_x = float(t_x)
            if(t_y != ''):
                center_y = float(t_y)
            print(center_x)
            # print(center_y)
            if(self.player.pos.x <= -6 or self.player.pos.x >= 6):
                print("超出範圍")
                # pass
            elif(280 <= center_x and center_x <= 360):
                print("中間")
                # pass
            elif(center_x < 280):
                print("左邊")
                self.player.pos.x -= self.player_v * self.dt
            elif(center_x > 360):
                print("右邊")
                self.player.pos.x += self.player_v * self.dt

            # 小球
            self.ball_v += self.ball_a * self.dt
            self.ball.pos += self.ball_v * self.dt

            if(self.ball.pos.y - self.floor.pos.y <= self.size + 0.5 * self.floor.height and self.ball_v.y < 0):
                self.i += 1
                # print(i, t, ball.pos.z)
                self.ball_v.y = -self.ball_v.y

            if(self.ball.pos.z > self.L/2 or self.ball.pos.z < -self.L/2):  # 測試
                self.ball_v.y = -self.ball_v.y
                self.ball_v.z = -self.ball_v.z

            self.t += self.dt


if __name__ == '__main__':
    print("window main")
    scene = Scene()
    scene.start()
    # scene.playerMove()
