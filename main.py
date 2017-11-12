import numpy as np
import matplotlib.pyplot as plt
from PIL import ImageGrab
import time

# previous_im = np.array(ImageGrab.grab())
# t0 = time.time()
# while time.time() - t0 < 20:
#     time.sleep(0.25)
#     current_im = np.array(ImageGrab.grab())
#     diff = np.sum(np.abs(current_im - previous_im))
#     print(diff)
#     previous_im = current_im
#
# exit(0)

# plt.imshow(img, cmap='gray', interpolation='bicubic')
# plt.show()


class ImageStream:

    def __init__(self):
        self.stream = []

    def collect(self, collection_time, kickoff_wait=6, period=0.1, evaluate_online=True):
        time.sleep(kickoff_wait)
        t0 = time.time()
        while time.time() - t0 < collection_time:
            time.sleep(period)
            self.stream.append((np.array(ImageGrab.grab())[:800, :, :], time.time()))
            if evaluate_online:
                self.evaluate_online()

    def evaluate_diffs(self):
        for i in range(1, len(self.stream)):
            print(np.sum(np.abs(self.stream[i][0] - self.stream[i-1][0])))

    def evaluate_online(self):
        try:
            diff = np.sum(np.abs(self.stream[-1][0] - self.stream[-2][0]))
            if diff > 200000:
                print(f'Significant change: {diff}')
        except IndexError:
            pass

if __name__ == '__main__':
    im_stream = ImageStream()
    im_stream.collect(150)
    im_stream.evaluate_diffs()
