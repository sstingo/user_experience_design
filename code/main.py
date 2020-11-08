import multiprocessing as mp
import time
from opencv import *
from scene import *

if __name__ == '__main__':
    camera = Camera()
    process = mp.Process(target=camera.captureFace)
    process.start()

    # view = Scene()

    # ball = Ball(view.floor, view.net)

    # ball.throwBall()

    process.join()
