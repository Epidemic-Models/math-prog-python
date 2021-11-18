from matplotlib import image
import matplotlib.pyplot as plt
import numpy as np


class ImageHandler:
    def __init__(self, path_to_image):
        self.image = image.imread(path_to_image)

        self.__image_r = None
        self.__image_g = None
        self.__image_b = None

    @property
    def image_r(self):
        self.__image_r = self.image[:, :, 0]
        return self.__image_r

    @property
    def image_g(self):
        self.__image_g = self.image[:, :, 1]
        return self.__image_g

    @property
    def image_b(self):
        self.__image_b = self.image[:, :, 2]
        return self.__image_b

    def convert_to_greyscale(self):
        return 0.299 * self.image_r + 0.587 * self.image_g + 0.114 * self.image_b


class Convolution:
    def __init__(self, path_to_image, conv_filter):
        self.image = ImageHandler(path_to_image=path_to_image).convert_to_greyscale()
        self.conv_filter = conv_filter

        self.__height = None
        self.__width = None
        self.__filter_size = None

    @property
    def height(self):
        self.__height = self.image.shape[0]
        return self.__height

    @property
    def width(self):
        self.__width = self.image.shape[1]
        return self.__width

    @property
    def filter_size(self):
        self.__filter_size = self.conv_filter.shape[0]
        return self.__filter_size

    def convolve(self):
        r = (self.filter_size - 1) // 2

        result = np.zeros((self.height, self.width))
        for h in range(r, self.height - r):
            for w in range(r, self.width - r):
                # Crop the window
                window = self.image[h-r:h+r+1, w-r:w+r+1]
                # Execute element wise product
                elem_prod = self.conv_filter * window
                # Sum up the elements
                conv_result = np.sum(elem_prod)
                # Place the convolution result into the result array
                result[h, w] = conv_result

        return result[r:self.height - r, r:self.width - r]


def main():
    path_to_image = "./../data/donuts.jpg"
    image_handler = ImageHandler(path_to_image=path_to_image)
    image_handler_r = image_handler.image_r
    plt.imshow(image_handler_r, cmap="Reds")
    plt.show()

    image_greyscale = image_handler.convert_to_greyscale()
    plt.imshow(image_greyscale, cmap=plt.cm.gray)
    plt.show()

    image_greyscale_cropped = image_greyscale[75:200, 60:200]
    image_cropped = image_handler.image[75:200, 60:200, :]
    plt.imshow(image_greyscale_cropped, cmap=plt.cm.gray)
    plt.imshow(image_cropped)
    plt.show()

    print("Matrix shape: ", image_handler.image.shape)

    conv_filter = np.array([[-1, 0, 1],
                           [-1, 0, 1],
                           [-1, 0, 1]])
    convolver = Convolution(path_to_image=path_to_image,
                            conv_filter=conv_filter)

    image_edge = convolver.convolve()

    plt.imshow(image_edge, cmap=plt.cm.gray)
    plt.show()


if __name__ == "__main__":
    main()
