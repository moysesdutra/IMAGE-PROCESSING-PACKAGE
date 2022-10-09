from skimage.transform import resize
from skimage.transform import swirl

def resize_image(image, proportion):
    assert 0 <= proportion <=1, "Specify a valid proportion between 0 and 1."
    height = round(image.shape[0] * proportion)
    width = round(image.shape[1] * proportion)
    image_resized = resize(image, (height, width), anti_aliasing=True)
    return image_resized


def redemoinho(image, rotacao, forca, raio):
    assert 0 <= rotacao <= 360,  "Specify a valid rotation between 0 and 360º."
    return swirl(image, rotacao, forca, raio)