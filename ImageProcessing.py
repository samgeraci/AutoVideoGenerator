from PIL import Image


def crop_image(image_name):
    with Image.open(image_name) as im:
        top = im.height
        left = im.width
        bottom = 0
        right = 0
        px = im.load()
        # print("left: " + str(left) + "\ntop: " + str(top) + "\nright: " + str(right) + "\nbottom: " + str(bottom))
        # im.show()

        for x in range(im.width):
            for y in range(im.height):
                if px[x, y] != (25, 25, 26, 255):
                    if x > right:
                        right = x
                    if y > bottom:
                        bottom = y
                    if x < left:
                        left = x
                    if y < top:
                        top = y

        # print("left: " + str(left) + "\ntop: " + str(top) + "\nright: " + str(right) + "\nbottom: " + str(bottom))
        im1 = im.crop((left, top, right, bottom))
        # im1.show()

        px1 = im1.load()
        im2 = Image.new("RGBA", (im1.width + 64, im1.height + 64), (25, 25, 26))
        px2 = im2.load()

        for x in range(im1.width):
            for y in range(im1.height):
                px2[x + 32, y + 32] = px1[x, y]

        # im2.show()

        aspect_ratio = im2.height / im2.width
        if aspect_ratio > 0.5625:
            resize_ratio = 720 / im2.height
        else:
            resize_ratio = 1080 / im2.width

        new_size = (int(im2.width * resize_ratio), int(im2.height * resize_ratio))
        im3 = im2.resize(new_size)

        im3.show()