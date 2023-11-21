import os
import sys
from PIL import Image

if __name__ == '__main__':

    if len(sys.argv)!= 2:
        print("Usage: python3 ImageByPixels.py <image_filename>")
        exit(1)


    image = Image.open(sys.argv[1])
    os.remove("output.txt")
    file = open("output.txt", "w")

    pixel_data = image.load()

    width, height = image.size

    size = 400 / width if width > height else 400 / height

    lastColor = tuple()
    transparentColor = (0, 0, 0, 0)

    file.write("push();\nrectMode(CORNER);\nnoStroke();\n")

    for x in range(width):
        for y in range(height):
            pixel = pixel_data[x, y]
            r, g, b, a = pixel
            if transparentColor == (r, g, b, a):
                continue
            if lastColor != (r, g, b, a):
                file.write(f"fill({r}, {g}, {b}, {a});\n")
                lastColor = (r, g, b, a)
            file.write(f"rect({x * size}, {y * size}, {size}, {size});\n")
            file.flush()


    file.write("pop();\n")
    file.close()

    #TODO: make this work, flushing the rectangle is not working
    #? rectangle is flushing too soon when colors change

    # rectangle = {"x": 0, "y": 0, "width": size, "height": size}

    # file.write("push();\nrectMode(CORNER);\nnoStroke();\n")

    # for x in range(width):
    #     for y in range(height):
    #         pixel = pixel_data[x, y]
    #         r, g, b, a = pixel
    #         if transparentColor == (r, g, b, a):
    #             continue
    #         if lastColor != (r, g, b, a):
    #             file.write(f"fill({r}, {g}, {b}, {a});\n")
    #             lastColor = (r, g, b, a)
    #             rectangle["x"] = x * size
    #             rectangle["y"] = y * size
    #             rectangle["width"] = size
    #             file.write(f"rect({rectangle['x']}, {rectangle['y']}, {rectangle['width']}, {rectangle['height']});\n")
    #             file.write("\n")
    #         elif rectangle['y'] == y * size:
    #             rectangle["width"] += size
    #         else:
    #             file.write(f"rect({rectangle['x']}, {rectangle['y']}, {rectangle['width']}, {rectangle['height']});\n")
    #             file.write("\n")

    #             rectangle["x"] = x * size
    #             rectangle["y"] = y * size
    #             rectangle["width"] = size
    #         file.flush()
