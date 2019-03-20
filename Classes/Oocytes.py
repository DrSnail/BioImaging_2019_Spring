import cv2

class Oocytes:
    def __init__(self, image_adress):
        self.image_adress = image_adress
        self._cv2_image = cv2.imread(self.image_adress)

    def smooth_Gaussian(self, image):
        """
        Функция для сглаживания изображения по методу Гаусса
        :param image: Изображение, которое нужно сгладить
        :type image: cv2
        :return: None
        :rtype: None
        """
        return cv2.GaussianBlur(image, (3, 3), 0)

    def gray(self):
        """
        Преобразует в серый цвет изображение. Это необходимо, поскольку cv2 может работать только с серыми изображениями
        :return:
        :rtype:
        """
        self.gray = cv2.cvtColor(self._cv2_image, cv2.COLOR_BGR2GRAY)
        self.gray = self.smooth_Gaussian(self._cv2_image)
