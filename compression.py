from PIL import Image

def main():
    image = Image.open("colorBox.png")
    numColors = len(image.getcolors())
    keys = []
    for i in range(numColors):
        keys.append(str(i))
    map = {}
    k = 0
    compressString = ""
    for i in range(10):
        for j in range(10):
            pixel = image.getpixel((i, j))
            if not any(pixel in pixelList for pixelList in map.values()): # pixel doesn't exist in map
                map[keys[k]] = [pixel]
                compressString += keys[k] + ','
                k = k + 1
            else: # pixel DOES exist in map
                for key in map:
                    for item in map[key]:
                        if item == pixel:
                            compressString += key + ','



    print(map)
    print(compressString)


if __name__ == "__main__":
    main()