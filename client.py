from PIL import Image
from adbutils import adb
from numpy import asarray
import io

class Client:
    def __init__(self, serial):
        self.serial = serial
        self.device = adb.device(serial=self.serial)

    def capture_screen(self):
        png_bytes = self.device.shell("screencap 2>/dev/null -p", encoding=None)
        image = Image.open(io.BytesIO(png_bytes))
        return asarray(image)

    def click(self, point):
        print('Click: ({}, {})'.format(point[0], point[1]))
        self.device.click(point[0], point[1])