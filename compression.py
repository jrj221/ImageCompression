from PIL import Image
#IDEA: invert the map in each direction. Easier to map pixels to characters when first compressing
# but when you are interpreting the compressed txt file, it would be easier to map characters to pixels.

def get_compression_string(image, pixel_dict):
    compressed_string = ''
    pixels_count = len(image.getcolors())  # number of unique pixels
    keys = []
    for i in range(pixels_count):  # set up dict keys so each pixel can be replaced with a key
        keys.append(str(i))

    k = 0
    for i in range(10):
        for j in range(10):  #iterate over image
            pixel = image.getpixel((i, j))
            #pixel_dict takes form '1' = RGBA(0,0,0,0)
            if not pixel in pixel_dict.values():  # pixel doesn't exist in dict
                pixel_dict[keys[k]] = pixel
                compressed_string += keys[k] + ','
                k += 1
            else:  # pixel DOES exist in map
                key = next((key for key in pixel_dict if pixel == pixel_dict[key]), None)
                compressed_string += key + ','

    return compressed_string

def main():
    image = Image.open("colorBox.png")
    pixel_dict = {}
    compressed_string = get_compression_string(image, pixel_dict)

    print(pixel_dict)
    print(compressed_string)


if __name__ == "__main__":
    main()
