import multiprocessing as mp
import time
from opencv import *
from window import *

if __name__ == '__main__':

    scene = Scene()
    ball = Ball(scene.floor, scene.net)
    # camera = Camera()
    player = Player()

    pb = mp.Process(target=ball.throwBall)
    # pc = mp.Process(target=camera.captureFace)

    pb.start()
    # pc.start()

    pb.join()
    # pc.join()

    print("done")
