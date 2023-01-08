from PIL import Image


def get_boarders(image_name, background_color):
    with Image.open(image_name) as im:
        top = im.height
        left = im.width
        bottom = 0
        right = 0
        px = im.load()

        for x in range(im.width):
            for y in range(im.height):
                if px[x, y] != background_color:
                    if x > right:
                        right = x
                    if y > bottom:
                        bottom = y
                    if x < left:
                        left = x
                    if y < top:
                        top = y
        bottom += 1
        right += 1
        return left, top, right, bottom


def crop_image(image_name, boarders, background_color):
    with Image.open(image_name) as im:
        im = im.crop(boarders)

        px = im.load()
        im_new = Image.new("RGBA", (im.width + 64, im.height + 64), background_color)
        px_new = im_new.load()

        for x in range(im.width):
            for y in range(im.height):
                px_new[x + 32, y + 32] = px[x, y]

        aspect_ratio = im_new.height / im_new.width
        if aspect_ratio > 0.5625:
            resize_ratio = 720 / im_new.height
        else:
            resize_ratio = 1280 / im_new.width

        new_size = (int(im_new.width * resize_ratio), int(im_new.height * resize_ratio))
        im_new = im_new.resize(new_size)

        im = Image.new("RGBA", (1280, 720), background_color)
        x_offset = int((1280 - im_new.width) / 2)
        y_offset = int((720 - im_new.height) / 2)

        px = im.load()
        px_new = im_new.load()

        for x in range(im_new.width):
            for y in range(im_new.height):
                px[x + x_offset, y + y_offset] = px_new[x, y]
        im.save(image_name)
