from PIL import Image

def decompress():
    old_image = Image.open("world_map.png")
    f = open("pixel_dict.txt")
    dict_txt = f.read()
    f.close()
    f2 = open("compressed.txt")
    compressed_string_list = f2.read().split(",")
    f2.close()

    pixel_dict = eval(dict_txt) #recompiles the dictionary
    pixel_dict = {v: k for k, v in pixel_dict.items()} #reverses the dictionary

    new_image = Image.new("RGB", (old_image.width, old_image.height))
    k = 0
    for i in range(new_image.height):
        for j in range(new_image.width):
            item = compressed_string_list[k]
            new_image.putpixel((j, i), pixel_dict[item])
            k += 1
    new_image.save("new_image.png")


if __name__ == "__main__":
    decompress()