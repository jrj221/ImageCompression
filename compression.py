import math
from PIL import Image


def round_pixel(pixel, mode, image):
    rounding_multiple = 10
    rounded_pixel = None
    match mode:
        case "RGBA":
            red = rounding_multiple * round(pixel[0] / rounding_multiple)
            green = rounding_multiple * round(pixel[1] / rounding_multiple)
            blue = rounding_multiple * round(pixel[2] / rounding_multiple)
            alpha = rounding_multiple * round(pixel[3] / rounding_multiple)
            rounded_pixel = (red, green, blue, alpha)
        case "RGB":
            red = rounding_multiple * round(pixel[0] / rounding_multiple)
            green = rounding_multiple * round(pixel[1] / rounding_multiple)
            blue = rounding_multiple * round(pixel[2] / rounding_multiple)
            rounded_pixel = (red, green, blue)

    return rounded_pixel


def compress():
    # SET UP VARIABLES
    filename = "car.png"
    name = filename.split('.')[0]
    ext = filename.split('.')[1]
    old_image = Image.open(filename)
    mode = old_image.mode
    if mode != "RGB" and mode != "RGBA":
        print(f"This program does not support {mode} images.")
        return
    new_image = Image.new(mode, (old_image.width, old_image.height))


    # ROUND PIXELS AND WRITE TO NEW IMAGE
    pixel_count = old_image.width * old_image.height
    p = 0
    for i in range(old_image.width):
        for j in range(old_image.height):  #iterate over image
            print(f"\rProgress: {round(100 * p/pixel_count)}%", end="", flush=True)
            p += 1
            pixel = old_image.getpixel((i, j))
            rounded_pixel = round_pixel(pixel, mode, old_image)
            new_image.putpixel((i, j), rounded_pixel)

    new_image.save(name + "_compressed." + ext)


if __name__ == "__main__":
    compress()
