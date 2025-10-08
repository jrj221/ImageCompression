import sys

from PIL import Image
#IDEA: invert the map in each direction. Easier to map pixels to characters when first compressing
# but when you are interpreting the compressed txt file, it would be easier to map characters to pixels.

def get_compression_string(image, pixel_dict):
    compressed_string = ''
    pixels_count = len(image.getcolors(maxcolors=(image.width * image.height)))  # number of unique pixels
    print("Number of unique pixels: " + str(pixels_count))
    keys = []
    for i in range(pixels_count):  # set up dict keys so each pixel can be replaced with a key
        keys.append(str(i))

    k = 0
    for i in range(image.width):
        for j in range(image.height):  #iterate over image
            print(i,j)
            pixel = image.getpixel((i, j))
            #pixel_dict takes form (r,g,b,a) = '1'


            if not pixel in pixel_dict:  # pixel doesn't exist in dict
                pixel_dict[pixel] = keys[k]
                compressed_string += keys[k] + ','
                k += 1
            else:  # pixel DOES exist in map
                compressed_string += pixel_dict[pixel] + ','

    return compressed_string

def main():
    image = Image.open("world_map.png")

    pixel_dict = {}
    # create map of chars to pixels and write chars to a string
    compressed_string = get_compression_string(image, pixel_dict)

    print(pixel_dict)
    #print("Compressed String: " + compressed_string)
    print("Length of Compressed String: " + str(len(compressed_string)))

    #write compressed_string to txt file
    f = open("compressed.txt", "w")
    f.write(compressed_string)
    f.close()
    print("Size of compressed.txt: " + str(sys.getsizeof("compressed.txt")))


if __name__ == "__main__":
    main()
