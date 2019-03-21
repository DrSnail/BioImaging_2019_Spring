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
            self.__gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        except NameError as e:
            raise ImageIsNotPresented("self.image is not specified")
        self._is_gray = True
        return _Gray_Image(self._address, self.__gray_image)

    # Возможно этот метод нафиг не нужен
    def gaussian_blur(self, ksize, sigmaX, dst=None, sigmaY=None, borderType=None):
        self.image = cv2.GaussianBlur(self.image, ksize, sigmaX, dst, sigmaY, borderType)

class _Gray_Image(Image):
    def __init__(self, address: str, gray_image):
        if super()._is_gray:
            super().__init__(address)
            self.image = gray_image
        else:
            raise GrayIncorrectCreatingError

    def _edge_finding(self, threshold1, threshold2, edges=None, apertureSize=None, L2gradient=None):
        self._is_edged = True
        try:
            cv2.Canny(self.image, threshold1, threshold2, edges, apertureSize, L2gradient)
        except Exception as e:
            self._is_edged = False
            raise e

class Edged_Image(Image):
    def __init__(self, address: str):
        super(Edged_Image, self).__init__(address)
        pass

class Closed_Image(Image):
    def __init__(self, address: str):
        super(Closed_Image, self).__init__(address)
        pass


if __name__ == "__main__":
    gi = _Gray_Image()