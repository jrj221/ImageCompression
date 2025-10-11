import math

from PIL import Image

def round_pixel(pixel, mode, image, new_palette):
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
        case "P":
            palette = image.getpalette()
            # palette takes form R0, G0, B0, R1, G1, B1.
            # To access the pixel-th color in the palette, we need to multiply by 3

            #try both rounding down and also telling them to round to 250 instead of 260 if 255 or 256
            red = rounding_multiple * math.floor(palette[pixel * 3] / rounding_multiple)
            green = rounding_multiple * math.floor(palette[pixel * 3 + 1] / rounding_multiple)
            blue = rounding_multiple * math.floor(palette[pixel * 3 + 2] / rounding_multiple)
            rgb = (red, green, blue)
            palette_tuples = [tuple(palette[i:i + 3]) for i in range(0, len(palette), 3)]
            #iteratively creates rgb tuples by grabbing contiguous sets of 3 indices and stepping through the range 3 at a time
            new_palette[pixel * 3: pixel * 3 + 3] = list(rgb) #start creating new palette, but drawing from the same indices as before
            rounded_pixel = pixel # not altering pixel for P mode, just the palette itself


    return rounded_pixel


def compress():
    old_image = Image.open("P_test--transparent_cat.png")
    mode = old_image.mode
    new_palette = [0 for i in range(768)] #is it smart to initialize this for all image modes? probably not
    new_image = Image.new(mode, (old_image.width, old_image.height))

    for i in range(old_image.width):
        for j in range(old_image.height):  #iterate over image
            pixel = old_image.getpixel((i, j))
            rounded_pixel = round_pixel(pixel, mode, old_image, new_palette)
            new_image.putpixel((i, j), rounded_pixel)

    new_image.putpalette(new_palette)

    new_image.save("new_image.png")


if __name__ == "__main__":
    compress()
