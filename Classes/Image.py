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

    def _get_gray_class(self):
        try:
            self.__gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        except NameError as e:
            raise ImageIsNotPresented("self.image is not specified")
        self._is_gray = True
        return Gray_Image(self._address, self.__gray_image)

    # Возможно этот метод нафиг не нужен
    def gaussian_blur(self, ksize, sigmaX, dst=None, sigmaY=None, borderType=None):
        self.image = cv2.GaussianBlur(self.image, ksize, sigmaX, dst, sigmaY, borderType)

class Gray_Image(Image):
    def __init__(self, address: str, gray_image):
        if super()._is_gray or self._is_edged:
            super().__init__(address)
            self.image = gray_image
        else:
            raise GrayIncorrectCreatingError

    def _get_edge_class(self, threshold1, threshold2, edges=None, apertureSize=None, L2gradient=None):
        self._is_edged = True
        try:
            self.__edge = cv2.Canny(self.image, threshold1, threshold2, edges, apertureSize, L2gradient)
        except Exception as e:
            self._is_edged = False
            raise e
        return Edged_Image(self._address, self.__edge, self._is_edged)

class Edged_Image(Image):
    def __init__(self, address: str, edge_image, is_edged = False):
        if is_edged:
            super(Edged_Image, self).__init__(address)
            self.image = edge_image
        else:
            raise EdgeIncorrectCreatingError

    def _get_closed_class(self, op, kernel, dst=None, anchor=None, iterations=None, borderType=None, borderValue=None):
        self._is_closed = True
        try:
            self.__closed = cv2.morphologyEx(self.image, op, kernel)
        except Exception as e:
            self._is_closed = False
            raise e
        return Closed_Image(self._address, self.__closed, True)

class Closed_Image(Image):
    def __init__(self, address: str, closed_image, is_closed = False):
        if is_closed:
            super(Closed_Image, self).__init__(address)
            self.image = closed_image
        else:
            raise ClosedIncorrectCreatingError



if __name__ == "__main__":
    gi = Gray_Image()