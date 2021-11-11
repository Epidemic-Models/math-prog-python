from matplotlib import image
import matplotlib.pyplot as plt


def main():
    img = image.imread("./../data/donuts.jpg")
    plt.imshow(img)
    plt.show()

    print("Matrix shape: ", img.shape)


if __name__ == "__main__":
    main()
