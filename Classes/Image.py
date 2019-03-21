import cv2
from Classes.Exceptions import *

class Image:
    def __init__(self, address: str):
        self._address = address
        pass

    def read(self):
        self.image = cv2.imread(self._address)

    def save(self):
        try:
            cv2.imwrite(self._address, self.image)
        except Exception as e:
            raise ImageIsNotPresented()

    def get_address(self):
        return self._address

    def set_address(self, address):
        self._address = address

class Grey_Image(Image):
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