import cv2
import numpy as np


class Camera:
    _x = 0
    _y = 0
    _w = 0
    _h = 0

    def captureFace(self):
        faceCascade = cv2.CascadeClassifier(
            "./haarcascade_frontalface_default.xml")

        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        if cap.isOpened():
            print("open")
        cap.set(3, 640)
        cap.set(4, 480)
        cap.set(10, 100)

        while True:
            max_w = 0
            max_h = 0

            success, frame = cap.read()
            frame = cv2.flip(frame, 1)

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            blurred = cv2.GaussianBlur(gray, (11, 11), 0)
            binary = cv2.Canny(blurred, 20, 160)

            faces = faceCascade.detectMultiScale(gray, 1.1, 4)
            for (x, y, w, h) in faces:
                if w * h > max_w * max_h:
                    max_w = w
                    max_h = h
                    self._x = x
                    self._y = y
                    self._w = w
                    self._h = h

            # webcam畫面
            frame = cv2.rectangle(
                frame, (self._x, self._y), (self._x+self._w, self._y+self._h), (255, 0, 0), 2)
            cv2.imshow("video", frame)

            # 臉的框框
            face = np.zeros((480, 640, 3), np.uint8)
            face = cv2.rectangle(
                face, (self._x, self._y), (self._x+self._w, self._y+self._h), (255, 0, 0), 2)
            cv2.imshow("face", face)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                cv2.imwrite('captest.jpg', frame)
                break

        cap.release()
        cv2.destroyAllWindows()


# if __name__ == '__main__':
#     camera = Camera()
#     camera.captureFace()


# cv2.imshow("gray", gray)
# cv2.imshow("blurred", blurred)
# cv2.imshow("binary", binary)

# text = np.zeros((480, 320, 3), np.uint8)
# cv2.putText(text, "test", (50, 50),
#             cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)
# imgStack = np.hstack((frame, text))
