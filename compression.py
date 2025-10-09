import sys
import decompression
from PIL import Image


def get_compression_string(image, pixel_dict):
    compressed_string = ''
    pixels_count = len(image.getcolors(maxcolors=(image.width * image.height)))  # number of unique pixels
    print("Number of unique pixels: " + str(pixels_count))
    keys = []
    for i in range(pixels_count):  # set up dict keys so each pixel can be replaced with a key
        keys.append(str(i))

    k = 0
    for i in range(image.height):
        for j in range(image.width):  #iterate over image
            print(i,j)
            pixel = image.getpixel((j, i))
            rounding_multiple = 30
            #pixel_dict takes form (r,g,b,a) = '1'
            rounded_pixel_red = rounding_multiple * round(pixel[0] / rounding_multiple)
            rounded_pixel_green = rounding_multiple * round(pixel[1] / rounding_multiple)
            rounded_pixel_blue = rounding_multiple * round(pixel[2] / rounding_multiple)
            rounded_pixel_alpha = rounding_multiple * round(pixel[3] / rounding_multiple)
            rounded_pixel = (rounded_pixel_red, rounded_pixel_green, rounded_pixel_blue, rounded_pixel_alpha)
            if not rounded_pixel in pixel_dict:  # pixel doesn't exist in dict
                pixel_dict[rounded_pixel] = keys[k]
                compressed_string += keys[k] + ','
                k += 1
            else:  # pixel DOES exist in map
                compressed_string += pixel_dict[rounded_pixel] + ','

    return compressed_string

def compress():
    image = Image.open("world_map.png")

    pixel_dict = {}
    # create map of chars to pixels and write chars to a string
    compressed_string = get_compression_string(image, pixel_dict)

    #print(pixel_dict)
    #print("Compressed String: " + compressed_string)
    print("Length of Compressed String: " + str(len(compressed_string)))

    #write compressed_string to txt file
    f = open("compressed.txt", "w")
    f.write(compressed_string)
    f.close()
    f2 = open("pixel_dict.txt", "w")
    f2.write(str(pixel_dict))
    f2.close()
    print("Length of Dictionary: " + str(len(pixel_dict)))


if __name__ == "__main__":
    compress()
    decompression.decompress()
