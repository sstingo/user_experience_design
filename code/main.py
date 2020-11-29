import multiprocessing as mp
import time
from opencv import *
from window import *
# 不用main分開執行, opencv.py用debug模式, window.py直接執行
if __name__ == '__main__':

    scene = Scene()
    camera = Camera()  # 不知道為什麼在main.py執行會報錯opencv.py就不會

    pb = mp.Process(target=scene.start)
    pc = mp.Process(target=camera.captureFace)

    pb.start()
    pc.start()

    pb.join()
    pc.join()

    print("done")
