import multiprocessing as mp
import time
from opencv import *
from window import *

if __name__ == '__main__':

    scene = Scene()
    camera = Camera()  # 不知道為什麼在main.py執行會報錯opencv.py就不會

    pb = mp.Process(target=scene.throwBall)
    pc = mp.Process(target=camera.captureFace)

    pb.start()
    pc.start()

    pb.join()
    pc.join()

    print("done")
