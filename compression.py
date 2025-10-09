from PIL import Image


def get_rounded_pixels(image):
    rounded_pixels = []
    for i in range(image.height):
        for j in range(image.width):  #iterate over image
            pixel = image.getpixel((j, i))
            print(pixel)
            rounding_multiple = 10

            rounded_pixel_red = rounding_multiple * round(pixel[0] / rounding_multiple)
            rounded_pixel_green = rounding_multiple * round(pixel[1] / rounding_multiple)
            rounded_pixel_blue = rounding_multiple * round(pixel[2] / rounding_multiple)
            rounded_pixel_alpha = rounding_multiple * round(pixel[3] / rounding_multiple)
            rounded_pixel = (rounded_pixel_red, rounded_pixel_green, rounded_pixel_blue, rounded_pixel_alpha)
            rounded_pixels.append(rounded_pixel)

    return rounded_pixels


def compress():
    old_image = Image.open("transparent_cat.png")
    print(old_image.mode)
    # create map of chars to pixels and write chars to a string
    rounded_pixels = get_rounded_pixels(old_image)

    new_image = Image.new("RGBA", (old_image.width, old_image.height))
    k = 0
    for i in range(new_image.height):
        for j in range(new_image.width):
            new_image.putpixel((j, i), rounded_pixels[k])
            k += 1
    new_image.save("new_image.png")


if __name__ == "__main__":
    compress()
