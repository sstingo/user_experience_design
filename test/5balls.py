from vpython import *

#  1. 參數設定
# 球半徑 0.05 m
size = 0.5
# 時間間隔
dt = 0.001

#  2. 畫面設定
scene = canvas(width=800, height=800, background=vec(0.5, 0.6, 0.5))
# x軸箭頭
x_axis = arrow(axis=vec(1, 0, 0), shaftwidth=0.01)
# y軸箭頭
y_axis = arrow(axis=vec(0, 1, 0), shaftwidth=0.01)
# z軸箭頭
z_axis = arrow(axis=vec(0, 0, 1), shaftwidth=0.01)


# 3. 球的設定
earth = sphere(pos=vec(0, 0, 0), radius=size, texture=textures.earth)
# marble = sphere(pos=vec(1, 0, 0), radius=size, texture=textures.marble)
# bricks = sphere(pos=vec(-1, 0, 0), radius=size, texture=textures.bricks)
wood = sphere(pos=vec(-2, 0, 0), radius=size, texture=textures.wood)
rough = sphere(pos=vec(2, 0, 0), radius=size, texture=textures.rough)

#  4. 運動
while True:
    rate(1000)
    earth.rotate(axis=vec(0, 0, 1), angle=-2*dt)
    # marble.rotate(axis=vec(0, 0, 1), angle=-2*dt)
    # bricks.rotate(axis=vec(0, 0, 1), angle=-2*dt)
    wood.rotate(axis=vec(0, 0, 1), angle=-2*dt)
    rough.rotate(axis=vec(0, 0, 1), angle=-2*dt)
