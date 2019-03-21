import cv2
from Classes.Exceptions import *

class Image:
    def __init__(self, address: str):
        self._address = address

    def _read(self):
        self.image = cv2.imread(self._address)

    def save(self):
        try:
            cv2.imwrite(self._address, self.image)
        except NameError as e:
            raise ImageIsNotPresented("self.image is not specified")

    def get_address(self):
        return self._address

    def set_address(self, address):
        self._address = address

    def _convert_to_gray(self):
        try:
            self.gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        except NameError as e:
            raise ImageIsNotPresented("self.image is not specified")

    # Возможно этот метод нафиг не нужен
    def gaussian_blur(self, ksize, sigmaX, dst=None, sigmaY=None, borderType=None):
        self.image = cv2.GaussianBlur(self.image, ksize, sigmaX)

class Gray_Image(Image):
    def __init__(self, address: str):
        super().__init__(address)
        pass

class Edged_Image(Image):
    def __init__(self, address: str):
        super(Edged_Image, self).__init__(address)
        pass

class Closed_Image(Image):
    def __init__(self, address: str):
        super(Closed_Image, self).__init__(address)
        pass


if __name__ == "__main__":
    gi = Gray_Image()